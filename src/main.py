from scrape_website import scrape_website
from text_extraction_from_html import text_extractoin_from_html
from basik_sentiment_analysis import basik_sentiment_analysis
from sqlite_interactions import putdata_to_databank


websitelink="https://www.hslu.ch/de-ch/"

scraped_html =scrape_website(websitelink)
extracted_text=text_extractoin_from_html(scraped_html)
sentient_p_n,sentient_value=basik_sentiment_analysis(extracted_text)
for text, sentient_p_nt, sentient_valuea in zip(extracted_text, sentient_p_n, sentient_value):
    print(text, sentient_p_nt, sentient_valuea )

putdata_to_databank(websitelink,extracted_text,sentient_p_n,sentient_value)

import time
time.sleep(10)  