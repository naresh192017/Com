import streamlit as st

def home():
    st.title("Home Page")
    st.write("Welcome to the home page")

def about():
    st.title("About Page")
    st.write("This is the about page")

# Create a dictionary to map page names to functions
pages = {
    "Home": home,
    "About": about
}

# Add a menu to the sidebar to allow the user to switch between pages
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Call the selected page function
page = pages[selection]
page()
