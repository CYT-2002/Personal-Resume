import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Yuting_CHEN_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Yuting CHEN")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** 13387883448@163.com
    - **Phone:** +86 13387883448
    - **Address:** Dalian, Liaoning Province, Mainland China
    """)

    st.header("Professional Summary")
    st.markdown("""
    Highly skilled software engineer with over 5 years of experience in developing scalable web applications. Proven ability to lead teams, manage projects, and improve software performance. Seeking a challenging role to utilize my technical expertise and problem-solving skills.
    """)

    st.header("Work Experience")
    st.markdown("""
    **Dell Inc.**
    - *June 2023 - August 2023*
    - Acquired proficiency in Dell's internal systems to gather customer information and identify potential new customers.
    - Learned and applied sales scripts to make outbound calls and promote products. 
    - Compiled customer data and conducted background research before contacting clients, ensuring effective communication. 
    - Maintained meticulous records of communication content and customer feedback post-call, laying the groundwork for subsequent interactions.
    
    **Suzhou Siweike Special Equipment Manufacturing Co., Ltd.**
    - *May 2022 - August 2022*
    - Conducted industry research on the cold chain logistics sector and processed 800,000+ pieces of sales data with Excel.
    - Analyzed and organized sales data from various regions across the country, and assist in identifying key competitive regions.
    """)

    st.header("Education")
    st.markdown("""
    **Master of Marketing**
    - Chinese University of Hong Kong
    - *Graduated: October 2025*
    - GPA: 3.9/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, JavaScript, Java, C++
    - **Web Technologies:** HTML, CSS, React, Node.js, Django
    - **Databases:** MySQL, PostgreSQL, MongoDB
    - **Tools:** Git, Docker, Jenkins, AWS
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Certifications")
    st.markdown("""
    - AWS Certified Solutions Architect
    - Certified Scrum Master
    """)

    st.header("Projects")
    st.markdown("""
    **E-commerce Website**
    - Developed a full-stack e-commerce application using React and Django.
    - Integrated payment gateways and implemented user authentication.

    **Data Analysis Tool**
    - Created a Python-based tool for analyzing large datasets and visualizing results.
    - Used pandas and matplotlib libraries for data manipulation and plotting.
    """)

    st.header("Languages")
    st.markdown("""
    - **English:** Fluent
    """)

    st.header("Interests")
    st.markdown("""
    - Open-source contributions
    - Blogging about technology trends
    - Hiking and outdoor activities
    """)

    st.markdown("---") 