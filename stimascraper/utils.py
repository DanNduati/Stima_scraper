#!/usr/bin/env python
"""Utilities"""


def gen_filename(s: str) -> str:
    """Generates pdf filename from pdf download url"""
    # Get the name of the pdf from the last slash and replace the % with -
    return s.rsplit("/", 1)[-1].replace("%", "-")
