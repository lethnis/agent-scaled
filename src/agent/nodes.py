from langchain.messages import SystemMessage
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI

from src.agent.state import AgentState
from src.prompts.system import SYSTEM_PROMPT
from src.settings import settings
from src.tools import ALL_TOOLS


def make_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model=settings.openai_model_name,
        base_url=settings.openai_base_url,
        api_key=settings.openai_api_key,
    )


llm_with_tools = make_llm().bind_tools(ALL_TOOLS)


async def assistant_node(state: AgentState, config: RunnableConfig) -> dict:
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = await llm_with_tools.ainvoke(messages, config=config)
    return {"messages": [response]}
