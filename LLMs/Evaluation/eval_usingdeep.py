#!/usr/bin/env python

from dotenv import load_dotenv
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from deepeval.test_case import LLMTestCase
from deepeval import evaluate
from deepeval.metrics import SummarizationMetric
from deepeval.evaluate import AsyncConfig

# Load environment variables from lab.env file
load_dotenv('../lab.env')

df = pd.read_csv('assets.csv')
df.shape

prompt_template = ChatPromptTemplate.from_messages([
    ('system', 'Summarize the following text in no more than 5 sentences.'),
    ('user', '{text}')
])

gpt41 = ChatOpenAI(model='gpt-4.1-mini')
gpt41mini = ChatOpenAI(model='gpt-4.1-nano')

chain41 = prompt_template | gpt41 | StrOutputParser()
chain41mini = prompt_template | gpt41mini | StrOutputParser()

# print("CHAIN 41")
# print(chain41.invoke(df['text'][0]))
# print("MINI")
# print(chain41mini.invoke(df['text'][0]))

df['41'] = None
df['41mini'] = None

for i, row in df.iterrows():
    print(i)
    df.at[i, '41'] = chain41.invoke(row['text'])
    df.at[i, '41mini'] = chain41mini.invoke(row['text'])

tests_41 = []
tests_41mini = []

for i, row in df.iterrows():
    tests_41.append(LLMTestCase(input=row['text'], actual_output=row['41']))
    tests_41mini.append(LLMTestCase(input=row['text'], actual_output=row['41mini']))

len(tests_41), len(tests_41mini)

metric = SummarizationMetric(model='gpt-4.1-nano')
# results_41 = evaluate(tests_41, [metric], async_config=AsyncConfig(run_async=False))
# results_41mini = evaluate(tests_41mini, [metric], async_config=AsyncConfig(run_async=False))
results_41 = evaluate(tests_41, [metric])
results_41mini = evaluate(tests_41mini, [metric])
print("41 results:", results_41)
print("41mini results:", results_41mini)

# # results_41, results_41mini
# for r in results_41:
#     print("41 verdict:", r.verdicts, "score:", r.score)

# for r in results_41mini:
#     print("41mini verdict:", r.verdicts, "score:", r.score)

# [SOLUTION]
results_41.test_results[0]
# [/SOLUTION]

mean_41 = sum(t.metrics_data[0].score for t in results_41.test_results) / len(results_41.test_results)
mean_41mini = sum(t.metrics_data[0].score for t in results_41mini.test_results) / len(results_41mini.test_results)

mean_41, mean_41mini

# [SOLUTION]
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams

custom_metric = GEval(
    name='Spiciness',
    model='gpt-4.1-nano',
    criteria='Determine the "spiciness" of the actual output based on the input text. Spiciness is how sassy, sarcastic, or brat the actual output is.',
    evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT]
)

results_41_custom = evaluate(tests_41, [custom_metric], async_config=AsyncConfig(run_async=False))
results_41mini_custom = evaluate(tests_41mini, [custom_metric], async_config=AsyncConfig(run_async=False))

mean_41_custom = sum(t.metrics_data[0].score for t in results_41_custom.test_results) / len(results_41_custom.test_results)
mean_41mini_custom = sum(t.metrics_data[0].score for t in results_41mini_custom.test_results) / len(results_41mini_custom.test_results)

mean_41_custom, mean_41mini_custom
# [/SOLUTION]