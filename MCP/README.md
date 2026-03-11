# Model Context Protocol

No, not Master Control Program, or a saying for not very pleasent males.

Model Context Protocol, the API for enabling desktop automation using Agentic AI to interact with your computer through using prompts to perform tasks.

## Important Notes

When working with MCP it is important to realise that your **resource** naming conventions and service name should match the DNS standard for naming;
- letters and numbers
- full stop/period (.)
- minus (-) symbol, **not** underscore (_)

### MCP

3 types of content available;
- Tools = actions to be performed, just like in an API there will be functions that could retrieve data, or send an Email, query database, etc.
- Resources = data to be read, e.g. a text file, config file, JSON document, directory listing, etc.  Generally static attribute to be listed in the resources
  > NOTE: dynamic resource do **not** get listed
- prompts = helps the LLM reason, write or behave, e.g. summarize a document, explain code, act as a ..., etc

## Basic Server

This is a very simplistic, client/server example of using MCP, showing how you can use FastMCP in Python to create both sides of the service.

## Mix Server

Adapted from https://medium.com/data-engineering-with-dremio/building-a-basic-mcp-server-with-python-4c34c41031ed with it's own client rather than integrating with Claude as the example does.