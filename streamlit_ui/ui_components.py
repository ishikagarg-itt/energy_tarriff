import streamlit as st
import pandas as pd

def render_filters():
    """Render all user input filters and return values as a dictionary."""
    st.session_state.setdefault("has_solar", False)

    address_data = _render_address_inputs()
    usage_data = _render_usage_inputs()
    contract_data = _render_contract_options()
    solar_data = _render_solar_inputs()
    submit = st.button("Submit")

    return {
        **address_data,
        **usage_data,
        **contract_data,
        **solar_data,
        "submit": submit
    }

def _render_address_inputs():
    postcode = st.text_input("Postcode")
    huisnummer = st.text_input("Huisnummer")
    return {"postcode": postcode, "huisnummer": huisnummer}

def _render_usage_inputs():
    piek = _render_labeled_input("Current Normal (Peak)", "Kwh")
    dal = _render_labeled_input("Stream valley (Off-peak)", "Kwh")
    gas = _render_labeled_input("Gas", "m³")
    return {"piek": piek, "dal": dal, "gas": gas}

def _render_contract_options():
    contract_kind = st.selectbox("Contract Type", ["Vast", "Variabel", "Dynamisch"])
    show_tarriff_period = contract_kind == "Vast"
    tarriff_period = None
    if show_tarriff_period:
        tarriff_period = st.selectbox("Tariff Period", ["OneYear", "TwoYear", "ThreeYear"])
    cost_type = st.selectbox("Show Cost As", ["Monthly Cost", "Yearly Cost"])
    result = {
        "contract_kind": contract_kind,
        "cost_type": cost_type,
        "show_tarriff_period": show_tarriff_period,
        "tarriff_period": tarriff_period
    }
    
    return result

def _render_solar_inputs():
    st.session_state["has_solar"] = st.toggle("Do you have solar panels?", value=st.session_state["has_solar"])
    feed_in_norm = feed_in_offpeak = None
    if st.session_state["has_solar"]:
        st.markdown("### ☀️ Solar Panel Feed-in")
        feed_in_norm = _render_labeled_input("Feed-in normal", "Kwh", key="norm")
        feed_in_offpeak = _render_labeled_input("Off-peak feed-in", "Kwh", key="dal")
    return {
        "has_solar": st.session_state["has_solar"],
        "feed_in_norm": feed_in_norm,
        "feed_in_offpeak": feed_in_offpeak
    }

def _render_labeled_input(label, unit, key=None):
    col1, col2 = st.columns([3, 1])
    with col1:
        value = st.text_input(label, key=key) if key else st.text_input(label)
    with col2:
        st.markdown(unit)
    return value

def render_tariff_results(df: pd.DataFrame, cost_label: str):
    """Display the results table"""
    if df.empty or not cost_label:
        st.warning("No data returned.")
        return

    if "Logo" in df.columns:
        df["Logo"] = df["Logo"].apply(
            lambda url: f'<img src="{url}" alt="Logo" width="50">' if url else ""
        )

    _render_contract_section(df)

def _render_contract_section(df: pd.DataFrame):
    html_table = df.to_html(classes="custom-table", escape=False, index=False)
    st.markdown(f"""
    <div class="table-wrapper">
        {html_table}
    </div>
    """, unsafe_allow_html=True)
