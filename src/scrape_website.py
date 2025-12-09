def scrape_website(url):
    import requests
    from requests.exceptions import RequestException, Timeout
    import streamlit as st
    st.write("--- scrape_website active ---")
    BASE_URL = url
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
    }

    def fetch(url, *, timeout=10):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=timeout)
            resp.raise_for_status()
            return resp
        except (RequestException, Timeout) as e:
            print(f"Request failed: {e}")
            return None

    response = fetch(BASE_URL)
    if response is None:
        raise SystemExit("Stopping: could not fetch the page.")
    return response.text
