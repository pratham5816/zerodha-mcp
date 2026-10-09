import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

MCP_URL = "https://mcp.kite.trade/mcp"


async def main():
    async with streamable_http_client(MCP_URL) as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(
            read_stream,
            write_stream,
        ) as session:

            # Initialize the MCP session
            await session.initialize()

            # Discover tools
            response = await session.list_tools()

            # Convert tools into Python dictionaries
            tools = [
                {
                    "name": tool.name,
                    "description": tool.description,
                    "input_schema": tool.input_schema,
                }
                for tool in response.tools
            ]

            # Print each tool
            for tool in tools:
                print(f"\nName: {tool['name']}")
                print(f"Description: {tool['description']}")
                print(f"Arguments: {tool['input_schema']}")


asyncio.run(main())