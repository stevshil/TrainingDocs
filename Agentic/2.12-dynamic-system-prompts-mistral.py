import os
from datetime import datetime
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai import Agent, RunContext

model = OpenAIChatModel("mistral:7b")

agent = Agent(
    model = model,
    deps_type=dict,
)

@agent.system_prompt
def generate_prompt(ctx: RunContext[dict]) -> str:
    user_name = ctx.deps.get('user_name', 'User')
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    return (
        f"You are a helpful assistant for {user_name}. "
        f"Today's date is {current_date}. "
        "Provide information relevant to the current context."
    )

# Pass deps at run time so the prompt is built from runtime values.
result = agent.run_sync('What can you help me with?', deps={'user_name': 'Alice'})

print(result.output)