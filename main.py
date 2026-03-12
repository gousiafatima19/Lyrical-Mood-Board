import streamlit as st
import requests
st.title("Lyrical Mood Board")
pexels_api = "n13lM7nHqQOHkfvct59J8O4ipHjPD9J5sRatjjw3FHVXg22HEHIpShFV"
word = st.text_input("Enter a word from song lyrics:")
is_clicked = st.button("Search", use_container_width=True, type="primary")
if is_clicked:
    res = requests.get(f"https://api.datamuse.com/words?ml={word}")
    if res.status_code == 200:
        data = res.json()
        if not data:
            st.write("No related words found.")
        else:
            st.write("Related Words and Images:")
            count = 1
            for item in data[:5]:
                related_word = item.get("word")
                st.write(f"{count}. {related_word}")
                img_res = requests.get(
                    f"https://api.pexels.com/v1/search?query={related_word}&per_page=1",
                    headers={"Authorization": pexels_api}
                )
                if img_res.status_code == 200:
                    img_data = img_res.json()
                    photos = img_data.get("photos", [])
                    if photos:
                        image_url = photos[0]["src"]["medium"]
                        st.image(image_url)
                st.write("-" * 50)
                count += 1
    else:
        st.write("Error:", res.status_code)