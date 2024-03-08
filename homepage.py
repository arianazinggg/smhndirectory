import streamlit as st

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

tab1, tab2, tab3, tab4= st.tabs(["🏠Home","📆Reservation of Venues", "🕴️School Administration", "🗺️Ateneo Map" ])

st.markdown(
    """
    <style>
        /* Set the width of each tab to 25% */
        .streamlit-tabs > div[role="tablist"] > div[role="tab"] {
            width: 25%;
        }
    </style>
    """,
    unsafe_allow_html=True
)
