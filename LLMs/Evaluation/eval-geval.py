#!/usr/bin/env python

from dotenv import load_dotenv
from datasets import load_dataset
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from deepeval import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval
from deepeval.evaluate import AsyncConfig

# Load environment variables
load_dotenv('../lab.env')

# Load HumanEval dataset
dataset = load_dataset("openai_humaneval")["test"]
print(dataset)  # Confirms: Dataset with 164 rows and features ['task_id', 'prompt', 'canonical_solution', 'test', 'entry_point']

# Initialize LLM
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.5)

# Select the sample prompt
sample = dataset[1]  # Matches your example: HumanEval/1
prompt = sample["prompt"]
canonical_solution = sample["canonical_solution"]

# Define a prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Complete the following code based on the prompt."),
    ("user", "{prompt}")
])

# Create a pipeline
output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser

# Generate completion
completion = chain.invoke({"prompt": prompt})

print(f"Prompt:\n{prompt}")
print(f"Generated Completion:\n{completion}")
print(f"Canonical Solution:\n{canonical_solution}")
print("-------------------------------")
print("")

# Define a correctness metric
correctness_metric = GEval(
    name="Code Correctness",
    model="gpt-4.1-mini",
    criteria="Evaluate if the generated code correctly implements the logic described in the prompt and matches the functionality of the canonical solution.",
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT
    ],
    # verbose_mode=True  # Useful for seeing details
)

test_case = LLMTestCase(
    input=prompt,
    actual_output=completion,
    expected_output=canonical_solution
)

evaluate(test_cases=[test_case], metrics=[correctness_metric], async_config=AsyncConfig(run_async=False))

print("--------------------------------")
print("")

# [SOLUTION] Challenge 1
# Select multiple samples for evaluation
samples = dataset.select(range(3))

# Generate completions and create test cases
test_cases = []
for sample in samples:
    prompt = sample["prompt"]
    canonical_solution = sample["canonical_solution"]
    
    # Generate completion
    completion = chain.invoke({"prompt": prompt})
    
    # Create test case
    test_case = LLMTestCase(
        input=prompt,
        actual_output=completion,
        expected_output=canonical_solution
    )
    test_cases.append(test_case)

# Use DeepEval's evaluate() function for bulk evaluation
# This is more efficient and provides better reporting than calling measure() in a loop
evaluate(test_cases=test_cases, metrics=[correctness_metric], async_config=AsyncConfig(run_async=False))

# Calculate average score
average_score = sum(correctness_metric.score for _ in test_cases) / len(test_cases)
print(f"\nAverage Correctness Score: {average_score:.2f}")
# [/SOLUTION]

# [SOLUTION] Challenge 2
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

# Define a readability metric
readability_metric = GEval(
    name='Code Readability',
    model='gpt-4.1-mini',
    evaluation_steps=[
        'Assess the simplicity and clarity of the actual_output’s structure.',
        'Evaluate whether variable names in the actual_output are descriptive and meaningful.',
        'Penalize unnecessary complexity or convoluted logic in the actual_output.',
        'Compare readability with the expected_output, favoring concise and clear code.'
    ],
    evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
    verbose_mode=True  # Enable detailed output for debugging
)

test_case = LLMTestCase(
    input="Write a function to check if any number in a list exceeds a threshold.",
    actual_output="def exceeds_threshold(lst, thresh):\n    return any(x > thresh for x in lst)",
    expected_output="def exceeds_threshold(numbers, threshold):\n    for num in numbers:\n        if num > threshold:\n            return True\n    return False"
)

# Measure readability
evaluate(test_cases=[test_case], metrics=[readability_metric], async_config=AsyncConfig(run_async=False))
readability_metric.measure(test_case)
print(f'Readability Score: {readability_metric.score}')
print(f'Reason: {readability_metric.reason}')
# [/SOLUTION]