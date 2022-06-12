from typing import Iterable
from element_coder import encode, decode
import numpy as np
import pytest

np.random.seed(0)


@pytest.mark.parametrize("element", ["Fe", "Tl", "Pb", "U", "Zn"])
@pytest.mark.parametrize("property", ["mod_pettifor", "pettifor", "mat2vec"])
def test_encode(element, property):
    encoding = encode(element, property)
    decoded = decode(encoding, property)
    assert decoded == element


@pytest.mark.parametrize("element", ["Fe", "Tl", "Pb", "U", "Zn"])
@pytest.mark.parametrize("property", ["mod_pettifor", "pettifor", "mat2vec"])
def test_encode_noisy(element, property):
    encoding = encode(element, property)
    if isinstance(encoding, Iterable):
        encoding = np.array(encoding)
        length = encoding.shape[0]
        encoding += np.random.normal(0, 0.1, length)
    else:
        encoding += np.random.normal(0, 0.1)

    decoded = decode(encoding, property)
    assert decoded == element
