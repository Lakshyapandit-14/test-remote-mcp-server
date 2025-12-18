import random
from fastmcp import FastMCP

mcp = FastMCP(name = "Demo server ") # creating instance of FastMCP

@mcp.tool()
def roll_dice(sides: int = 6) -> int:
    """Roll a dice with a given number of sides."""
    return random.randint(1, sides)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def main():
    print("Hello from expence-tracker-mcp-server!")


if __name__ == "__main__":
    #main()
    #mcp.run()  # running the FastMCP server , this means you set your transport is stdio by default
    mcp.run(transport="http", host="0.0.0.0", port=8000) # this is for remote server using http transport