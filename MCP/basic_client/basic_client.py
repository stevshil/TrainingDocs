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

        # Call the add tool
        add_result = await client.call_tool("add", {"a": 2, "b": 3})

        # Read the info resource
        info = await client.read_resource("resource://info")

        # Read the dynamic greeting resource
        greeting = await client.read_resource("greetings://Steve")
        
        try:
            data=sys.argv[1]
            # Print just the data
            print(f"Add result DATA only: {add_result.data}")
            # Show just the text of a "list" object
            print(f"Greeting TEXT only: {greeting[0].text}")
            # Show just the info text, like above
            info_dict=json.loads(info[0].text)
            print(f"Info AUTHOR: {info_dict["author"]}")
        except:
            # Show what is available
            print("Tools:", tools)
            print("Resources:", resources)
            print("Prompts:", prompts)

            print("Add result:", add_result)
            print("Info resource:", info)
            print("Greeting:", greeting)

asyncio.run(main())
