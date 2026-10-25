import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

MCP_URL = "https://mcp.kite.trade/mcp"


async def loginKite():
    async with streamable_http_client(MCP_URL) as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(
            read_stream,
            write_stream,
        ) as session:

            await session.initialize()

                        # response = await session.list_tools()
            # tools = [
            #     {
            #         "name": tool.name,
            #         "description": tool.description,
            #         "input_schema": tool.input_schema,
            #     }
            #     for tool in response.tools
            # ]
            # for tool in tools:
            #     print(f"\nName: {tool['name']}")
            #     print(f"Description: {tool['description']}")
            #     print(f"Arguments: {tool['input_schema']}")
            # result = await session.call_tool(
            #     "search_instruments",
            #     arguments={
            #         "query": "NSE:KOTAKBANK",
            #         "filter_on": "*",
            #         "from": 0,
            #         "limit": 10,
            #     },
            # )
            # for content in result.content:
            #     if content.type == "text":
            #         print(content.text)
            #     if result.is_error:
            #         print("Tool execution failed!")
            
            # result2 = await session.call_tool(
            #     "get_quotes",
            #     arguments={
            #         "instruments":["NSE:KOTAKBANK"]
            #     }
            # )
            # for content in result2.content:
            #     if content.type == "text":
            #         print(content.text)
            #     if result2.is_error:
            #         print("Tool execution failed!")

            # 1. Call the login tool to generate the authorization link
            login_result = await session.call_tool(
                "login",
                arguments={},
            )

            for content in login_result.content:
                if content.type == "text":
                    print(content.text)

            # 2. KEEP SESSION ALIVE:
            # We pause here so the HTTP connection to mcp.kite.trade remains active
            # while you open the URL and authenticate in the browser.
            print("\n" + "=" * 60)
            await asyncio.to_thread(
                input,
                "👉 Click the login link above in your browser and authorize.\n"
                "👉 AFTER logging in, return here and press [Enter] to continue: ",
            )
            print("=" * 60 + "\n")

            # 3. Test calling a tool now that the session is authenticated
            print("🔍 Testing authenticated call: search_instruments for NSE:KOTAKBANK...")
            result = await session.call_tool(
                "search_instruments",
                arguments={
                    "query": "NSE:KOTAKBANK",
                    "filter_on": "*",
                    "from": 0,
                    "limit": 5,
                },
            )

            for content in result.content:
                if content.type == "text":
                    print(content.text)
            if result.is_error:
                print("⚠️ Tool execution failed!")


if __name__ == "__main__":
    asyncio.run(loginKite())