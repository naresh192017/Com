import streamlit as st

def home():
    st.title("Home Page")
    option = st.radio(
        "Select an option:",
        ("Perform basic calculations", "Perform advanced calculations")
    )
    if option == "Perform basic calculations":
        basic_calculations()
    elif option == "Perform advanced calculations":
        advanced_calculations()

def basic_calculations():
    st.title("Basic Calculations")
    operation = st.sidebar.selectbox(
        "Select an operation",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )
    x = st.sidebar.number_input("Enter a value for x:", value=0)
    y = st.sidebar.number_input("Enter a value for y:", value=0)
    if operation == "Addition":
        result = x + y
    elif operation == "Subtraction":
        result = x - y
    elif operation == "Multiplication":
        result = x * y
    elif operation == "Division":
        result = x / y
    else:
        result = None
    if result is not None:
        st.write(f"Result: {result}")

def advanced_calculations():
    st.title("Advanced Calculations")
    # TODO: Implement advanced calculations

home()
