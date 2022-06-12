"""We represent each possible elemental encoding as a `sciris` dict. This allows for more convenient bi-directional lookup.
"""

import os
from difflib import get_close_matches
from functools import lru_cache

import sciris as sc
from loguru import logger

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_CODING_DATA_DIR = os.path.join(_THIS_DIR, "raw")

CODING_FILES = {
    "mod_pettifor": "mod_petti.json",
    "element_net": "elemnet.json",
    "matscholar": "matscholar.json",
    "pettifor": "petti.json",
    "atomic_number": "atomic.json",
    "cgcnn": "cgcnn.json",
    "jarvis_sc": "jarvis_sc.json",
    "jarvis": "jarvis.json",
    "magpie_sc": "magpie_sc.json",
    "magpie": "magpie.json",
    "mat2vec": "mat2vec.json",
    "megnet16": "megnet16.json",
    "mendeleev": "mendeleev.json",
    "oliynk_sc": "olink_sc.json",
    "oliynk": "olink.json",
}


_PROPERTY_KEYS = set(list(CODING_FILES.keys()))

__all__ = ("get_coding_dict",)


def _load_coding_data(property_key: str) -> sc.odict:
    """Load the coding data for a given property key."""
    file = os.path.join(_CODING_DATA_DIR, CODING_FILES[property_key])
    return sc.odict(sc.loadjson(file))


@lru_cache()
def get_coding_dict(key: str) -> dict:
    """Get the coding dict for the given key.
    If no exact match is found, it performs a fuzzy search to find a close match.

    Args:
        key (str): property name

    Returns:
        dict: property dictionary
    """
    key = key.lower()
    if not key in _PROPERTY_KEYS:
        key = get_close_matches(key, _PROPERTY_KEYS, n=1)[0]
        logger.warning(f"No matching key found for {key}. Falling back to closest match {key}.")
        return _load_coding_data(key)
    return _load_coding_data(key)
