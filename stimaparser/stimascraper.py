"""Stimascraper"""

from pathlib import Path
from typing import List

import requests
from bs4 import BeautifulSoup

URL = "https://kplc.co.ke/category/view/50/planned-power-interruptions"
PDF_FILE_PATH = Path(__file__).parent.parent.absolute().joinpath("pdfs")


def make_request(url: str):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    return response


def scrape_interruptions(url: str) -> List[str]:
    interrupt_links = []
    page = make_request(url)
    soup = BeautifulSoup(page.content, "html.parser")
    main_element = soup.find(id="content")
    interruption_elements = main_element.find_all("div", class_="blogSumary")
    for interruption_element in interruption_elements:
        interruption_links = interruption_element.find_all("a")
        for interruption_link in interruption_links:
            interrupt_links.append(interruption_link["href"])
    return interrupt_links


def get_pdf_links(urls: List[str]):
    return list(x for x in urls if ".pdf" in x)


def download_documents(urls: List[str]):
    # create pdf directory wonder whether this should be a temporary dir huh!
    try:
        PDF_FILE_PATH.mkdir(exist_ok=True)
    except OSError as e:
        raise Exception(e)
    # download the files to this directory
    for url in urls:
        filename = PDF_FILE_PATH.joinpath(
            str(url).rsplit("/", 1)[-1].replace("%", "-")
        )  # Get the name of the pdf from the last slash and replace the % with -
        if not filename.is_file():
            # if the pdf file is already there dont redownload
            print(f"Downloading {filename} from {url}")
            response = requests.get(url)
            filename.write_bytes(response.content)

def main():
    interruptions = scrape_interruptions(URL)
    pdf_url_list = get_pdf_links(interruptions)
    download_documents(pdf_url_list)

if __name__ == "__main__":
    main()
