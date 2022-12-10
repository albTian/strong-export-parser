import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

DEFAULT_METRICS = ["Weight", "Reps"]


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

    # Get the unique exercises -> selected_exercise_df
    all_exercise_names = df["Exercise Name"].unique()
    selected_exercise_names = st.multiselect(
        "Select exercises", all_exercise_names)
    selected_exercise_patern = '|'.join(
        map(re.escape, selected_exercise_names))     # ex_name_1|ex_name_2
    selected_exercise_df = df[df["Exercise Name"].str.fullmatch(
        selected_exercise_patern)]

    # Display the table
    num_to_display = st.slider("How many rows to display", 0, 500)
    # st.dataframe(selected_exercise_df.head(num_to_display))

    # Choose metric to display
    selected_metric = st.selectbox("Select metric", DEFAULT_METRICS)
    selected_exercise_df = selected_exercise_df[[
        "Date", "Exercise Name", selected_metric]]
    # selected_exercise_df.head(num_to_display)
    selected_exercise_pivot = selected_exercise_df.pivot(
        columns=["Exercise Name"], values=["Date", selected_metric]).fillna(0)
    # if selected_exercise_pivot.size > 0:
    st.dataframe(selected_exercise_pivot.head(num_to_display))

    fig, ax = plt.subplots()
    selected_exercise_pivot.plot(ax=ax)
    
    st.pyplot(fig)



main()
