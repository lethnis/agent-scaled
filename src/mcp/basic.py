from fastmcp import FastMCP

mcp = FastMCP(
    name="tools-server",
    instructions="Server providing weather tool.",
)


# TODO make async and use real API
@mcp.tool
def get_weather(city: str) -> str:
    """Get current weather for a given city name."""
    weather = {
        "moscow": "Moscow: -5C, snow",
        "tokyo": "Tokyo, 18C, sunny",
    }
    return weather.get(city.lower(), f"{city}: 20C, good day to swim [stub]")


if __name__ == "__main__":
    mcp.run(transport="stdio", show_banner=False)
