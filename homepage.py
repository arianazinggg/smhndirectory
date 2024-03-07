import streamlit as st

st.set_page_config(page_title="SAMAHAN Directory", 
                    page_icon=":book:",
                    layout="wide",
                    initial_sidebar_state="expanded",
)

st.title("SAMAHAN Directory")

st.download_button(
        "Download SMHN Directory",
        pdf,
        "SMHN GUIDEBOOK FOR STUDENT ACTIVITIES.pdf",
        "text/pdf",
        key='download-pdf'
        )