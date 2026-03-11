def mix_resources(mcp):
    @mcp.prompt("summarize-file")
    def summarize_file_prompt():
        return {
            "name": "summarize-file",
            "description": "Summarize the contents of a file resource.",
            "arguments": [
                {
                    "name": "uri",
                    "type": "string",
                    "description": "The resource URI to summarize."
                }
            ],
            "prompt": """You are given a file at {uri}. Read it and produce a concise summary."""
        }


    @mcp.prompt("analyze-csv")
    def analyze_csv_prompt():
        return {
            "name": "analyze-csv",
            "description": "Analyze a CSV file and extract insights.",
            "arguments": [
                {
                    "name": "uri",
                    "type": "string",
                    "description": "CSV resource URI, e.g. csv/sample"
                }
            ],
            "prompt": """
    You are given a CSV file at {uri}.
    Read the resource and provide:
    1. A schema description
    2. Basic statistics
    3. Interesting patterns or anomalies
    """
        }

