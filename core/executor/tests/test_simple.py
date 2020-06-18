import pytest

from core import ExecutorKekException


@pytest.mark.parametrize(
    'inp, expected', (
        ('test_int', 456),
        ('test_str', 'this is str'),
        ('(int 1)', 1),
        ("(int -567)", -567),
        ('(+ (int 1) (int 2))', 3),
        ('(quote (a b c))', ('a', 'b', 'c')),
        ("(= x (int 5)) x", 5)
    )
)
def test_constants(ex, inp, expected):
    assert ex(inp) == expected


@pytest.mark.parametrize(
    'inp, expected', (
        ('(int wrong)', None),
        ('(+ test_str (int 5))', None)
    )
)
def test_wrong(ex, inp, expected):
    with pytest.raises(ExecutorKekException):
        ex(inp)
