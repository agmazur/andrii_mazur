
def basik_sentiment_analysis(word_array):
    import torch
    from transformers import pipeline
    sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest")   
    sentimentreslut_p_n=[]
    sentimentreslut_value=[]
    for word in word_array:
        sentiment_result=sentiment_pipeline(word)
        sentimentreslut_p_n.append(sentiment_result[0]["label"])
        sentimentreslut_value.append(sentiment_result[0]["score"])
    print(sentimentreslut_p_n,sentimentreslut_value)
    return sentimentreslut_p_n,sentimentreslut_value