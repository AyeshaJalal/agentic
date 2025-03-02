import streamlit as st

st.title("Agentic AI")
st.text(
    "Welcome to Agentic AI.We are a team of AI experts and we are here to help you with your AI needs."
)

st.write("We are a team of AI experts and we are here to help you with your AI needs.")
st.text_area("Enter your message")
st.text_input("Enter your name")
image = st.camera_input("Take a picture")
st.video("https://www.youtube.com/watch?v=jnPP5etOZXs")

# Create a sample data dictionary
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [28, 24, 32],
    "Role": ["Data Scientist", "ML Engineer", "AI Researcher"],
}

# Display the table using streamlit
st.table(data)
# Create a button
if st.button("Click me!"):
    st.write("You clicked the button!")
    

