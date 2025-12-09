
def clean_array_strings(array_of_strings):
    import re
    import streamlit as st
    st.write("--- doing regex cleaning---")
    array1=[]
    pattern = re.compile(r'[\t\n]+')
    for s in array_of_strings:
        # 2. Use re.sub to replace the targeted characters with an empty string ('')
        cleaned_string = pattern.sub('', s)
        # 3. Strip any remaining leading or trailing spaces (which were NOT removed by the regex)
        # 4. Filter: Only include the string if it is not empty after cleaning
        if cleaned_string:
            array1.append(cleaned_string)
        rejoined_string = "".join(array1)
    return rejoined_string.split()
