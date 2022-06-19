"""Numerically encode an Element."""
from typing import Union

import numpy as np
from pymatgen.core import Element

from .data.coding_data import get_coding_dict

__all__ = ("encode",)


def encode(element: Union[Element, str, int], property: str) -> Union[float, int, np.ndarray]:
    """Numerically encode an element.

    Args:
        element (Union[Element, str, int]): Input element, e.g. "Fe",  or Element("Fe"),
            or atomic number (Z) as int.
        property (str): Property that was used for encoding, e.g. "mod_pettifor"

    Raises:
        ValueError: If element is not of type `str` or `pymatgen.core.Element`

    Returns:
        Union[float, int, np.ndarray]: Numerical encoding of element.

    Examples:
        >>> encode("Fe", "mod_pettifor")
        70
    """
    if isinstance(element, int):
        element = Element.from_Z(element).symbol
    if isinstance(element, Element):
        element = element.symbol

    if not isinstance(element, str):
        raise ValueError(
            f"`element` must be a string or a `pymatgen` `Element`, not {type(element)}"
        )

    return get_coding_dict(property)[element]
