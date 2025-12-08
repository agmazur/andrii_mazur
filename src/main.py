from scrape_website import scrape_website
from text_extraction_from_html import text_extractoin_from_html






scraped =scrape_website("https://www.hslu.ch/de-ch/")
extracted_text=text_extractoin_from_html(scraped)
for element in extracted_text:
    print(f"{element}+")


import time
time.sleep(10)