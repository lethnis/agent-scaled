import pytest

from src.agent.graph import create_agent


@pytest.fixture
def agent():
    return create_agent()
