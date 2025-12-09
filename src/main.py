from scrape_website import scrape_website
from text_extraction_from_html import text_extractoin_from_html
from basik_sentiment_analysis import basik_sentiment_analysis
from sqlite_interactions import putdata_to_databank ,retrieve_data_by_website,fetch_different_websites
from data_visualization import creaet_graphic


websitelink="https://www.tagesschau.de"
scraped_html =scrape_website(websitelink)
extracted_text=text_extractoin_from_html(scraped_html)
sentient_p_n,sentient_value=basik_sentiment_analysis(extracted_text)
putdata_to_databank(websitelink,extracted_text,sentient_p_n,sentient_value)
# fetched_df=retrieve_data_by_website(websitelink)
# my_plt=creaet_graphic(fetched_df)
# my_plt.show()
# x=input("")

import time
time.sleep(10)  