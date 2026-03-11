#!/usr/bin/env python

from fastmcp import FastMCP

# This is the shared MCP server instance
mcp = FastMCP(name="mix-server")

# Import our tools
import resources
import tools.csv_tools
import tools.parquet_tools
import prompts

resources.mix_resources(mcp)
tools.csv_tools.mix_tool_csv(mcp)
tools.parquet_tools.mix_tool_parquet(mcp)
prompts.mix_resources(mcp)

if __name__ == "__main__":
    mcp.run(transport="http", host='0.0.0.0', port=6274)