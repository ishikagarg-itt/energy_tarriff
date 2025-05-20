import streamlit as st
from tarriff_service import fetch_independer_tariffs, fetch_energievergelijk_tariffs
from ui_components import render_energievergelijk_filters, render_independer_filters, render_independer_tariff_results, render_energievergelijk_tariff_results
import os

st.set_page_config(page_title="Energy Tariff Viewer", layout="wide")
st.title("🔌 Energy Tariff Viewer")

TOOL_OPTIONS = {
    "Independer": "independer",
    "Energievergelijk": "energyvergelijk"
}

st.header("Search Filters")
tool_name = st.selectbox("Choose comparison tool", list(TOOL_OPTIONS.keys()))
selected_tool = TOOL_OPTIONS[tool_name]
if selected_tool == "independer":
    user_inputs = render_independer_filters()
elif selected_tool == "energyvergelijk":
    user_inputs = render_energievergelijk_filters()
else:
    user_inputs = {}

style_path = os.path.join(os.path.dirname(__file__), "styles.css")

with open(style_path, encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if user_inputs.get("submit"):
    user_inputs_filtered = {k: v for k, v in user_inputs.items() if k != "submit"}
    
    if selected_tool == "independer":
        df, cost_label = fetch_independer_tariffs(**user_inputs_filtered)
    elif selected_tool == "energyvergelijk":
        df, cost_label = fetch_energievergelijk_tariffs(**user_inputs_filtered)
    else:
        df, cost_label = None, None

    st.session_state["results_df"] = df
    st.session_state["cost_label"] = cost_label
    st.session_state["selected_row"] = None

if "results_df" in st.session_state and st.session_state["results_df"] is not None:
    st.header("📊 Tariff Results")
    if selected_tool == "independer":
        render_independer_tariff_results(
            st.session_state["results_df"],
            st.session_state["cost_label"]
        )
    elif selected_tool == "energyvergelijk":
        render_energievergelijk_tariff_results(
            st.session_state["results_df"],
            st.session_state["cost_label"]
        )
