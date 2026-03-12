#!/usr/bin/env python

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.tools import tool
from pydantic import BaseModel
from typing import List

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('lab.env')

# Define output schema
class AnalysisResult(BaseModel):
    summary: str
    key_points: List[str]
    next_steps: List[str]

# Create a tool
@tool
def analyze_data(data: str) -> str:
    """Analyze the provided data and return insights."""
    return f"Analysis of {data}"

# Create chain
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a data analyst."),
    ("user", "{input}")
])

model = ChatOpenAI(model="gpt-4o-mini").with_structured_output(AnalysisResult)
chain = prompt | model

# Data
phonedata="""Month,Nova One,Nova Air,Nova Pro,Nova Max,Nova Ultra
Jan,12500,9800,7200,4500,2100
Feb,13200,10100,7500,4700,2200
Mar,14000,10900,8000,5000,2400
Apr,13800,10700,7900,4900,2350
May,15200,11300,8300,5200,2500
Jun,16000,12000,8700,5500,2650
Jul,15800,11900,8600,5450,2600
Aug,16500,12300,8900,5700,2700
Sep,17200,12800,9200,5900,2800
Oct,18000,13500,9700,6200,3000
Nov,22000,16000,12000,8500,4200
Dec,25000,18500,14000,10000,5000
"""

accessorydata="""
Month,Chargers,Cables,Headphones,Cases,Screen Protectors
Jan,18000,22000,8500,15000,20000
Feb,18500,22500,8700,15300,20500
Mar,19200,23200,9100,15800,21200
Apr,19000,23000,9000,15600,21000
May,20500,24500,9600,16500,22000
Jun,21000,25000,10000,17000,22500
Jul,20800,24800,9900,16800,22300
Aug,21500,25500,10200,17300,23000
Sep,22000,26000,10500,17800,23500
Oct,23000,27000,11000,18500,24500
Nov,28000,32000,14000,22000,30000
Dec,32000,36000,16500,25000,34000
"""

pricingcost="""
Item,Type,Retail Price,Cost
Nova One,Phone,199,120
Nova Air,Phone,299,180
Nova Pro,Phone,449,260
Nova Max,Phone,699,400
Nova Ultra,Phone,899,520
Charger,Accessory,25,10
Cable,Accessory,12,4
Headphones,Accessory,79,35
Case,Accessory,20,6
Screen Protector,Accessory,10,2
"""

combined_data = f"""
Phone Data:
{phonedata}

Accessory Data:
{accessorydata}

Pricing & Cost Data:
{pricingcost}
"""
# Execute
# result = chain.invoke({"input": "Analyze this data..."})

result = chain.invoke({
    "input": f"Analyze this data:\n{combined_data}"
})

print(result)