import streamlit as st
import pandas as pd
import card

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
tabs = ["Home", "Request & Reservations", "Letter Templates", "School Administration", "Ateneo Map"]
selected_tab = st.selectbox("Select a tab:", tabs)

# Display content based on the selected tab
if selected_tab == "Home":
    st.markdown('<iframe src="https://samahan.addu.edu.ph" width="1300" height="500"></iframe>', unsafe_allow_html=True)
elif selected_tab == "Request & Reservations":

#STEP 1    
    st.header('📆 Requests & Reservation')
    st.markdown('<div style="display: inline-block; padding: 10px;border-radius: 10px;text-align: center; font-family: Helvetica; font-size: 20px;color: white; background-color: #124076;margin-top: 8px; margin-bottom: 8px;">STEP 1 - Submission of Concept Paper</div>', unsafe_allow_html=True)
    st.markdown("""
    Submit the Concept Paper to the Office of the Student Affairs
    HOW? Fill up the Google Form using the Organization's Email. You will be given a receipt of your submission shortly. 

    You may send your follow-ups and concerns to the OSA Program Coordinator, Mr. Benz Edd Garay <beagaray@addu.edu.ph>.

    You may access the Google Form Link below: 
    """)
    st.markdown("[Concept Paper Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdpCHygaKo64U6MUpV9kO6wCdWpWnuw29TZOPLwxcg5pVpAGA/viewform)")
    st.markdown('<div style="display: inline-block; padding: 10px;border-radius: 10px;text-align: center; font-family: Helvetica; font-size: 20px;color: white; background-color: #124076;margin-top: 8px;margin-bottom: 8px;">STEP 2 - Venue Reservation</div>', unsafe_allow_html=True)
    st.write("<i>Note: These venues are available on a first-come and first-serve basis. Make sure that you include all the necessary details in your letter of request together with your approved concept paper.</i>", unsafe_allow_html=True)

#STEP 2
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: black; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>Arrupe Hall, Ground Floor Martin Hall</i></div>', unsafe_allow_html=True)
    
    #information

    paragraph = "Directly go to the Office of the Student Affairs located at Mezzanine Floor, Martin Hall. Ask for a <i>Reservation Form</i> where you will fill up the necessary information in the form. Also, there will be signatories needed for the reservation. When the reservation is already approved by OSA, proceed to the front desk of Community Center of the First Companions (CCFC), and wait for the approval of Ma'am Suzanne Marie Doromal, the Assistant to the President for Community Center Operations."
    st.write(f'<p style="text-align: justify;">{paragraph}</p>', unsafe_allow_html=True)

    
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: black; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>4th Floor, 6th Floor, or 7th Floor Martin Hall</i></div>', unsafe_allow_html=True)
    paragraph1 = "Proceed to the Athletics Office located at the back of the 4th floor of Martin Hall, look for Ma’am Ivy Guadalquiver (icguadalquiver@addu.edu.ph) and inquire about the availability of the venue. Obtain a copy of the <i>Martin Hall Reservation Form</i> as soon as your event has been tentatively scheduled."
    st.write(f'<p style="text-align: justify;">{paragraph1}</p>', unsafe_allow_html=True)


    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: black; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>Conference Rooms, Ricci Hall 3rd Floor CCFC Building</i></div>', unsafe_allow_html=True) 
    paragraph2 = "Proceed to the Ground floor of the Community Center of the First Companions (CCFC) Building and look for Ma’am Charlene Apayart (cmapayart@addu.edu.ph). Inquire about the availability of the conference rooms and obtain a copy of the <i>Ricci Hall Reservation Form</i> as soon as your event has been tentatively scheduled."
    st.write(f'<p style="text-align: justify;">{paragraph2}</p>', unsafe_allow_html=True)

    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: black; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>UCEAC Media/Training Room, 8th Floor CCFC Building</i></div>', unsafe_allow_html=True)
    paragraph3 = "Send a Letter of Request to Mr. Mark Paul Samante (mposamante@addu.edu.ph), UCEAC Chairperson and you may also cc: UCEAC (uceac@addu.edu.ph), or proceed to the 8th floor of the CCFC Building UCEAC Office and inquire about the availability of the Media or Training Room. Obtain a copy of the Room Reservation Form as soon as your event has been tentatively scheduled."
    st.write(f'<p style="text-align: justify;">{paragraph3}</p>', unsafe_allow_html=True)

    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: black; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>Jubilee “J” Building Classrooms, Bapa Benny Tudtud Auditorium and Finster Auditorium 7th Floor Finster</i></div>', unsafe_allow_html=True)
    paragraph4 = "Proceed to the Physical Plant Office (PPO) located at the 1st Floor, Dotterweich (Law Building), request through the window and look for Ms. Carmen Celebrar (cscelebrar@addu.edu.ph). Inquire about the availability of the venues you want to reserve. Obtain a copy of the Reservation Form as soon as your event has been tentatively scheduled. Wait until Engr. Tender Grace Ferolin (tpferolin@addu.edu.ph), PPO Director, approves the reservation."
    st.write(f'<p style="text-align: justify;">{paragraph4}</p>', unsafe_allow_html=True)


#STEP 3
    st.markdown('<div style="display: inline-block; padding: 10px;border-radius: 10px;text-align: center; font-family: Helvetica; font-size: 20px;color: white; background-color: #124076;margin-top: 8px; margin-bottom: 8px;">STEP 3 - Environmental Resource Management Plan (ERMAP)</div>', unsafe_allow_html=True)
    ermap = "Process the ERMAP form at the ECOTENEO Office located at the 5th Floor, Martin Hall (right side of the stage). If you will serve snacks or meals during your event, make sure to secure the details of your food supplier, the materials used for its packaging, and your plans for disposal."
    st.write(f'<p style="text-align: justify;">{ermap}</p>', unsafe_allow_html=True)

#STEP 4
    st.markdown('<div style="display: inline-block; padding: 10px;border-radius: 10px;text-align: center; font-family: Helvetica; font-size: 20px;color: white; background-color: #124076;margin-top: 8px; margin-bottom: 8px;">STEP 4 - Request for Equipment</div>', unsafe_allow_html=True)
    st.write("<i>Note: You may simultaneously process your request for equipment with your venue reservation to save time. Make sure to indicate all the equipment needed for your event (e.g. sound system, microphone, tables, chairs, platforms, etc.) For events with tables and chairs, don’t forget to attach a detailed floor plan of the venue in your letter. Be aware that such requests may necessitate a Job Order and may incur overtime fees (for university staff who work outside of normal hours), so remember to settle your payment with Finance afterward.</i>", unsafe_allow_html=True)

    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: black; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>LED/iCOMMP Studio</i></div>', unsafe_allow_html=True)
    markdown_link = "[Concept Paper Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdpCHygaKo64U6MUpV9kO6wCdWpWnuw29TZOPLwxcg5pVpAGA/viewform)"
    st.markdown(f"<i>Fill up the {markdown_link}</i>", unsafe_allow_html=True)

elif selected_tab == "Letter Templates":
    st.header('📝 Letter Templates')

    col1, col2, col3 = st.columns((1,1,1))
    import base64
    with open('pictures\martin_hall.jpg', "rb") as a:
        data = a.read()
        encoded = base64.b64encode(data)
    martin = "data:image/png;base64," + encoded.decode("utf-8")
    
    with open(r'pictures\tudtud.jpg', "rb") as b:
        tudtud_read = base64.b64encode(b.read())
    tudtud = "data:image/png;base64," + tudtud_read.decode("utf-8")
    
    with open(r'pictures\arrupe.jpg', "rb") as c:
        data = c.read()
        encoded = base64.b64encode(data)
    arrupe = "data:image/png;base64," + encoded.decode("utf-8")

    with open(r'pictures\conference_room.jpg', "rb") as d:
        data = d.read()
        encoded = base64.b64encode(data)
    conf_room = "data:image/png;base64," + encoded.decode("utf-8")

    with open(r'pictures\finaud.jpg', "rb") as e:
        data = e.read()
        encoded = base64.b64encode(data)
    finaud = "data:image/png;base64," + encoded.decode("utf-8")

    with open(r'pictures\hisflex.jpg', "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    hisflex = "data:image/png;base64," + encoded.decode("utf-8")
   
   
    with col1:
        card(title="Martin Hall",
        text="4th Flr, Martin Hall",
        image=martin,
        styles={
            'card':{
                "width":"105%"}},
        url="https://samahan.addu.edu.ph/")
        
    
        card(title="Bapa Benny Tudtud Auditorium",
        text="Ateneo de Davao - Jacinto",
        image=tudtud,
        styles={
            'card':{
                "width":"105%"}},
        url="https://samahan.addu.edu.ph/")

    with col2: 
        card(title="Arrupe Hall",
        text="1st Flr, Martin Hall",
        image=arrupe,
        styles={
            'card':{
                "width":"105%"}},
        url="https://github.com/gamcoh/st-cardhttps://samahan.addu.edu.ph/")

        card(title="Hisflex Classrooms",
        text="Ateneo de Davao - Jacinto",
        image=hisflex,
        styles={
            'card':{
                "width":"105%"}},
        url="https://samahan.addu.edu.ph/")
    
    with col3: 
        card(title="CCFC Conference Rooms",
        text="3rd Flr, Ricci Hall",
        image=conf_room,
        styles={
            'card':{
                "width":"105%"}},
        url="https://samahan.addu.edu.ph/")

        card(title="Finster Auditorium",
        text="7th Flr, Finster Building",
        image=finaud,
        styles={
            'card':{"width":"105%"}},
        url="https://samahan.addu.edu.ph/")
    
elif selected_tab == "School Administration":
    st.header('🕴️ School Administration')
   
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 20px; color: white; background-color: #124076; margin-top: 8px; margin-bottom: 8px; margin-left: auto; margin-right: auto;">Center Administration</div>', unsafe_allow_html=True)
    # Add your content for School Administration here
    st.markdown("**:blue[Fr. Karel S. San Juan, S.J.]** <br> <i>University President</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Jeremy S. Eliab]** <br> <i>Executive Vice President</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Romulo Vinci R. Bueza]** <br> <i>Executive Assistant to the President<br> Director, Ateneo Internationalization for Mindanao (AIM) Office</i> ", unsafe_allow_html=True) 
    st.markdown("**:blue[Ms. Fatima Jennae B. Jereza]** <br> <i>Assistant Director, Ateneo Internationalization for Mindanao (AIM) Office</i> ", unsafe_allow_html=True) 
    st.markdown("**:blue[Atty. Romeo T. Cabarde, JR.]** <br> <i>Assistant to the President for Advocacy & Legal Affairs</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Lilibeth L. Arcena]** <br> <i>Assistant to the President for Advancement</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Shiela Joy C. Gallemaso-Bacon, CPA]** <br> <i>Internal Auditor</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Suzette D. Aliño]** <br> <i>Vice President for Quality Assurance and Planning</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Suzanne Marie A. Doromal]** <br> <i>Assistant to the President for Community Center and Martin Hall Operations</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Bernie M. Jereza]** <br> <i>Assistant to the President for Information Technology<br> Director, Institutional Communications and Promotions (iCOMMP) Office</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Gian Carlo C. Tancontian]** <br> <i>Deputy Director, Institutional Communications and Promotions (iCOMMP) Office</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Jimmy E. Delgado, CPA]** <br> <i>Vice President for Finance and Treasurer</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Atty. Niceforo V. Solis]** <br> <i>Director, Human Resource Management and Development Office</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Rev. Fr. Carlos G. Cenzon, Jr., S.J., Ph.D.]** <br> <i>Director, University IT Office (UITO)</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Bernie M. Jereza]** <br> <i>Director, Management Information Systems Office – UITO</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Ruben F. Estuart, Jr. ]** <br> <i>Director, Technical Services – UITO", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Jose Mari V. Freires ]** <br> <i>Quality Assurance and Cybersecurity Officer – UITO", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Carmela Marie M. Santos]** <br> <i>Director, Ecoteneo", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Alfredo Teodoro]** <br> <i>Director, Ateneo Academy", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Hannah Grace Cang]** <br> <i>OIC Director, Ateneo de Davao Academy of Lifelong Learning (ADD-ALL)", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Ozelle L. Rivamonte]** <br> <i>Manager, Purchasing Office", unsafe_allow_html=True)
    st.markdown("**:blue[Dr. Tender Grace P. Ferolin]** <br> <i>University Physical Plant Director", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Jhoan Mae A. Labog]** <br> <i>Food Court and Commercial Spaces Manager ", unsafe_allow_html=True)
    st.markdown("**:blue[Engr. Noah A. Bubod]** <br> <i>Physical Plant Supervisor – Matina Campus", unsafe_allow_html=True)
    st.markdown("**:blue[Engr. Eduvegio V. Ornopia]** <br> <i>Officer-in-Charge, Physical Plant Office, Bangkal campus", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Regin Ruis B. Oliveros]** <br> <i>Program Coordinator, Madaris Volunteer Program (MVP)", unsafe_allow_html=True)
    

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
    
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: white; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>Computer Studies</i></div>', unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Antonio G. Bulao II]** <br> <i>Chairperson, Computer Science Department <br> Coordinator, BS Data Science Program</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Adrian Ablazo]** <br> <i>Chairperson, Information Technology Department <br> and Information Systems Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Patrick Angelo Paasa]** <br> <i>Director, Ateneo de Davao Research in Information Systems and Software <br> Engineering (ARISEn) Laboratory</i>", unsafe_allow_html=True)
    
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: white; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>Humanities and Letters</i></div>', unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Stella Marie G. Arcenas, Ph.D.]** <br> <i> Chairperson, Languages, Literature, and Arts Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Joseph A. Laroscain, Ph.D.]** <br> <i>Chairperson, Mass Communication Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Vida Mia S. Valverde, Ph.D.]** <br> <i>Chair, Philosophy Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Roawie L. Quimba, Ph.D.]** <br> <i>Chairperson, Theology Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Maricar Gay V. Panda, Ph.D.]** <br> <i>Director, Confucius Institute</i>", unsafe_allow_html=True)
    

    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: white; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>Natural Sciences and Mathematics</i></div>', unsafe_allow_html=True)
    st.markdown("**:blue[Dr. Anna Liza V. Llamera]** <br> <i> Chairperson, Biology Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Joval C. Afalla, Ph.D.]** <br> <i>Chairperson, Chemistry Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Doris B. Montecastro, Ph.D.]** <br> <i>Chairperson, Environmental Science Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Joseph E. Belida]** <br> <i>Chairperson, Mathematics Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Raymund S. Vizcarra, Ph. D.]** <br> <i>Chair, Physics Department</i>", unsafe_allow_html=True)
    
    st.markdown('<div style="display: inline-block; padding: 10px; border-radius: 10px; text-align: center; font-family: Helvetica; font-size: 14px; color: white; background-color: #FFEDD8; margin-top: 8px; margin-bottom: 8px;"><i>Social Sciences</i></div>', unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Rosalinda C. Tomas]** <br> <i> Chairperson, Anthropology Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Atty. Augusto Jose Emmanuel B. Gatmaytan, Ph.D.]** <br> <i>Director, Ateneo Institute of Anthropology</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Christian C. Pasion]** <br> <i>Chairperson, Economics Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Krizza Janica B. Hannah]** <br> <i>Chairperson, International Studies Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Sultan U. Ubpon]** <br> <i>Chairperson, Islamic Studies Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Rhodalie O. Emilio]** <br> <i>Chairperson, Political Science and History Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Dr. Samuel H. Aquino, Jr.]** <br> <i>Chairperson, Psychology Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Epifania Melba L. Manapol, Ph.D.]** <br> <i>Chairperson, Social Work Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Mr. Jerome A. Serrano]** <br> <i>Chairperson, Sociology Department</i>", unsafe_allow_html=True)
    st.markdown("**:blue[Ms. Christine S. Diaz]** <br> <i>Coordinator, Development Studies Graduate Program</i>", unsafe_allow_html=True)
    

elif selected_tab == "Ateneo Map":
    st.header('🗺️ Ateneo Map')
    # Add your content for Ateneo Map here
