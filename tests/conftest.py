import tempfile
from pathlib import Path

import pytest

from examples.basic_example import PDF_FILE_PATH
from stimascraper.scraper import StimaScraper


# Define a scraper fixture
@pytest.fixture(scope="module")
def test_scraper():
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_dir = Path(tmpdirname)
        scraper = StimaScraper(pdf_path=temp_dir)
        yield scraper
