import streamlit as st

mango_profile = st.Page("profiles/mango.py", title="Mango")
julius_profile = st.Page("profiles/julius.py", title="Julius")

pg = st.navigation(
    {
        "Profiles": [mango_profile, julius_profile]
    }
)

pg.run()
