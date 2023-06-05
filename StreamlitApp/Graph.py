import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Web Application")

    # Add text
    st.header("Welcome!")
    st.write("This is a web application built with Streamlit.")

    # Add an image
    # st.image("image.jpg", caption="Streamlit Logo", use_column_width=True)

    # Add a file uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.dataframe(data)

    # Add a plot
    x = [1, 2, 3, 4, 5]
    y = [3, 5, 2, 6, 1]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
