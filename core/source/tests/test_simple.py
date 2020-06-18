import pytest

from core import SourceStr


def test_name():
    source = SourceStr("123", name="<test>")
    assert source.name == "<test>"

    assert "<test>" in repr(source)


@pytest.mark.parametrize('src', (
    "123",
    "",
    "1010101010",
    "abracadabra babradacarba",
    "(do whatever (you want))"
))
def test_iter(src):
    source = SourceStr(src)

    output = ""
    for ch in source:
        assert len(ch) == 1
        output += ch

    assert output == src
