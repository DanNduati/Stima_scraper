#!/usr/bin/env python
"""Stimascraper"""

from pathlib import Path
from typing import List

import requests
from bs4 import BeautifulSoup

from stimascraper._logging import get_logger
from stimascraper.utils import gen_filename

from stimascraper.exceptions import (  # isort:skip
    StimaScraperParseError,
    StimaScraperRequestError,
    StimaScraperPdfError,
)

URL = "https://kplc.co.ke/category/view/50/planned-power-interruptions"


class StimaScraper:
    def __init__(self, pdf_path: str, url: str = URL) -> None:
        # self.scraper_logger = logger
        self.url = url
        self.pdf_path = Path(pdf_path)

    def make_request(self, url: str) -> requests.Response:
        """Makes a http request to the interruption url

        Args:
            url (str): interrupt url

        Raises:
            StimaScraperRequestError: Exception on failed http request

        Returns:
            requests.Response: Response object
        """
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise StimaScraperRequestError(e)
        # self.scraper_logger.info(f"Fetching html content of: {url}")
        return response

    def scrape_interruptions(self) -> List[str]:
        """Extracts all interruption pdf document urls from kplc's interruption page

        Raises:
            StimaScraperParseError: Exception raised on element parse error

        Returns:
            List: List of interruption pdf document urls
        """
        interrupt_links = []
        page = self.make_request(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        if not soup:
            raise StimaScraperParseError(
                f"Could not parse html document from url: {self.url}"
            )
        main_element = soup.find(id="content")
        if not main_element:
            raise StimaScraperParseError(
                f"Could not find interruptions main element in url: {self.url}"
            )
        interruption_elements = main_element.find_all("div", class_="blogSumary")
        for interruption_element in interruption_elements:
            interruption_links = interruption_element.find_all("a")
            for interruption_link in interruption_links:
                interrupt_links.append(interruption_link["href"])
        return [link for link in interrupt_links if ".pdf" in link]

    def download_documents(self, urls: List[str], storage_path: Path) -> None:
        """Downloads all the pdf document obtained in the interruption page links

        Args:
            urls (List[str]): List of pdf urls
            storage_path (Path): PDF's strorage path

        Raises:
            StimaScraperPdfError: Exception raised for pdf download/write related errors
        """
        # create pdf directory wonder whether this should be a temporary dir huh!
        try:
            storage_path.mkdir(exist_ok=True)
        except OSError as e:
            raise StimaScraperPdfError(e)
        # download the files to this directory
        for url in urls:
            filename = storage_path.joinpath(gen_filename(url))
            if not filename.is_file():
                # if the pdf file is already there dont redownload
                # self.scraper_logger.info(f"Downloading {filename} from {url}")
                print(f"Downloading {filename} from {url}")
                response = requests.get(url)
                filename.write_bytes(response.content)

    def scrape(self) -> None:
        interruptions = self.scrape_interruptions()
        self.download_documents(interruptions, self.pdf_path)


def main():
    scraper = StimaScraper()
    scraper.scrape()


if __name__ == "__main__":
    main()
