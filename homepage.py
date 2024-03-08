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

row1 = st.columns(2)
row2 = st.columns(2)

tile_data = [
        ("Reservation of Venues", "#ff9999"),
        ("School Administration", "#99ff99"),
        ("Letter Templates", "#9999ff"),
        ("Ateneo Map", "#ffff99")
    ]

for i, (name, color) in enumerate(tile_data):
        col = row1[i] if i < 2 else row2[i-2]
        with col:
            st.markdown(f'<div style="background-color: {color}; height: 120px; padding: 20px;">{name}</div>', unsafe_allow_html=True)
