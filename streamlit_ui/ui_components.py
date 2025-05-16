import streamlit as st
import pandas as pd

ELEKTRA_LABEL = {
    0: "Grey electricity",
    1: "European green electricity",
    2: "Dutch green electricity",
}
GAS_LABEL = {
    0: "Grey gas",
    1: "Natural gas with CO₂ compensation",
}

EXCLUDE_COLS = {"Description", "Contract Duration", "Stream", "Gas"}

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

def render_tariff_results(df: pd.DataFrame, cost_label: str) -> None:
    if df.empty or not cost_label:
        st.warning("No data returned.")
        return

    df_full = df.copy()

    # Filter columns for the main table
    cols_to_show = [col for col in df_full.columns if col not in EXCLUDE_COLS]
    df_display = df_full[cols_to_show].copy()

    # Render image HTML (for display purposes only)
    if "Logo" in df_display.columns:
        df_display["Logo"] = df_display["Logo"].apply(
            lambda url: f'<img src="{url}" alt="Logo" width="50">' if url else ""
        )

    all_cols = list(df_display.columns)
    all_cols.append("LearnMore")

    # Define widths for columns (you can adjust or make all equal)
    # For example, give Logo smaller width, others normal width, LearnMore small width
    col_widths = []
    for col in all_cols:
        if col == "Logo":
            col_widths.append(3)
        elif col == "LearnMore":
            col_widths.append(2.5)
        else:
            col_widths.append(4)

    # Render headers dynamically (except index column if you want to skip it)
    header_cols = st.columns(col_widths)
    for i, col_name in enumerate(all_cols):
        if col_name == "LearnMore":
            header_cols[i].markdown("🔍")
        else:
            header_cols[i].markdown(f"{col_name}")

    # Render rows dynamically
    for i, row in df_display.iterrows():
        with st.container():
            row_cols = st.columns(col_widths)
            for j, col_name in enumerate(all_cols):
                if col_name == "LearnMore":
                    if row_cols[j].button("Learn more", key=f"learn_more_{i}"):
                        st.session_state["selected_row"] = i
                else:
                    val = row[col_name]
                    if col_name == "Logo":
                        row_cols[j].markdown(val, unsafe_allow_html=True)
                    elif col_name == cost_label:
                        row_cols[j].markdown(f"€{val}")
                    else:
                        row_cols[j].markdown(str(val))

    selected = st.session_state.get("selected_row")
    if selected is not None:
        _render_row_details(df.loc[selected], cost_label)

def _render_row_details(row: pd.Series, cost_label: str) -> None:
    with st.expander(f"Details – {row['Plan name']}", expanded=True):
        col1, col2 = st.columns([1, 2])

        with col1:
            stroom_text = ELEKTRA_LABEL.get(row.get("Stream"), "n/a")
            gas_text = GAS_LABEL.get(row.get("Gas"), "n/a")

            st.markdown(f"**Electricity (Stroom):** {stroom_text}")
            st.markdown(f"**Gas:** {gas_text}")
            st.markdown(f"**Contract Duration:** {row.get('Contract Duration', 'n/a')}")

        with col2:
            st.markdown("### Description")
            if "Description" in row and pd.notnull(row["Description"]):
                st.markdown(row["Description"])
            else:
                st.markdown("No additional information provided.")