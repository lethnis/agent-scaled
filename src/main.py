import asyncio

from langchain.messages import HumanMessage

from src.agent.graph import create_agent


async def main():
    agent = create_agent()

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
