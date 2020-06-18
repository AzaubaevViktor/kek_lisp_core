import pytest


@pytest.mark.parametrize(
    'inp, expected', (
        ('test_int', 456),
        ('test_str', 'this is str'),
        ('(int 1)', 1),
        ("(int -567)", -567),
        ('(+ (int 1) (int 2))', 3),
        ('(quote (a b c))', ('a', 'b', 'c'))
    )
)
def test_constants(ex, inp, expected):
    assert ex(inp) == expected
