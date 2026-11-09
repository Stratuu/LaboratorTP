import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)

from collections import Counter
from arsenal.aparare.detector import suspecti
def test_pragul_taie():
    c = Counter({"a": 13, "b": 2})
    assert suspecti(c, 10) == [("a", 13)]


def test_prag_invalid():
    import pytest

    with pytest.raises(ValueError):
        suspecti({}, 0)