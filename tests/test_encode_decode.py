"""Testing that the encoded input can be decoded into the input."""
from typing import Iterable

import numpy as np
import pytest

from element_coder import decode, encode
from element_coder.data.coding_data import _PROPERTY_KEYS

np.random.seed(0)


@pytest.mark.parametrize("element", ["Ti"])
@pytest.mark.parametrize("property", _PROPERTY_KEYS)
def test_encode(element, property):
    """Make sure that we get the input back after we apply decode on encoded input."""
    if property not in ["critical_temperature", "reflectivity", "refractive_index"]:
        encoding = encode(element, property)
        decoded = decode(encoding, property)
        assert decoded == element


@pytest.mark.parametrize("element", ["Fe", "Tl", "Pb", "U", "Zn"])
@pytest.mark.parametrize("property", ["mod_pettifor", "pettifor", "mat2vec"])
def test_encode_noisy(element, property):
    """Make sure that the lookup also works with a bit of noise."""
    encoding = encode(element, property)
    if isinstance(encoding, Iterable):
        encoding = np.array(encoding)
        length = encoding.shape[0]
        encoding += np.random.normal(0, 0.1, length)
    else:
        encoding += np.random.normal(0, 0.1)

    decoded = decode(encoding, property)
    assert decoded == element
