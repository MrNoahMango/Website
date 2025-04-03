import streamlit as st

index = st.Page("index.py", title="Home")

mango_profile = st.Page("profiles/mango.py", title="Mango")
julius_profile = st.Page("profiles/julius.py", title="Julius")

credits_page = st.Page("credits.py", title="Credits")

pg = st.navigation(
    {
        "": [index],
        "Profiles": [mango_profile, julius_profile],
        "Misc": [credits_page]
    }
)

pg.run()
