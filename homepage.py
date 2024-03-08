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


# Define the tabs
tabs = ["Home", "Reservation of Venues", "Letter Templates", "School Administration", "Ateneo Map"]
selected_tab = st.selectbox("Select a tab:", tabs)

# Display content based on the selected tab
if selected_tab == "Home":
    st.markdown('<iframe src="https://samahan.addu.edu.ph" width="1300" height="500"></iframe>', unsafe_allow_html=True)
elif selected_tab == "Reservation of Venues":
    st.header('📆 Reservation of Venues')
    st.markdown('<div style="display: inline-block; padding: 10px;border-radius: 10px;text-align: center; font-family: Helvetica; font-size: 20px;color: white; background-color: #124076;margin-top: 8px; margin-bottom: 8px;">STEP 1</div>', unsafe_allow_html=True)
    st.markdown("""
    Submit the Concept Paper to the Office of the Student Affairs
    HOW? Fill up the Google Form using the Organization's Email. You will be given a receipt of your submission shortly. 

    You may send your follow-ups and concerns to the OSA Program Coordinator, Mr. Benz Edd Garay <beagaray@addu.edu.ph>.

    You may access the Google Form Link below: 
    """)
    st.markdown("[Concept Paper Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdpCHygaKo64U6MUpV9kO6wCdWpWnuw29TZOPLwxcg5pVpAGA/viewform)")
    st.markdown('<div style="display: inline-block; padding: 10px;border-radius: 10px;text-align: center; font-family: Helvetica; font-size: 20px;color: white; background-color: #124076;margin-top: 8px;margin-bottom: 8px;">STEP 2</div>', unsafe_allow_html=True)
    st.write("<i>Note: These venues are available on a first-come and first-serve basis. Make sure that you include all the necessary details in your letter of request together with your approved concept paper.</i>", unsafe_allow_html=True)
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: white; background-color: #A87C7C; margin-top: 8px; margin-bottom: 8px;"><i>Arrupe Hall, Ground Floor Martin Hall</i></div>', unsafe_allow_html=True)
    st.write("Directly go to the Office of the Student Affairs located at Mezzanine Floor, Martin Hall. Ask for a <i>Reservation Form</i> where you will fill up the necessary information in the form. Also, there will be signatories needed for the reservation. Proceed to the Ecoteneo Office located at 5th Floor, Martin to get a <i>Environmental Resource Management Plan</i>, fill up the needed details and get it signed by the Ecoteneo Director. <p> When the two reservations are already approved by OSA & Ecoteneo, proceed to the front desk of Community Center of the First Companions (CCFC), and wait for the approval of Ma'am Suzanne Marie Doromal, the Assistant to the President for Community Center Operations. The reservation will take place in less than 2-3 days and they will contact you to receive the <i>Job Order</i> for it to be paid at the Finance Office.</p>", unsafe_allow_html=True)
elif selected_tab == "Letter Templates":
    st.header('📝 Letter Templates')
    # Add your content for Letter Templates here
elif selected_tab == "School Administration":
    st.header('🕴️ School Administration')
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 20px; color: white; background-color: #124076; margin-top: 8px; margin-bottom: 8px; margin-left: auto; margin-right: auto;">Center Administration</div>', unsafe_allow_html=True)
    # Add your content for School Administration here
    st.write("** Fr. Karel S. San Juan, S.J. **" "<p><i> University President</i></p>")

elif selected_tab == "Ateneo Map":
    st.header('🗺️ Ateneo Map')
    # Add your content for Ateneo Map here
