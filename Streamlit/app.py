import streamlit as st
import pandas as pd
import numpy as np 
import random 

# Set the title of the app
st.title("Hello Streamlit")

#display a simple text
st.write("This is a simple Streamlit app.")

# Create a simple DataFrame
data = {
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)

# Display the DataFrame
st.write("Here is a simple DataFrame:")
st.dataframe(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Column 1', 'Column 2', 'Column 3']
)
st.write(chart_data)

st.line_chart(chart_data)