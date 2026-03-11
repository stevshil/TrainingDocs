#!/usr/bin/env python

from fastmcp import FastMCP
import json

mcp = FastMCP(name="Basic Server")

@mcp.tool
async def add(a: int, b: int) -> int:
  """Add 2 numbers"""
  return a + b

@mcp.resource("resource://info")
async def get_info():
  """Provides application information"""
  return json.dumps({"version": 1.0, "author": "Steve Shilling"})

@mcp.resource("greetings://{name}")
def personalized_greeting(name: str) -> str:
    """Generates a personalized greeting for the given name."""
    return f"Hello, {name}! Welcome to the MCP server."

if __name__ == "__main__":
    mcp.run(transport="http", host='0.0.0.0', port=6274)