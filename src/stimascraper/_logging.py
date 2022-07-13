#!/usr/bin/env python
"""This module provides the logging facilities used by the scraper"""
import logging
from pathlib import Path
from sys import stdout

LOG_FILE = "scraper.log"
LOG_FILE_PATH = Path(__file__).parent.parent.parent.absolute().joinpath("logs")
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
HANDLE = "stima_scraper"


def get_stream_handler():
    # Handlers
    scraper_stream_handler = logging.StreamHandler(stdout)
    scraper_stream_handler.setLevel(logging.INFO)
    scraper_stream_handler.setFormatter(FORMATTER)


def get_file_handler():
    scraper_file_handler = logging.FileHandler(
        filename=str(LOG_FILE_PATH) + "/scraper.log", mode="a"
    )
    scraper_file_handler.setLevel(logging.CRITICAL)
    scraper_file_handler.setFormatter(FORMATTER)


def get_logger(handle: str = None):
    # Create custom logger
    LOG_FILE_PATH.mkdir(exist_ok=True)
    scraper_logger = logging.getLogger(handle)
    scraper_logger.addHandler(get_stream_handler())
    scraper_logger.addHandler(get_file_handler())
    return scraper_logger
