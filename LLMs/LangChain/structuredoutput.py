#!/usr/bin/env python

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('lab.env')

class Person(BaseModel):
    name: str
    age: Optional[int] = None
    skills: List[str] = Field(description="List of person's skills")

llm = ChatOpenAI(model="gpt-4o-mini").with_structured_output(Person)
response = llm.invoke("Extract info about John, age 30, who knows Python and SQL")
# Returns a Person object

john = response
print(f"{john.name} is {john.age} years old and specialies in {" ".join(john.skills)}")