"""Testing the utils module."""
from pymatgen.core import Element

from element_coder.utils import get_range


def test_get_range():
    """Esnure that we get the correct range."""
    minimum, maximum = get_range(["H", "He", "Li"], property="atomic")
    assert minimum == 0
    assert maximum == 2

    minimum, maximum = get_range([1, Element("He"), "Li"], property="atomic")
    assert minimum == 0
    assert maximum == 2
