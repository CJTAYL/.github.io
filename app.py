from PIL import Image
import streamlit as st 

st.set_page_config(page_title="CJT Portfolio", page_icon=":tada:", layout="wide")

# --- LOAD ASSESTS ---
img_contact_form = Image.open("Images/image_1.jpeg")

# --- HEADER SECTION ---
with st.container():
    st. subheader("Chris Taylor")
    st.title("Data Scientist Based in Durham, NC")

# --- ABOUT ME ---
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.write("Chris Taylor is a former behavioral constant and single-case researcher seeking an internship related to data science.")
        st.write("His primary interests involve using big data to help members of marginalized populations and data-driven health practices.")
        st.header("Skills")
        st.write("""
                - R
                - Python (Pandas, Altair, Streamlit)
                - Statistics
                - Technical Writing
                - Teaching
                """)
# --- CV ---
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Education")
        st.write(
            """
            - University of Colorado - Boulder, CO
                - MS in Data Science
                - In progress
            """
        )
        st.write(
            """
            - University of Kentucky - Lexington, KY
                - MS in Special Education
                - 2015
            """
        )
    with right_column:
        st.header("Relevant Courses")
        st.write(
            """
            - Probability Theory
            - Statistical Inference
            - Modern Regression Analysis in R
            - ANOVA and Experimental Design 
            - Fundamentals of Visualization
            """
        )
    st.header("Publications")
    st.write("Ringdahl, J. E., Berg, W. K., Wacker, D. P., Cook, K., Molony, M. A., Vargo, K. K., Neurnberger, J. E., Zabala, K., & **Taylor, C. J.** (2018). Effects of response preference on resistance to change. *Journal of the Experimental Analysis of Behavior*, 109, 265-280.")
    st.write("**Taylor, C. J.**, Spriggs, A. D., Ault, M. J., Flanagan, S. M., & Sartini, E. (2017). A systematic review of using weighted vests with individuals with autism spectrum disorder. *Research in Autism Spectrum Disorders*, 37, 49-60.")
    st.header("Recent Experience")
    st.write("""
            **Behavioral Consultant** - Carolina Center for ABA and Autism Treatment, Cary NC
            - Used R and Microsoft Excel to examine client data
            - Led research seminar for collegues
            - Provided training to new employees
            """)
    st.write("---")

# --- PROJECTS ---
with st.container():
    st.header("Projects")
    st.write("[Variables Affecting COVID-19](http://rpubs.com/CJTA/948749)")
