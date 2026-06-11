import asyncio
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Awaitable
from graphlib import TopologicalSorter
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel


# -----------------------------
# Workflow Data Models
# -----------------------------

class TaskInput(BaseModel):
    text: str | None = None
    topics: List[str] | None = None
    results: Dict[str, str] | None = None


class TaskOutput(BaseModel):
    text: str | None = None
    results: Dict[str, str] | None = None


# -----------------------------
# Agents (Mistral or Qwen)
# -----------------------------

class ResearchAgent(Agent):
    model = OpenAIChatModel("qwen2.5:7b-instruct")   # or OpenAIChatModel("qwen2.5:7b-instruct")


class SummaryAgent(Agent):
    model = OpenAIChatModel("mistral:7b")


research_agent = ResearchAgent()
summary_agent = SummaryAgent()


# -----------------------------
# Task Definition
# -----------------------------

@dataclass
class Task:
    name: str
    run: Callable[[TaskInput], Awaitable[TaskOutput]]
    depends_on: List[str] = field(default_factory=list)


# -----------------------------
# Async Workflow Engine
# -----------------------------

class AsyncWorkflow:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.graph: Dict[str, set] = {}

    def add_task(self, task: Task):
        self.tasks[task.name] = task
        self.graph[task.name] = set(task.depends_on)

    async def run(self, initial_inputs: Dict[str, TaskInput]):
        sorter = TopologicalSorter(self.graph)
        sorter.prepare()

        results: Dict[str, TaskOutput] = {}

        while sorter.is_active():
            ready = sorter.get_ready()

            jobs = []
            names = []

            for name in ready:
                task = self.tasks[name]

                # Merge dependency outputs
                if task.depends_on:
                    merged_results = {}
                    merged_text = ""

                    for dep in task.depends_on:
                        dep_out = results[dep]
                        if dep_out.results:
                            merged_results.update(dep_out.results)
                        if dep_out.text:
                            merged_text += dep_out.text + "\n"

                    input_model = TaskInput(
                        text=merged_text.strip(),
                        topics=initial_inputs.get("prepare", TaskInput()).topics,
                        results=merged_results or None
                    )
                else:
                    input_model = initial_inputs[name]

                jobs.append(task.run(input_model))
                names.append(name)

            outputs = await asyncio.gather(*jobs)

            for name, output in zip(names, outputs):
                results[name] = output
                sorter.done(name)

        return results


# -----------------------------
# Realistic Agent‑Powered Tasks
# -----------------------------

async def prepare_topics(input: TaskInput) -> TaskOutput:
    return TaskOutput(text="Preparing research topics...")

async def research_topic(input: TaskInput, topic: str) -> TaskOutput:
    r = await research_agent.run(f"Research the topic: {topic}. Provide a concise paragraph.")
    return TaskOutput(results={topic: r.output})

async def summarise_all(input: TaskInput) -> TaskOutput:
    combined = "\n\n".join(f"{k}: {v}" for k, v in input.results.items())
    s = await summary_agent.run(f"Summarise the following research into a single coherent report:\n\n{combined}")
    return TaskOutput(text=s.output)


# -----------------------------
# Build and Run Workflow
# -----------------------------

async def main():
    topics = ["quantum computing", "renewable energy", "AI safety", "climate modelling"]

    wf = AsyncWorkflow()

    # Sequential start
    wf.add_task(Task("prepare", prepare_topics))

    # Parallel middle
    for topic in topics:
        wf.add_task(Task(
            name=f"research_{topic.replace(' ', '_')}",
            run=lambda inp, t=topic: research_topic(inp, t),
            depends_on=["prepare"]
        ))

    # Sequential end
    wf.add_task(Task(
        name="final_summary",
        run=summarise_all,
        depends_on=[f"research_{t.replace(' ', '_')}" for t in topics]
    ))

    initial = {
        "prepare": TaskInput(
            text="Start research",
            topics=topics
        )
    }

    results = await wf.run(initial)

    print("\nFINAL SUMMARY:\n")
    print(results["final_summary"].text)


if __name__ == "__main__":
    asyncio.run(main())
