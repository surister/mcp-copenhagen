from mcp.server.fastmcp import FastMCP
from mountains import get_mountain

# Create an MCP server
mcp = FastMCP("copenhagen-mountains")


# Add an addition tool
@mcp.tool()
def get_mountains_by_country(country: str) -> list[dict]:
    """Given a country, returns a list of the top highest mountains of that country."""
    return get_mountain(country.lower())
