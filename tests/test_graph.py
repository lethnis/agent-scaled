import pytest
from langchain.messages import HumanMessage


@pytest.mark.asyncio
async def test_agent_responds(agent):
    result = await agent.ainvoke({"messages": [HumanMessage(content="What is 12 * 12?")]})
    last = result["messages"][-1]
    assert "144" in last.content
