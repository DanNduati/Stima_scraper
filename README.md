<h1 align="center"><b>Stima Scraper</b></h1>

[![Project Status: WIP – Initial development is in progress.](https://www.repostatus.org/badges/latest/wip.svg)](https://github.com/DanNduati/Jokes_api)

## <b>Description</b>


Stima scraper extracts and pulls scheduled power interruptions pdf data off KPLC's [website](https://kplc.co.ke/category/view/50/planned-power-interruptions).

## <b>Prerequisites</b>
- Python3

## <b>Installation</b>
```bash
$ pip install stima-scraper
```

## <b>Usage</b>
```python
from pathlib import Path
from stimascraper.scraper import StimaScraper

# PDF storage directory you can define your own path here
PDF_FILE_PATH = Path(__file__).parent.joinpath("pdfs")


def main():
    scraper = StimaScraper(pdf_path=PDF_FILE_PATH)
    scraper.scrape()


if __name__ == "__main__":
    main()


```
## <b>Demo</b>
[![asciicast](https://asciinema.org/a/Wvq14B2GsrknPqCLUaRIvLS1F.svg)](https://asciinema.org/a/Wvq14B2GsrknPqCLUaRIvLS1F)

## <b>Built with</b>
- [Beautifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/)


## <b>License and Copyright</b>
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)

Copyright 2022 Daniel Chege Nduati