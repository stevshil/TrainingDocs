#!/usr/bin/env python

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('../lab.env')

class Person(BaseModel):
    name: str
    age: Optional[int] = None
    skills: List[str] = Field(description="List of person's skills")

llm = ChatOpenAI(model="gpt-4o-mini").with_structured_output(Person)
john = llm.invoke("Extract info about John, age 30, who knows Python and SQL")
bob = llm.invoke("Extract info about Bob who is a senior executive, age 45, who knows Finance and Leadership")
# Returns a Person object
print(f"{john.name} is {john.age} years old and specialies in {" ".join(john.skills)}")
print(f"{bob.name} is {bob.age} years old and specialies in {" ".join(bob.skills)}")