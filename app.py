import streamlit as st

pg = st.navigation([st.Page("main.py"), st.Page("page2.py")])
pg.run()

