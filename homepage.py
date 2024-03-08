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

    # Define tile names and colors
    tile_data = [
        ("Reservation of Venues", "#ff9999"),
        ("School Administration", "#99ff99"),
        ("Letter Templates", "#9999ff"),
        ("Ateneo Map", "#ffff99")
    ]

    # Create two rows with two columns each
    row1 = st.columns(2)
    row2 = st.columns(2)

    # Loop through columns and create clickable tiles with names and colors
    for i, (name, color) in enumerate(tile_data):
        col = row1[i] if i < 2 else row2[i-2]
        with col:
            # Wrap the tile content in an anchor tag to make it clickable
            if st.markdown(
                f'<a href="#" style="text-decoration: none;">'
                f'<div style="background-color: {color}; height: 150px; padding: 20px; margin: 10px; text-align: center; font-family: Arial, sans-serif; font-weight: bold; font-size: 20px; border-radius: 10px;">'
                f'{name}'
                f'</div>'
                f'</a>', 
                unsafe_allow_html=True
            ):
                navigate_to_page(name)

def navigate_to_page(name):
    st.title(f"You clicked {name}")
    st.write("This is the content of the new page.")

if __name__ == "__main__":
    main()