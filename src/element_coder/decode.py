"""Decode an elemental encoding."""
from typing import Callable, Union

import numpy as np
from loguru import logger
from scipy.spatial.distance import cdist

from .data.coding_data import get_coding_dict


def decode(
    encoding: Union[int, float, np.ndarray, list, tuple],
    property: str,
    metric: Union[str, Callable] = "euclidean",
) -> str:
    """Decode an elemental encoding.

    Args:
        encoding (Union[int, float, np.ndarray]): Numerical encoding of an element
        property (str): Property that was used for encoding, e.g. "mod_pettifor"
        metric (Union[str, callable] optional): Metric to measure distance between (noisy) input encoding
            and tabulated encodings.
            If a string, the distance function can be 'braycurtis', 'canberra', 'chebyshev',
            'cityblock', 'correlation', 'cosine', 'dice', 'euclidean', 'hamming', 'jaccard',
            'jensenshannon', 'kulsinski', 'kulczynski1', 'mahalanobis', 'matching', 'minkowski',
            'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath',
            'sqeuclidean', 'yule'. Defaults to "euclidean".

    Returns:
        str: Element symbol

    Examples:
        >>> decode(80, "mod_pettifor")
        'Tl'
    """
    if isinstance(encoding, (int, float)):
        encoding = np.array([encoding])
    elif isinstance(encoding, (list, tuple)):
        encoding = np.array(encoding)

    coding_dict = get_coding_dict(property)
    coding_data = coding_dict[:]
    coding_shape = coding_data.shape
    if len(coding_shape) == 1:
        coding_data = coding_data.reshape(-1, 1)

    distance = cdist(coding_data, encoding.reshape(1, -1), metric=metric)
    matching_index = distance.argmin()
    logger.debug(
        f"Matching distance: {distance[matching_index]}, mean distance: {distance.mean()}, std: {distance.std()}"
    )
    return coding_dict.keys()[matching_index]
