import pytest

import greeters


class TestGreeters:
    def test_say_hello_says_hello(self) -> None:
        assert greeters.say_hello() == "Hello from pyproject-test!"

    @pytest.mark.parametrize("name", ["Peter", "Max"])
    def test_say_personalized_hello_says_hello(self, name: str) -> None:
        assert greeters.say_personalized_hello(name) == f"Hello {name}"
