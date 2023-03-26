import streamlit as st

# Define the home page
def home():
    st.title("Home Page")
    st.write("Welcome to my Streamlit app!")
    st.write("Use the navigation bar to access other pages.")

# Define the calculations page
def calculations():
    st.title("Calculations Page")
    st.write("Enter the numbers you'd like to calculate:")
    x = st.number_input("Enter a value for x:")
    y = st.number_input("Enter a value for y:")
    operation = st.selectbox(
        "Select an operation",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )
    if operation == "Addition":
        result = x + y
    elif operation == "Subtraction":
        result = x - y
    elif operation == "Multiplication":
        result = x * y
    else:
        result = x / y
    st.write(f"Result: {result}")

# Define the navigation bar
pages = {
    "Home": home,
    "Calculations": calculations
}
navigation = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[navigation]()
