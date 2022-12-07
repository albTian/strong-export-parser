import streamlit as st
import numpy as np
import pandas as pd


def main():
    csv_file = st.file_uploader("Upload a strong export", type=["csv"])
    if (not csv_file):
        return

    # Read the table (auto cleans the nan)
    df = pd.read_csv(csv_file, na_filter=False)

    # Display the table
    number = st.slider("How many rows to display", 0, 100)
    st.dataframe(df.head(number))
    # st.line_chart(df, y=["Weight", "Reps"])

    # Parse the data
    df["Date"] = pd.to_datetime(df["Date"])
    df["Duration"] = pd.to_timedelta(df["Duration"])
    df["1rm"]

    df.groupby("Duration")

    
    

main()
