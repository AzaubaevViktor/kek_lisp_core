import pytest

from core import Atom, SourceStr, Lexer
from core import LexerKekException


checks = (
    ("", None),
    ("(a b c)", ('a', 'b', 'c')),
    ("( a b c)", ('a', 'b', 'c')),
    ("(a b c )", ('a', 'b', 'c')),
    ("(a b    c)", ('a', 'b', 'c')),
    ("(    a     b       c   )", ('a', 'b', 'c')),
    ("(a \nb    \n c\n\n\n\n)\n", ('a', 'b', 'c')),
    ("(a (b c))", ('a', ('b', 'c'))),
    ("((a b) (c d (e f)))", (('a', 'b'), ('c', 'd', ('e', 'f')))),
    ("(abcdef abcdef)", ("abcdef", "abcdef")),
    ("(quotes here \" \')", ('quotes', 'here', '"', "'")),
    ("a", "a"),
    ('abcde', 'abcde'),
    ('(a)', ('a', )),
    ('(a b c d)', ('a', 'b', 'c', 'd')),
    ('(x y (z w))', ('x', 'y', ('z', 'w'))),
    ('(x a(ii mm(a b)x)b)', ('x', 'a', ('ii', 'mm', ('a', 'b'), 'x'), 'b')),
    ('   (\ta\t\t\t  \n  b c \n\n\nd\t\t)', ('a', 'b', 'c', 'd'))
)


@pytest.mark.parametrize('raw, expected', checks)
def test_parse_good(raw: str, expected: Atom):
    source = SourceStr(raw, name='<test>')
    lexer = Lexer(source)

    result = lexer()

    raise NotImplementedError()
    assert result == expected


@pytest.mark.parametrize(
    'raw, expected',
    (
            ('(a', None),
            ('(a (b', None),
            ('(x ))', None),
            (')', None),
    )
)
def test_parse_wrong(raw, expected):
    source = SourceStr(raw, name='<test>')
    lexer = Lexer(source)

    with pytest.raises(LexerKekException):
        lexer()

    raise NotImplementedError()
