from typing import Callable, Any

from core import NameSpace, SourceStr, Lexer, Executor


def ex() -> Callable[[str], Any]:
    # TODO: Create methods
    # TODO: Add test stack (append lemma + value, return list of)

    ns = NameSpace({
        'test_int': 456,
        'test_str': 'this is str',
        'quote': None,
        'int': None,
        '+': None,
        '=': None,
    })

    executor = Executor(ns)

    def do_exec(raw: str):
        source = SourceStr(raw, name='test_executor')

        lexer = Lexer(source)

        atom = lexer()

        return executor(atom)

    return do_exec

