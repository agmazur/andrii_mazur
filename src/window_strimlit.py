from scrape_website import scrape_website
from text_extraction_from_html import text_extractoin_from_html
from basik_sentiment_analysis import basik_sentiment_analysis
from sqlite_interactions import putdata_to_databank ,retrieve_data_by_website,fetch_different_websites
from data_visualization import creaet_graphic
from regex_cleaning import clean_array_strings

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

def streamlit_window():






    st.title("Interactive Matplotlib Plotter")
    st.markdown("Use the input box below to set the frequency of the sine wave, then click the button to plot it.")

 
    websitelink = st.text_input(
        label="Enter Sine Wave Frequency (Number of Cycles):",
        placeholder="example/somesite.com" 
    )


    if st.button("make symatic analysis"):
        scraped_html =scrape_website(websitelink)
        extracted_text=text_extractoin_from_html(scraped_html)
        better_text=clean_array_strings(extracted_text)
        sentient_p_n,sentient_value=basik_sentiment_analysis(better_text)
        putdata_to_databank(websitelink,better_text,sentient_p_n,sentient_value)
        fetched_df=retrieve_data_by_website(websitelink)
        my_plt=creaet_graphic(fetched_df)

      
        st.pyplot(my_plt)

        # Optional: Display the data used for the plot

        time.sleep(10)
    # --- End of script ---
streamlit_window()