#!/usr/bin/env python

from langchain_community.utilities import SQLDatabase
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from pydantic import BaseModel
from dotenv import load_dotenv
from dedent import dedent
import sys

# load_dotenv("lab.env")
ai_model = "qwen2.5:7b-instruct"

# 1. Connect to DB
db = SQLDatabase.from_uri(
    "sqlite:///data2.db",
    include_tables=None,
    sample_rows_in_table_info=3
)

# 2. SQL tool
query_tool = QuerySQLDatabaseTool(db=db)

# 3. LLM with tool binding (Ollama)
llm = ChatOllama(
    model=ai_model,
    temperature=0,
).bind_tools([query_tool])

# 4. Prompt for SQL generation
sql_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a SQL assistant. Use ONLY the provided schema."),
    ("system", "You MUST use the SQL SCHEMA provided in the prompt to answer the question."),
    ("system", "Schema: {schema}"),
    ("user", "Question: {question}")
])

# 5. Prompt for natural language answer
nl_prompt = ChatPromptTemplate.from_messages([
    ("system", dedent("""You are a professional sales reporter.
        Turn the SQL result into a clear English sentence.
        Pay attention to the prompts provided to ensure you are returning the correct information.
        Check your answer for accuracy and completeness and that it meets the prompt requirements.""")),
    ("user", "SQL result: {result}"),
])

# 6. Tool execution
def run_tool(response):
    if response.tool_calls:
        try:
            if sys.argv[1] == "debug":
                print("TOOL CALL:", response.tool_calls)
        except:
            pass
        for call in response.tool_calls:
            if call["name"] == "sql_db_query":
                sql = call["args"]["query"]
                return query_tool.run(sql)
    return response.content

def debug_sql_prompt(prompt):
    print("\n--- SQL PROMPT SENT TO LLM ---")
    print(prompt)
    print("--- END SQL PROMPT ---\n")
    return prompt

# 7. LCEL pipeline
chain = (
    {
        "schema": lambda _: db.get_table_info(),
        "question": RunnablePassthrough()
    }
    | sql_prompt
    # | RunnableLambda(debug_sql_prompt)
    | llm
    | RunnableLambda(run_tool)
    # | (lambda result, question: {"result": result, "question": RunnablePassthrough()})
    | nl_prompt
    | ChatOllama(model=ai_model, temperature=0)
)

# 8. Run it
print("Total sales of Nova One")
result = chain.invoke("What is the total Nova One sales for the year?")
print(result.content)

print("Total Nova One units sold")
result = chain.invoke("How many Nova One units were sold?")
print(result.content)

print("Worst selling product")
result = chain.invoke("What is the worst selling product?")
print(result.content)

print("Best selling product")
result = chain.invoke("What is the best selling product?")
print(result.content)
