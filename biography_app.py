import streamlit as st
from PIL import Image

# Title of the App
st.title("My Biography")

# Create two columns with a 2:1 ratio for info and image
col1, col2 = st.columns([2, 1])

# Info on the left side
with col1:
    st.header("About Me")
    st.write("""
    Hi, I'm a 4th year BSIT student at Cebu Institute of Technology University. 
    I have a passion for technology and love exploring new ideas in the field of IT.
    """)

    st.header("Hobbies & Interests")
    st.write("""
    In my free time, I love playing the guitar and immersing myself in music. 
    Music is a big part of my life, and I find it to be a great way to relax and express myself creatively.
    """)

    st.subheader("Personal Note")
    st.write("""
    I'm always eager to learn more, improve my skills, and work on interesting projects. 
    Feel free to connect with me if you'd like to talk about tech, music, or anything else!
    """)

# Profile Picture on the right side
with col2:
    # Add your own image here, make sure to replace "profile.jpg" with your actual image file path
    image = Image.open("profile.jpg")
    
    # Increase the image size and center it vertically with the text
    st.image(image, caption="Juan David R. Catulong", width=350)

# Optional: Add a subtle background color using st.markdown with custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)
