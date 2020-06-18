import pytest

from core import NameSpace


def test_parent():
    parent = NameSpace({'a': 1})

    child = NameSpace({'b': 2}, parent=parent)

    assert child['a'] == 1
    assert child['b'] == 2

    child['a'] = 3
    assert child['a'] == 3
    assert parent['a'] == 1

    child['c'] = 4
    assert child['c'] == 4
    assert 'c' not in parent


@pytest.mark.parametrize('count', (10, ))
@pytest.mark.parametrize(
    'creator',
    (
        lambda d, ns: NameSpace(d, parent=ns),
        lambda d, ns: ns.child(d)
    ))
def test_deep(count, creator):
    assert count > 2

    ns = root = NameSpace({'0': 0})

    for i in range(1, count):
        ns = creator({str(i): i}, ns)

    for i in range(count):
        assert str(i) in ns
        assert ns[str(i)] == i

    ns['x'] = -1

    assert ns['x'] == -1
    assert 'x' not in ns
