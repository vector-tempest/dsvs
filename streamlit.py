# prompt: make the entire code under the streamlit


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 


st.title("Data Visualization App")
st.text("Upload any csv file you want and we'll generate chatrs for you!!")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
        st.write(df.info())
        columns = df.columns.tolist()
        st.text("Select the elements you want to plot graph against")
        x_column = st.selectbox("Select X-axis Column", columns)
        y_column = st.selectbox("Select Y-axis Column", columns)

        chart_type = st.selectbox("Select Chart Type", ["bar", "scatter", "line", "pie"])

        if st.button("Generate Chart"):
            fig, ax = plt.subplots()
            if chart_type == "bar":
                sns.barplot(x=df[x_column], y=df[y_column], ax=ax)
            elif chart_type == "scatter":
                sns.scatterplot(x=df[x_column], y=df[y_column], ax=ax)
            elif chart_type == "line":
                sns.lineplot(x=df[x_column], y=df[y_column], ax=ax)
            elif chart_type == "pie":
                df[x_column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
            st.pyplot(fig)
    except Exception as e:
        st.error(f"Error processing the file: {e}")
else:
    st.info("Please upload a CSV file.")
