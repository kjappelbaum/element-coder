# -*- coding: utf-8 -*-

"""Encode chemical elements numerically and decode numerical representations of elements."""
from .decode import decode, decode_many
from .encode import encode, encode_many

__all__ = ("encode", "encode_many", "decode", "decode_many")
