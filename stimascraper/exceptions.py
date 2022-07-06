#!/usr/bin/env python
"""Custom exceptions"""
from _logging import get_logger

logger = get_logger()


class StimaError(Exception):
    """Base class for all stima exceptions"""

    def __init__(self, message) -> None:
        self.message = message
        logger.critical("Exception raised")

    def __str__(self) -> str:
        return f"Stima failed with {self.message!r}"


class StimaScraperRequestError(StimaError):
    """Exceprtion raised when it is not possible to make a request"""

    pass


class StimaScraperParseError(StimaError):
    """Exception raised when there is an error in parsing elements"""

    pass


class StimaScraperNoneError(StimaError):
    """Exception raised when the scraper can’t find a tag that you know is in the document"""

    pass


class StimaScraperPdfError(StimaError):
    """Exception raised on pdf related errors"""

    pass
