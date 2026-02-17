from datetime import datetime, UTC

from langchain.tools import tool
from pydantic import BaseModel, Field


@tool
def get_current_datetime() -> str:
    """Returns the current date and time in UTC."""
    return datetime.now(UTC).strftime("%Y.%m.%d %H:%M:%S UTC")


class CalculatorInput(BaseModel):
    expression: str = Field(description="A math expression to evaluate, e.g. '2 + 2 * 3'")


@tool(args_schema=CalculatorInput)
def calculator(expression: str) -> str:
    """Evaluate a math expression."""
    allowed_chars = set("0123456789+-*/.() ")
    print(f"Calc tool: got {expression}")
    if not all(char in allowed_chars for char in expression):
        return "Error: expression contains invalid characters."
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


def web_search(query: str) -> str:
    """Search the web for information. Use when you need up-to-date or factual information."""
    return "[stub] Web search not implemented."
