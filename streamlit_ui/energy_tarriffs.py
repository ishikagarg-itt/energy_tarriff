import streamlit as st
from tarriff_service import fetch_tariffs
from ui_components import render_filters, render_tariff_results

st.set_page_config(page_title="Energy Tariff Viewer", layout="wide")
st.title("🔌 Energy Tariff Viewer")

col1, col2 = st.columns([1, 2])


st.header("Search Filters")
user_inputs = render_filters()


with open("styles.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
if user_inputs.get("submit"):
    user_inputs_filtered = {k: v for k, v in user_inputs.items() if k != "submit"}
    df, cost_label = fetch_tariffs(**user_inputs_filtered)
    st.session_state["results_df"]   = df
    st.session_state["cost_label"]   = cost_label

if "results_df" in st.session_state:
    st.header("\U0001F4CA Tariff Results")
    render_tariff_results(
        st.session_state["results_df"],
        st.session_state["cost_label"]
    )