from pythonisms import Pythonisms
import pytest
from pythonisms import Pythonisms


def test_len():
    pun = ["I'm a big fan of whiteboards...", "I find them quite re-markable "]
    assert len(pun) == 2


def test_iter():
    pun = ["I'm a big fan of whiteboards...", "I find them quite re-markable "]
    iterator = iter(pun)
    assert next(iterator) == "I'm a big fan of whiteboards..."
    assert next(iterator) == "I find them quite re-markable "


def test_get_item():
    p = Pythonisms([1, 2, 3])
    assert p[0] == 1
    assert p[1] == 2
    assert p[2] == 3

def test_set_item():
    p = Pythonisms([1, 2, 3])
    p[2] = 4
    assert p[2] == 4
    assert p.data == [1, 2, 4]
