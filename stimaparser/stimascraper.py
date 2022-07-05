#!/usr/bin/env python
"""Stimascraper"""

import logging
from pathlib import Path
from typing import List

import requests
from bs4 import BeautifulSoup
from exceptions import (StimaScraperNoneError, StimaScraperParseError,
                        StimaScraperRequestError)
from utils import gen_filename

URL = "https://kplc.co.ke/category/view/50/planned-power-interruptions"
PDF_FILE_PATH = Path(__file__).parent.parent.absolute().joinpath("pdfs")


class StimaScraper:
    def __init__(self, url=URL) -> None:
        self.url = url

    def make_request(self, url: str):
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise StimaScraperRequestError(e)
        return response

    def scrape_interruptions(self, url: str) -> List[str]:
        interrupt_links = []
        page = self.make_request(url)
        soup = BeautifulSoup(page.content, "html.parser")
        if not soup:
            raise StimaScraperParseError(
                f"Could not parse html document from url: {url}"
            )
        main_element = soup.find(id="content")
        if not main_element:
            raise StimaScraperNoneError(f"Could not find main element in url: {url}")
        interruption_elements = main_element.find_all("div", class_="blogSumary")
        for interruption_element in interruption_elements:
            interruption_links = interruption_element.find_all("a")
            for interruption_link in interruption_links:
                interrupt_links.append(interruption_link["href"])
        return interrupt_links

    def get_pdf_links(self, urls: List[str]) -> List[str]:
        return list(x for x in urls if ".pdf" in x)

    def download_documents(self, urls: List[str]) -> None:
        # create pdf directory wonder whether this should be a temporary dir huh!
        try:
            PDF_FILE_PATH.mkdir(exist_ok=True)
        except OSError as e:
            raise Exception(e)
        # download the files to this directory
        for url in urls:
            filename = PDF_FILE_PATH.joinpath(gen_filename(url))
            if not filename.is_file():
                # if the pdf file is already there dont redownload
                print(f"Downloading {filename} from {url}")
                response = requests.get(url)
                filename.write_bytes(response.content)

    def scrape(self) -> None:
        interruptions = self.scrape_interruptions(self.url)
        pdf_url_list = self.get_pdf_links(interruptions)
        self.download_documents(pdf_url_list)


def main():
    scraper = StimaScraper()
    scraper.scrape()


if __name__ == "__main__":
    main()
