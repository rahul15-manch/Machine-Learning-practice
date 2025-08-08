import streamlit as st
st.title("Streamlit Text  Input")
name=st.text_input("Enter some text")
if name:
    st.write(f"You entered: {name}")
else:
    st.write("Please enter some text above.")


age=st.slider("Select your age", 0, 100, 25)
st.write(f"You selected age: {age}")


options=["Option 1", "Option 2", "Option 3"]
choice=st.selectbox("Choose an option", options)
st.write(f"You selected: {choice}")

uploded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploded_file is not None:
    content = uploded_file.read()
    st.write("File content:")
    st.text(content.decode("utf-8"))