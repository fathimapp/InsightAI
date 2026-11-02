import streamlit as st

DATA_KEY = "uploaded_dataframe"


def save_dataframe(df):
    st.session_state[DATA_KEY] = df


def get_dataframe():
    return st.session_state.get(DATA_KEY)


def clear_dataframe():
    if DATA_KEY in st.session_state:
        del st.session_state[DATA_KEY]