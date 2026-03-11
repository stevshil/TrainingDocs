from utils.file_reader import read_csv_summary

async def get_csv_summary(filename: str) -> str:
    return read_csv_summary(filename)

def mix_tool_csv(mcp):
    @mcp.tool
    async def summarize_csv_file(filename: str) -> str:
        """
        Summarize a CSV file by reporting its number of rows and columns.
        Args:
            filename: Name of the CSV file in the /data directory (e.g., 'sample.csv')
        Returns:
            A string describing the file's dimensions.
        """
        return get_csv_summary(filename)