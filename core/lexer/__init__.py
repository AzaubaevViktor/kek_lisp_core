from core import BaseSource, Atom
from .exc import LexerKekException


class Lexer:
    def __init__(self, source: BaseSource):
        self.source = source

    def __call__(self) -> Atom:
        raise NotImplementedError()
