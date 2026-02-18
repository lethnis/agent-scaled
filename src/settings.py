from typing import Literal
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MCPServerConfig(BaseModel):
    transport: Literal["stdio", "http"] = "stdio"

    # stdio
    command: str | None = None
    args: list[str] = Field(default_factory=lambda: [])
    env: dict[str, str] | None = None

    # http
    url: str | None = None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    openai_api_key: str
    openai_base_url: str
    openai_model_name: str

    max_iterations: int = 5

    mcp_enabled: bool = True

    def get_mcp_servers(self) -> dict[str, MCPServerConfig]:

        servers: dict[str, MCPServerConfig] = {}

        if self.mcp_enabled:
            servers["tools-server"] = MCPServerConfig(
                transport="http",
                url="http://127.0.0.1:8001/mcp",
            )

        return servers


settings = Settings()
