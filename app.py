
import streamlit as st
from streamlit_option_menu import option_menu

from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Tobias' Portfolio",
    page_icon="😎",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "About": "This my portfolio website, where you can learn more about me and my projects. Feel free to reach out to me if you have any questions or want to connect!",
    })


front_col1, front_col2 = st.columns([1,2])
with front_col1:
    st.image("images/tobias.png", use_column_width="auto")

with front_col2:
    st.title("👋 Hi, I'm Tobias!")
    st.subheader("Student and Data Science Enthusiast")
    st.markdown("I am a student at Copenhagen Business School (CBS) and I am currently studying my bachelor's degree in Business Administration and Digital Management. I am passionate about data science and I am always looking for new opportunities to learn more about the field.")

selected = option_menu(
    menu_title= None, 
    options= ["About me", 'Projects', 'Contact me'],
    icons=['file-person', 'code-slash', "person-lines-fill"], menu_icon="cast", default_index=0, orientation='horizontal') # Icons from https://icons.getbootstrap.com/


if selected == "About me":
    #st.header("Experience")

    st.header("Work Experience")
    work_col1, work_col2 = st.columns([3,1])

    with work_col1:
        st.subheader("Lenus eHealth")
        st.subheader("Junior Support Engineer")
        st.markdown("""
        - Provided prompt, professional support to clients and internal teams, ensuring a high level of service satisfaction.
        - Identified system issues and used SQL for diagnostics and resolution, assessing impact and informing product teams.
        - Implemented a no-code automation with Make to expedite the reply processes for app reviews, uniting Support with Product Marketing and Language Specialists.
        """)

    with work_col2:
        st.image("images/lenus_logo.png", use_column_width="auto")
    
    st.write("---")
    st.header("Education")


    # Experience 1
    exp1_col1, exp1_col2 = st.columns([3,1])

    with exp1_col1:
        st.subheader("COPENHAGEN BUSINESS SCHOOL")
        st.subheader("BSc Business Administration and Digital Management")
        st.write("🎓 Full Time - Current GPA 10.58 / 12.00")
        st.markdown("""
        📚 Relevant courses:
        - Business Data Analytics
        - Digital Technologies and Data-Driven Business
        - Information Management in Organizations
        """)        
        st.write("🗓️ Sep 2021 – Jun 2024")
        st.write("📍 Copenhagen, Denmark")

    with exp1_col2:
        st.image("images/CBSlogo_rgb_blue.png", use_column_width="auto")

    st.write("---")
    
    # Experience 2
    exp2_col1, exp2_col2 = st.columns([3,1])

    with exp2_col1:
        st.subheader("UNIVERSITY OF MICHIGAN STEPHEN M. ROSS SCHOOL OF BUSINESS")
        st.write("🎓 Exchange Semester - GPA 3.74 / 4.00")
        st.markdown("""
        📚 Relevant courses:
        - Advanced Analytics for Management Consulting
        - Excel Skills for Business
        - Business Intelligence and Data Visualization
        - B2B Marketing
        - Tech-Enabled Business Innovation
        """)        
        st.write("🗓️ Sep 2023 – Dec 2023")
        st.write("📍 Ann Arbor, MI")

    with exp2_col2:
        st.image("images/RossLogo.png", use_column_width="auto")

    st.write("---")

    # Experience 3
    exp3_col1, exp3_col2 = st.columns([4,1])

    with exp3_col1:
        st.subheader("BUSINESS COLLEGE VIBORG")
        st.subheader("Business & Entrepreneurship programme")
        st.markdown("""
        📚 Subjects:
        - Business Economics
        - Marketing
        - Innovation
        """)        
        st.write("Participated in Company Programme and qualified for Denmark's Championship in Entrepreneurship")
        st.write("🗓️ Aug 2016 – Jun 2019")
        st.write("📍 Viborg, Denmark")

    with exp3_col2:
        st.image("images/hhx_viborg.png", use_column_width="auto")


if selected == "Projects":
    st.header("Here's a couple of things I've worked on:")
    st.write("---")

    with st.container():
        col1, col2 = st.columns([3,1])

        with col1: 

            # Project 1
            st.subheader("📑 PDF to Content App")
            st.markdown("*This application allows users to upload a PDF file and then automatically get a Summary, 5 Question Multiple Choice Quiz and 10 Flashcards to study the uploaded content in different ways.*")
            st.markdown("The application was created to quickly start testing basic functionalities of a product idea two colleagues had")
            st.markdown("**Tools Used:** Python, Langchain, Streamlit")
            st.markdown("[Link to the project](https://pdf-to-content.streamlit.app)")

        with col2:
            st_lottie("https://lottie.host/042a8861-2832-48e1-bf47-6d968194bf48/ExhyK0yZYD.json",
                      speed=0.5,
                      height=300,
                      width=200)

    st.write("---") 
    
    with st.container():
        col3, col4 = st.columns([3,1])

        with col3: 

            # Project 2
            st.subheader("🔍 Diabetes Prediction App")
            st.markdown("*This tool provides a quick survey for users to complete. After analyzing your answers, it calculates the probability of you having diabetes using a prediction model trained with data from the National Health and Nutrition Examination Survey (NHANES).*")
            st.markdown("This application was created in collaboration with a group of students from the University of Michigan and the Michigan Data Science Team (MDST). While the model is not perfect, it is a good example of how data science can be used to create value for people.")
            st.markdown("*... if the data and questions asked are relevant.*")
            st.markdown("**Tools Used:** Python, Pandas, Tensorflow, Streamlit")
            st.markdown("[Link to the project](https://mdst-diabetes-project.streamlit.app)")

        with col4:
            st_lottie("https://lottie.host/506f41d9-f338-412f-8d48-6fbf3f3672c5/WYeRUrF9fO.json",
                      speed=1,
                      height=300,
                      width=200)

if selected == "Contact me":
    st.header("Feel free to reach out!")

    contact_form = """
    <form action="https://formsubmit.co/681bca75dace6a46b3be10dc2cfc009f" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
