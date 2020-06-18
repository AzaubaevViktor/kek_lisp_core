from .exc import ExecutorKekException
from core import NameSpace, Atom


class Executor:
    def __init__(self, ns: NameSpace):
        self.ns = ns

    def __call__(self, atom: Atom):
        raise NotImplementedError()
