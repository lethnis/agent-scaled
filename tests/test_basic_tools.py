from src.tools import get_current_datetime, calculator


def test_calculator():
    result = calculator.invoke({"expression": "2 + 2 * 3"})
    assert result == "8"


def test_datetime_returns_utc():
    result = get_current_datetime.invoke({})
    assert "UTC" in result
