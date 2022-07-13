from pathlib import Path
from stimascraper.scraper import StimaScraper

# Create a "pdfs/" directory here
PDF_FILE_PATH = Path(__file__).parent.joinpath("pdfs")


def main():
    scraper = StimaScraper(pdf_path=PDF_FILE_PATH)
    scraper.scrape()


if __name__ == "__main__":
    main()
