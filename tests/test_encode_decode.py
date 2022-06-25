"""Testing that the encoded input can be decoded into the input."""
from typing import Iterable

import numpy as np
import pytest

from element_coder import decode, decode_many, encode, encode_many
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


def test_encode_many():
    """Make sure that the encode_many() method works as exepected, also with mixed types."""
    encoding_a = encode_many(["H", "Li"], "mod_pettifor")
    assert encoding_a[0] == 102
    assert encoding_a[1] == 11

    encoding_b = encode_many([1, "Li"], "mod_pettifor")
    assert encoding_b[0] == 102
    assert encoding_b[1] == 11

    encoding_c = encode_many([1, 3], "mod_pettifor")
    assert encoding_c[0] == 102
    assert encoding_c[1] == 11


def test_decode_many():
    """Make sure the decoding works as exepected."""
    assert all(decode_many([80, 90], "mod_pettifor") == np.array(["Tl", "Sb"]))

    assert all(
        decode_many(
            [
                [
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                ],
                [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    1,
                    0,
                    0,
                    0,
                ],
            ],
            "cgcnn",
        )
        == np.array(["H", "He"])
    )
