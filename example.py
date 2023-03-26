import streamlit as st

# Define the home page
def home():
    st.title("Home Page")
    choice = st.radio(
        "Select an option:",
        ["Perform basic calculations", "Perform advanced calculations"]
    )
    if choice == "Perform basic calculations":
        basic_calculations()
    elif choice == "Perform advanced calculations":
        advanced_calculations()

# Define the basic calculations page
def basic_calculations():
    st.title("Basic Calculations")
    operation = st.sidebar.selectbox(
        "Select an operation",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )
    x = st.sidebar.number_input("Enter a value for x:")
    y = st.sidebar.number_input("Enter a value for y:")
    if operation == "Addition":
        result = x + y
    elif operation == "Subtraction":
        result = x - y
    elif operation == "Multiplication":
        result = x * y
    else:
        result = x / y
    st.write(f"Result: {result}")

# Define the advanced calculations page
def advanced_calculations():
    st.title("Advanced Calculations")
    # TODO: Implement more complex calculations here
    st.write("Sorry, this feature is still under construction.")

# Run the app
home()
