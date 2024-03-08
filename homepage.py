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
        ("Reservation of Venues", "#ff9999", reservation_of_venues),
        ("School Administration", "#99ff99", school_administration),
        ("Letter Templates", "#9999ff", letter_templates),
        ("Ateneo Map", "#ffff99", ateneo_map)
    ]

    # Create two rows with two columns each
    row1 = st.columns(2)
    row2 = st.columns(2)

    # Loop through tile data and create clickable tiles with names and colors
    for i, (name, color, page_function) in enumerate(tile_data):
        col = row1[i] if i < 2 else row2[i-2]
        with col:
            # Wrap the tile content in an anchor tag to make it clickable
            if st.markdown(
                f'<a href="/{name}" style="text-decoration: none;">'
                f'<div style="background-color: {color}; height: 150px; padding: 20px; margin: 10px; text-align: center; font-family: Arial, sans-serif; font-weight: bold; font-size: 20px; border-radius: 10px;">'
                f'{name}'
                f'</div>'
                f'</a>', 
                unsafe_allow_html=True
            ):
                navigate_to_page(page_function)

def navigate_to_page(page_function):
    page_function()

def reservation_of_venues():
    st.title("Reservation of Venues Page")
    st.write("This is the content of the Reservation of Venues page.")

def school_administration():
    st.title("School Administration Page")
    st.write("This is the content of the School Administration page.")

def letter_templates():
    st.title("Letter Templates Page")
    st.write("This is the content of the Letter Templates page.")

def ateneo_map():
    st.title("Ateneo Map Page")
    st.write("This is the content of the Ateneo Map page.")

if __name__ == "__main__":
    main()