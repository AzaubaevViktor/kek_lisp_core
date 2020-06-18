from core import NameSpace


def test_set_get():
    ns = NameSpace()

    ns['test'] = 1

    assert ns['test'] == 1


def test_init():
    ns = NameSpace({'a': 1, 'b': 2, 'c': 3})

    assert ns['a'] == 1
    assert ns['b'] == 2
    assert ns['c'] == 3

    ns['b'] = 4
    assert ns['b'] == 4


def test_contains():
    orig_ = {'aa': 1, 'bccc': 2, 'cffff': 3}
    ns = NameSpace(orig_)

    for key in orig_.keys():
        assert key in orig_

    for wrong_key in ('xxx', 'ttt', '', 3):
        assert wrong_key not in orig_, 'Use another key'
        assert wrong_key not in ns
