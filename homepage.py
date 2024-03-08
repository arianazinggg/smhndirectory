import streamlit as st
import pandas as pd

st.set_page_config(page_title="SAMAHAN Directory", 
                    page_icon=":book:",
                    layout="wide",
                    initial_sidebar_state="expanded",
)

st.title("SAMAHAN Directory")

pdf = open("SMHN GUIDEBOOK FOR STUDENT ACTIVITIES.pdf", "rb").read()
st.download_button(
        label="Download SMHN Directory",
        data=pdf,
        file_name="SMHN GUIDEBOOK FOR STUDENT ACTIVITIES.pdf",
        mime="application/pdf",
        key='download-pdf'
    )

tab1, tab2, tab3, tab4, tab5= st.tabs(["🏠Home Page","📆Reservation of Venues", "📝Letter Templates", "🕴️School Administration", "🗺️Ateneo Map"])

with tab1:
    st.header('🏠Home Page')
    st.markdown("## Website Overview")
    st.components.iframe("samahan.addu.edu.ph", width=1000, height=600)

with tab2:
    st.header('📆Reservation of Venues')

with tab3:
    st.header('📝Letter Templates')

with tab4:
    st.header('🕴️School Administration')

with tab5:
    st.header('🗺️Ateneo Map')