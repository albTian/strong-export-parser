import streamlit as st
import numpy as np
import pandas as pd
import re


def main():
    csv_file = st.file_uploader("Upload a strong export", type=["csv"])
    if (not csv_file):
        return

    # Read the table (auto cleans the nan)
    df = pd.read_csv(csv_file, na_filter=False)

    # Parse the data
    df["Date"] = pd.to_datetime(df["Date"])
    # df["Duration"] = pd.to_timedelta(df["Duration"])
    df["Volume"] = df["Weight"] * df["Reps"]

    # Get the unique exercises
    all_exercise_names = df["Exercise Name"].unique()
    selected_exercise_names = st.multiselect("Select exercises", all_exercise_names)
    selected_exercise_patern = '|'.join(map(re.escape, selected_exercise_names))     # ex1|ex2
    # print(selected_exercise_patern)

    selected_exercise_df = df[df["Exercise Name"].str.fullmatch(selected_exercise_patern)]

    # Display the table
    num_to_display = st.slider("How many rows to display", 0, 500)
    st.dataframe(selected_exercise_df.head(num_to_display))

    
    

main()
