def creaet_graphic(dataframe):
    import streamlit as st
    st.write("--- create_graphic ---")
    sentiment=dataframe["sentiment_p_n"].value_counts().sort_index()
    sentiment_dict = sentiment.to_dict()
    print(sentiment_dict)
    import pandas as pd
    import matplotlib.pyplot as plt
    sentiment_series = pd.Series(sentiment_dict, name='count')
    sentiment_series.index.name = 'sentiment_p_n'
    fig, ax = plt.subplots()
    ax.bar(sentiment_series.index, sentiment_series.values, color=['grey', 'green','#FF2400'])
    ax.set_xlabel(sentiment_series.index.name)
    ax.set_ylabel(sentiment_series.name)
    ax.set_title('Sentiment Count Distribution')
    for i, v in enumerate(sentiment_series.values):
        ax.text(i, v + 0.5, str(v), ha='center', va='bottom')
    plt.xticks(rotation=0)
    # plt.savefig('sentiment_bar_chart.png')
    return fig