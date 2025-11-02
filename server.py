import os
from mcp.server.fastmcp import FastMCP

# Initialize your MCP server
mcp = FastMCP("keyword-search-server")


@mcp.tool()
def search_file_for_keyword(keyword: str, filename: str) -> str:
    """
    Searches a text file for a specific keyword and returns all matching lines.
    """
    if not os.path.exists(filename):
        return f"Error: The file '{filename}' was not found. Make sure you are in the correct directory."

    try:
        matching_lines = []
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f):
                if keyword.lower() in line.lower():
                    matching_lines.append(f"Line {i+1}: {line.strip()}")

        if not matching_lines:
            return f"No matches found for '{keyword}' in '{filename}'."

        result = "\n".join(matching_lines)
        return f"Found {len(matching_lines)} match(es):\n{result}"

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Run the server
if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run()
