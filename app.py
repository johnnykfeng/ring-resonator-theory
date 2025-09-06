import streamlit as st

pg = st.navigation([
    st.Page("main.py", title="Model"), 
    st.Page("ring_res_simulator.py", title="Meep Simulator")])
pg.run()

