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
    from streamlit_searchbar import streamlit_searchbar

    value = streamlit_searchbar()

    st.write(value)
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 20px; color: white; background-color: #124076; margin-top: 8px; margin-bottom: 8px; margin-left: auto; margin-right: auto;">Center Administration</div>', unsafe_allow_html=True)
    # Add your content for School Administration here
    st.markdown("<br> **:blue[Fr. Karel S. San Juan, S.J.]** <br> <i>University President</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Jeremy S. Eliab]** <br> <i>Executive Vice President</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Romulo Vinci R. Bueza]** <br> <i>Executive Assistant to the President<br> Director, Ateneo Internationalization for Mindanao (AIM) Office</i> ", unsafe_allow_html=True) 
    st.markdown("<br>**:blue[Ms. Fatima Jennae B. Jereza]** <br> <i>Assistant Director, Ateneo Internationalization for Mindanao (AIM) Office</i> ", unsafe_allow_html=True) 
    st.markdown("<br>**:blue[Atty. Romeo T. Cabarde, JR.]** <br> <i>Assistant to the President for Advocacy & Legal Affairs</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Ms. Lilibeth L. Arcena]** <br> <i>Assistant to the President for Advancement</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Ms. Shiela Joy C. Gallemaso-Bacon, CPA]** <br> <i>Internal Auditor</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Ms. Suzette D. Aliño]** <br> <i>Vice President for Quality Assurance and Planning</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Ms. Suzanne Marie A. Doromal]** <br> <i>Assistant to the President for Community Center and Martin Hall Operations</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Bernie M. Jereza]** <br> <i>Assistant to the President for Information Technology<br> Director, Institutional Communications and Promotions (iCOMMP) Office</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Gian Carlo C. Tancontian]** <br> <i>Deputy Director, Institutional Communications and Promotions (iCOMMP) Office</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Jimmy E. Delgado, CPA]** <br> <i>Vice President for Finance and Treasurer</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Atty. Niceforo V. Solis]** <br> <i>Director, Human Resource Management and Development Office</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Rev. Fr. Carlos G. Cenzon, Jr., S.J., Ph.D.]** <br> <i>Director, University IT Office (UITO)</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Bernie M. Jereza]** <br> <i>Director, Management Information Systems Office – UITO</i>", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Ruben F. Estuart, Jr. ]** <br> <i>Director, Technical Services – UITO", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Jose Mari V. Freires ]** <br> <i>Quality Assurance and Cybersecurity Officer – UITO", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Ms. Carmela Marie M. Santos]** <br> <i>Director, Ecoteneo", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Alfredo Teodoro]** <br> <i>Director, Ateneo Academy", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Ms. Hannah Grace Cang]** <br> <i>OIC Director, Ateneo de Davao Academy of Lifelong Learning (ADD-ALL)", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Ms. Ozelle L. Rivamonte]** <br> <i>Manager, Purchasing Office", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Dr. Tender Grace P. Ferolin]** <br> <i>University Physical Plant Director", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Ms. Jhoan Mae A. Labog]** <br> <i>Food Court and Commercial Spaces Manager ", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Engr. Noah A. Bubod]** <br> <i>Physical Plant Supervisor – Matina Campus", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Engr. Eduvegio V. Ornopia]** <br> <i>Officer-in-Charge, Physical Plant Office, Bangkal campus", unsafe_allow_html=True)
    st.markdown("<br>**:blue[Mr. Regin Ruis B. Oliveros]** <br> <i>Program Coordinator, Madaris Volunteer Program (MVP)", unsafe_allow_html=True)
    

    #OAVP
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 20px; color: white; background-color: #124076; margin-top: 8px; margin-bottom: 8px; margin-left: auto; margin-right: auto;">Office of the Academic Vice President</div>', unsafe_allow_html=True)
    st.markdown("<br> **:blue[Ms. Gina L. Montalan, Ph.D.]** <br> <i>Academic Vice President (AVP)</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Tracy B. Villanueva]** <br> <i>Director, Admission and Aid Office</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Atty. Edgar B. Pascua II]** <br> <i>Registrar for Tertiary Education</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Fretzie F. Alfaro-Fajardo]** <br> <i>Director, University Libraries & AV Center</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Theresa Salaver-Eliab]** <br> <i>Director, Director, Office of Student Affairs</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Atty. Ira Calatrava-Valenzuela]** <br> <i>Assistant Director, Office of Student Affairs</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Leah C. Reparado]** <br> <i>Director, College Guidance and Testing Center</i>", unsafe_allow_html=True)
    #SAS
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 20px; color: white; background-color: #124076; margin-top: 8px; margin-bottom: 8px; margin-left: auto; margin-right: auto;">School of Arts and Sciences</div>', unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Renante D. Pilapil, Ph.D.]** <br> <i>Dean</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Ma. Teresa Quindoy]** <br> <i>Assistant Dean, Computer Studies — SAS</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Jeremy Glenn A. Tuvida]** <br> <i>Assistant Dean, Humanities and Letters — SAS</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Agnes T. Aranas, Ph.D.]** <br> <i>Assistant Dean, Natural Sciences and Mathematics — SAS</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Nelly Z. Limbadan, Ph.D.]** <br> <i>Assistant Dean, Social Sciences — SAS</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Benedict V. Omblero, Ph.D.]** <br> <i>Director, Ateneo Language Center</i>", unsafe_allow_html=True)
elif selected_tab == "Ateneo Map":
    st.header('🗺️ Ateneo Map')
    # Add your content for Ateneo Map here
