import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Corporate Account Manager
    **Dell Inc.** | *June 2023 - August 2023*
    
    - Acquired proficiency in Dell's internal systems to gather customer information and identify potential new customers.
    - Learned and applied sales scripts to make outbound calls and promote products. 
    - Compiled customer data and conducted background research before contacting clients. 
    """)
    
    st.markdown("""
    ### Software Development Intern
    **Suzhou Siweike Special Equipment Manufacturing Co., Ltd.** | *May 2022 - August 2022*
    
    - Conducted industry research on the cold chain logistics sector and processed 800,000+ pieces of sales data with Excel.
    - Analyzed and organized sales data from various regions across the country, and assist in identifying key competitive regions.
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Customer Segmentation Analysis",
            "description": "Used K-means clustering to segment customers based on purchasing behavior.",
            "skills": ["Python", "scikit-learn", "Pandas", "Matplotlib"],
            "outcome": "Identified 5 distinct customer segments that informed targeted marketing campaigns."
        },
        {
            "title": "Predictive Maintenance System",
            "description": "Developed a model to predict equipment failures before they occur.",
            "skills": ["Python", "TensorFlow", "Time Series Analysis", "IoT"],
            "outcome": "Reduced downtime by 23% and maintenance costs by 15%."
        },
        {
            "title": "Natural Language Processing for Customer Support",
            "description": "Created a text classification system to automatically categorize customer support tickets.",
            "skills": ["Python", "NLTK", "spaCy", "BERT"],
            "outcome": "Improved response time by 35% and increased customer satisfaction scores."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Machine Learning:** scikit-learn, TensorFlow, PyTorch
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** AWS, Azure, Google Cloud
        - **Web Development:** Django, Flask, React
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 