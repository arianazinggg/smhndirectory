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

tab1, tab2= st.tabs(["Homepage","Contact Us" ])

    
    # CSS for styling the tiles
css = """
    <style>
    .tile {
        background-color: #f4f4f4;
        border-radius: 5px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """
st.markdown(css, unsafe_allow_html=True)
    
    # Tiles
st.write('<div class="tile">Reserving of Venues<br>This is the content of Tile 1</div>', unsafe_allow_html=True)
st.write('<div class="tile">Making Letters<br>This is the content of Tile 2</div>', unsafe_allow_html=True)
st.write('<div class="tile">School Admin<br>This is the content of Tile 3</div>', unsafe_allow_html=True)
