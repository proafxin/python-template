import pytest

from pytemplate.something import hello


@pytest.mark.asyncio
async def test_hello() -> None:
    res = hello()

    assert isinstance(res, str)
    assert "hello" in res.lower()
    assert "world" in res.lower()
