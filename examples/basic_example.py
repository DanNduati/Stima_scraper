from pathlib import Path

from stimascraper.scraper import StimaScraper

# A "pdfs/" directory in the current working directory
PDF_FILE_PATH = str(Path.cwd().joinpath("pdfs"))

# You can specify your own pdf directory as well:
# PDF_FILE_PATH = "/home/daniel/Desktop/pdfs"


def main():
    scraper = StimaScraper(pdf_path=PDF_FILE_PATH)
    scraper.scrape()


if __name__ == "__main__":
    main()
