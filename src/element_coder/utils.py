"""Utilities for `element_coder`."""
from typing import Iterable, Union

from pymatgen.core import Element

from .encode import encode


def get_range(elements: Iterable[Union[str, Element, int]], property: str = "Z"):
    """Get the range of a property for a list of elements.

    Args:
        elements (Iterable[Union[str, Element, int]]): List of elements.
        property (str): Property that was used for encoding, e.g. "mod_pettifor"

    Returns:
        Tuple[float, int, np.ndarray]: Numerical encoding of element.

    Examples:
        >>> get_range(["Fe", "Tl", "Pb", "U", "Zn"], "mod_pettifor")
        (70, 74)
    """
    encodings = [encode(element, property) for element in elements]
    return min(encodings), max(encodings)
