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

EXCLUDE_INDEPENDER_COLS = {"Description", "Contract Duration", "Stream", "Gas", "Discount per Year (€)", 
                "Electricity Fixed delivery cost per month (€)", "Gas Fixed delivery cost per month (€)"}

EXCLUDE_ENERGIEVERGELIJK_COLS = {"Energy Type", "Term", "Term End", "Discount per Year", "Discount Type", }

def render_independer_filters():
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

def render_energievergelijk_filters():
    """Render all user input filters and return values as a dictionary."""
    st.session_state.setdefault("has_solar", False)

    address_data = _render_address_inputs()
    contract_data = _render_energievergelijk_contract_options()
    submit = st.button("Submit")

    return {
        **address_data,
        **contract_data,
        "submit": submit
    }

def _render_address_inputs():
    col1, col2, _ = st.columns([2, 2, 1])
    with col1:
        postcode = st.text_input("Postcode")
    with col2:
        huisnummer = st.text_input("Huisnummer")
    return {"postcode": postcode, "huisnummer": huisnummer}


def _render_usage_inputs():
    col1, col2, col3 = st.columns(3)
    with col1:
        piek = _render_labeled_input("Electricity Current Normal (Peak)", "Kwh")
    with col2:
        dal = _render_labeled_input("Electricity Stream valley (Off-peak)", "Kwh")
    with col3:
        gas = _render_labeled_input("Gas", "m³")
    return {"piek": piek, "dal": dal, "gas": gas}


def _render_contract_options():
    col1, col2, col3 = st.columns(3)
    with col1:
        contract_kind = st.selectbox("Contract Type", ["Vast", "Variabel", "Dynamisch"])
    with col2:
        cost_type = st.selectbox("Show Cost As", ["Monthly Cost", "Yearly Cost"])
    with col3:
        tarriff_period = None
        if contract_kind == "Vast":
            tarriff_period = st.selectbox("Tariff Period", ["OneYear", "TwoYear", "ThreeYear"])

    return {
        "contract_kind": contract_kind,
        "cost_type": cost_type,
        "show_tarriff_period": contract_kind == "Vast",
        "tarriff_period": tarriff_period
    }

def _render_energievergelijk_contract_options():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        contract_kind = st.selectbox("Contract Type", ["Vast", "Variabel", "Dynamisch"])
    with col2:
        cost_type = st.selectbox("Show Cost As", ["Monthly Cost", "Yearly Cost"])
    with col3:
        tarriff_period = None
        if contract_kind == "Vast":
            tarriff_period = st.selectbox("Tariff Period", ["OneYear", "ThreeYear"])
    with col4:
        durability = st.selectbox("Durability", ["No Preference", "100% green from NL"])

    return {
        "contract_kind": contract_kind,
        "cost_type": cost_type,
        "show_tarriff_period": contract_kind == "Vast",
        "tarriff_period": tarriff_period,
        "durability": durability
    }


def _render_solar_inputs():
    st.session_state["has_solar"] = st.toggle("Do you have solar panels?", value=st.session_state["has_solar"])
    feed_in_norm = feed_in_offpeak = None
    if st.session_state["has_solar"]:
        st.markdown("### ☀️ Solar Panel Feed-in")
        col1, col2 = st.columns(2)
        with col1:
            feed_in_norm = _render_labeled_input("Feed-in normal", "Kwh", key="norm")
        with col2:
            feed_in_offpeak = _render_labeled_input("Off-peak feed-in", "Kwh", key="dal")
    return {
        "has_solar": st.session_state["has_solar"],
        "feed_in_norm": feed_in_norm,
        "feed_in_offpeak": feed_in_offpeak
    }


def _render_labeled_input(label, unit, key=None):
    col1, col2 = st.columns([4, 1])
    with col1:
        value = st.text_input(label, key=key) if key else st.text_input(label)
    with col2:
        st.markdown(unit)
    return value

def render_independer_tariff_results(df: pd.DataFrame, cost_label: str) -> None:
    if df.empty or not cost_label:
        st.warning("No data returned.")
        return

    df_full = df.copy()

    cols_to_show = [col for col in df_full.columns if col not in EXCLUDE_INDEPENDER_COLS]
    df_display = df_full[cols_to_show].copy()

    if "Logo" in df_display.columns:
        df_display["Logo"] = df_display["Logo"].apply(
            lambda url: f'<img src="{url}" alt="Logo" width="50">' if url else ""
        )

    all_cols = list(df_display.columns)
    all_cols.append("ShowMore")

    col_widths = []
    for col in all_cols:
        if col == "Logo":
            col_widths.append(3)
        elif col == "ShowMore":
            col_widths.append(2.5)
        else:
            col_widths.append(4)

    header_cols = st.columns(col_widths)
    for i, col_name in enumerate(all_cols):
        if col_name == "ShowMore":
            header_cols[i].markdown("🔍")
        else:
            header_cols[i].markdown(f"{col_name}")

    for i, row in df_display.iterrows():
        with st.container():
            row_cols = st.columns(col_widths)
            for j, col_name in enumerate(all_cols):
                if col_name == "ShowMore":
                    if row_cols[j].button("Show more", key=f"show_more_{i}"):
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
        _render_independer_row_details(df.loc[selected], cost_label)

def _render_independer_row_details(row: pd.Series, cost_label: str) -> None:
    with st.expander(f"Details – {row['Plan name']}", expanded=True):
        col1, col2 = st.columns([1, 2])

        with col1:
            stroom_text = ELEKTRA_LABEL.get(row.get("Stream"), "n/a")
            gas_text = GAS_LABEL.get(row.get("Gas"), "n/a")

            st.markdown(f"**Electricity (Stroom):** {stroom_text}")
            st.markdown(f"**Gas:** {gas_text}")
            st.markdown(f"**Contract Duration:** {row.get("Contract Duration", "n/a")}")
            discount = row.get("Discount per Year (€)")
            if discount is not None and pd.notna(discount):
                st.markdown(f"**Discount:** {discount}")


        with col2:
            description = row.get("Description")
            if isinstance(description, list) and len(description) > 0:
                st.markdown("**Description**")
                for line in description:
                    st.markdown(f"{line}")
            st.markdown(f"**Electricity Fixed Delivery Cost :** {row.get("Electricity Fixed delivery cost per month (€)", "n/a")}")
            st.markdown(f"**Gas Fixed Delivery Cost:** {row.get("Gas Fixed delivery cost per month (€)", "n/a")}")

def render_energievergelijk_tariff_results(df: pd.DataFrame, cost_label: str) -> None:
    if df.empty or not cost_label:
        st.warning("No data returned.")
        return

    df_full = df.copy()

    cols_to_show = [col for col in df_full.columns if col not in EXCLUDE_ENERGIEVERGELIJK_COLS]
    df_display = df_full[cols_to_show].copy()

    if "Vendor Logo" in df_display.columns:
        df_display["Vendor Logo"] = df_display["Vendor Logo"].apply(
            lambda url: f'<img src="{url}" alt="Logo" width="90">' if url else ""
        )

    all_cols = list(df_display.columns)
    all_cols.append("ShowMore")

    col_widths = []
    for col in all_cols:
        if col == "Vendor Logo":
            col_widths.append(4)
        elif col == "ShowMore":
            col_widths.append(2.5)
        else:
            col_widths.append(4)

    header_cols = st.columns(col_widths)
    for i, col_name in enumerate(all_cols):
        if col_name == "ShowMore":
            header_cols[i].markdown("🔍")
        else:
            header_cols[i].markdown(f"{col_name}")

    for i, row in df_display.iterrows():
        with st.container():
            row_cols = st.columns(col_widths)
            for j, col_name in enumerate(all_cols):
                if col_name == "ShowMore":
                    if row_cols[j].button("Show more", key=f"show_more_{i}"):
                        st.session_state["selected_row"] = i
                else:
                    val = row[col_name]
                    if col_name == "Vendor Logo":
                        row_cols[j].markdown(val, unsafe_allow_html=True)
                    elif col_name == cost_label:
                        row_cols[j].markdown(f"€{val}")
                    else:
                        row_cols[j].markdown(str(val))

    selected = st.session_state.get("selected_row")
    if selected is not None:
        _render_energievergelijk_row_details(df.loc[selected], cost_label)

def _render_energievergelijk_row_details(row: pd.Series, cost_label: str) -> None:
    with st.expander(f"Details – {row['Contract Type']}", expanded=True):
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(f"**Energy Type:** {row.get("Energy Type", "n/a")["description"]}")
            discount = row.get("Discount per Year")
            discountType = row.get("Discount Type")
            if discount is not None and pd.notna(discount) and discount != 0:
                if discountType == "PRICE":
                    st.markdown(f"**Discount:** €{discount}")
                else:
                    st.markdown(f"**Discount:** {discount}%")
        with col2:
            st.markdown(f"**Type :** {row.get("Term", "n/a")}")
            st.markdown(f"**Recite:** {row.get("Term End", "n/a")}")