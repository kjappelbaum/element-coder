from element_coder.utils import get_range
from pymatgen.core import Element


def test_get_range():
    minimum, maximum = get_range(["H", "He", "Li"], property="atomic")
    assert minimum == 0
    assert maximum == 2

    minimum, maximum = get_range([1, Element("He"), "Li"], property="atomic")
    assert minimum == 0
    assert maximum == 2
