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
def main():

    tile_data = [
        ("Reservation of Venues", "#ff9999", "/reservation"),
        ("School Administration", "#99ff99", "/administration"),
        ("Letter Templates", "#9999ff", "/templates"),
        ("Ateneo Map", "#ffff99", "/map")
    ]

    # Create two rows with two columns each
    row1 = st.columns(2)
    row2 = st.columns(2)

    # Loop through tile data and create clickable tiles with names and colors
    for i, (name, color, page_name) in enumerate(tile_data):
        col = row1[i] if i < 2 else row2[i-2]
        with col:
            # Wrap the tile content in an anchor tag to make it clickable
            if st.markdown(
                f'<a href="/{page_name}" style="text-decoration: none;">'
                f'<div style="background-color: {color}; height: 150px; padding: 20px; margin: 10px; text-align: center; font-family: Arial, sans-serif; font-weight: bold; font-size: 20px; border-radius: 10px;">'
                f'{name}'
                f'</div>'
                f'</a>', 
                unsafe_allow_html=True
            ):


if __name__ == "__main__":
    main()