import asyncio

from langchain.messages import HumanMessage

from src.agent.graph import create_agent
from src.agent.mcp_client import get_mcp_tools


async def main():

    mcp_tools = await get_mcp_tools()

    if mcp_tools:
        print(f"MCP tools loaded: {[t.name for t in mcp_tools]}")

    agent = create_agent(extra_tools=mcp_tools)

    print("Agent ready. Type 'quit' to exit.\n")
    while True:
        user_input = input("Your input: ").strip()
        if user_input.lower() in {"quit", "exit", "q"}:
            break

        result = await agent.ainvoke({"messages": [HumanMessage(content=user_input)]})

        ai_message = result["messages"][-1]
        print(f"Agent: {ai_message.content}\n")


if __name__ == "__main__":
    asyncio.run(main())
