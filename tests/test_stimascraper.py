"""Tests for the `stimaparser` package"""
import pytest


def test_scrape_interruptions(test_scraper):
    interruptions = test_scraper.scrape_interruptions()
    print(interruptions)
    assert len(interruptions) > 0
