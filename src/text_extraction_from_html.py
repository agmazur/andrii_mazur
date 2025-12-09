def text_extractoin_from_html(html):
    import streamlit as st
    st.write("--- text_extractoin_from_html ---")
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    all_p_tags=soup.find_all('p')
    p_text=[]
    for ptag in all_p_tags:
        if ptag.get_text()=="":
            pass
        else:
            p_text.append(ptag.get_text())
    return p_text