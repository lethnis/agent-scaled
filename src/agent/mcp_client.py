from langchain.tools import BaseTool
from langchain_mcp_adapters.client import MultiServerMCPClient

from src.settings import settings


def _build_client_config() -> dict:
    """Преобразует MCPServerConfig из `settings` в формат для MultiServerMCPClient."""
    config = {}
    for name, server in settings.get_mcp_servers().items():
        config[name] = {"transport": server.transport}

        if server.transport == "stdio":
            config[name]["command"] = server.command
            config[name]["args"] = server.args
            if server.env is not None:
                config[name]["env"] = server.env

        elif server.transport == "http":
            config[name]["url"] = server.url

    return config


async def get_mcp_tools() -> list[BaseTool]:
    """Поднимает mcp-клиенты, возвращает список LangChain tools,
    при выходе закрывает соединения."""

    config = _build_client_config()

    if not config:
        return []

    client = MultiServerMCPClient(config)
    return await client.get_tools()
