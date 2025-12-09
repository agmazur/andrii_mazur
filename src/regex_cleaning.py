
def clean_array_strings(array_of_strings):
    import re
    import streamlit as st
    st.write("--- doing regex cleaning---")
    array1=[]
    pattern = re.compile(r'[\t\n]+')
    for s in array_of_strings:
        cleaned_string = pattern.sub('', s)
        if cleaned_string:
            array1.append(cleaned_string)
        rejoined_string = "".join(array1).split()
    sentences = []
    current_sentence_words = []
    sentence_end_pattern = re.compile(r'[.!?]$')
    for word in rejoined_string:
        current_sentence_words.append(word)
        if sentence_end_pattern.search(word):
            sentence = " ".join(current_sentence_words)
            sentences.append(sentence)
            current_sentence_words = [] # Reset for the next sentence
    if current_sentence_words:
        sentences.append(" ".join(current_sentence_words))
    return sentences    
