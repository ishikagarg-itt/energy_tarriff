import streamlit as st
from tarriff_service import fetch_tariffs
from ui_components import render_filters, render_tariff_results

st.set_page_config(page_title="Energy Tariff Viewer", layout="wide")
st.title("🔌 Energy Tariff Viewer")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Search Filters")
    user_inputs = render_filters()

with col2:
    if user_inputs.get("submit"):
        with open("styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        user_inputs_filtered = {k: v for k, v in user_inputs.items() if k != "submit"}
        df, cost_label = fetch_tariffs(**user_inputs_filtered)

        st.header("\U0001F4CA Tariff Results")
        render_tariff_results(df, cost_label)