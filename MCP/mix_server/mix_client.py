#!/usr/bin/env python

import asyncio, sys, json
from fastmcp import Client

# Connect to the server service
client = Client("http://localhost:6274/mcp")

# In-memory server (ideal for testing)
# server = FastMCP("TestServer")
# client = Client(server)

# Local Python script
# client = Client("my_mcp_server.py")

async def main():
    async with client:
        # Check week can connect to service
        await client.ping()

        # Get the components from the service
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

        try:
            data=sys.argv[1]
            # Call summarize_parquet_file hardcoded
            parquet_summary = await client.call_tool("summarize_parquet_file", {"filename": "sample.parquet"})
            print(parquet_summary.data)

            try:
                # This example uses the resource to return data, rather than just the resource name
                csv = await client.read_resource("mix-server://csv/sample")
                print(csv)
            except Exception as e:
                print(f"Error reading resource: {e}")

            try:
                # This is how you would use a remote resource in the real world.
                # This is requesting the resources for parquet, which returns the methods
                parquet = await client.read_resource("mix-server://parquet/sample")
                print(parquet[0].text)
            except Exception as e:
                print(f"Error reading resource: {e}")

        except:
            # Show what is available
            print("Tools:", tools)
            print("Resources:", resources)
            print("Prompts:", prompts)

asyncio.run(main())
