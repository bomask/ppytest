import pytest


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_passing2():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.skip(reason="no way of currently testing this")
def test_passing3_smoke():
    assert (1, 2, 33) == (1, 2, 13)
