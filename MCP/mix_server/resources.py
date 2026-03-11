import os, mimetypes, json

def get_file_info(path: str):
    size = os.path.getsize(path)  # size in bytes
    mime, _ = mimetypes.guess_type(path)  # e.g. "text/csv"

    return {
        "size_bytes": size,
        "mime_type": mime or "unknown"
    }


def mix_resources(mcp):
  # This resource returns the content of the file
  @mcp.resource("csv/{filename}")
  async def csv_resource(filename: str):
    """"Get csv data"""
    with open(f"data/{filename}.csv") as fh: 
      text = fh.read() # single string
      return text

  # The resource does not return the data as parquet is special
  # Instead we return file attributes
  @mcp.resource("parquet/{filename}")
  async def parquet_resource(filename: str):
    """"Get parquet file attributes"""
    data = get_file_info(f"data/{filename}.parquet")
    return json.dumps(data)
  
  # Static resources must be uri
  @mcp.resource("mix-server://parquet/sample.parquet")
  async def parquet_resource_info():
    """
    Simple place holder for the parquet resource

    Call: mix-server://parquet/{filename}
    
    Arguments: filename

    Returns: Size and file type
    """
    return "To use this call parquet/\{filename\}"