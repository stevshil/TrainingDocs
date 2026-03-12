#!/usr/bin/env python

from langchain_community.utilities import SQLDatabase
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv("../lab.env")

# 1. Connect to DB
db = SQLDatabase.from_uri("sqlite:///data.db")

# 2. SQL tool
query_tool = QuerySQLDatabaseTool(db=db)

# 3. LLM with tool binding
llm = ChatOpenAI(model="gpt-4o-mini").bind_tools([query_tool])

# 4. Prompt for SQL generation
sql_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a SQL assistant. Use ONLY the provided schema."),
    ("human", "Schema:\n{schema}\n\nQuestion: {question}")
])

# 5. Prompt for natural language answer
nl_prompt = ChatPromptTemplate.from_messages([
    ("system", "Turn the SQL result into a clear English sentence."),
    ("user", "What is the total Nova One sales for the year"),
    ("assistant", "The total sales for the year of the Nova One is $199,200."),
    ("human", "SQL result: {result}")
])

# 6. Tool execution
def run_tool(response):
    if response.tool_calls:
        for call in response.tool_calls:
            if call["name"] == "sql_db_query":
                sql = call["args"]["query"]
                return query_tool.run(sql)
    return response.content

# 7. LCEL pipeline
chain = (
    {
        "schema": lambda _: db.get_table_info(),
        "question": RunnablePassthrough()
    }
    | sql_prompt
    | llm
    | RunnableLambda(run_tool)
    | (lambda result: {"result": result})
    | nl_prompt
    | ChatOpenAI(model="gpt-4o-mini")
)

# 8. Run it
result = chain.invoke("What is the total Nova One sales for the year?")
print(result.content)
result = chain.invoke("What is the worst selling product for the year relative to its price?")
print(result.content)
