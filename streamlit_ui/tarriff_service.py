import pandas as pd
import requests

LOGO_URLS = {
    "Eneco": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/eneco.svg",
    "Vattenfall": "//www.independer-static.nl/images/logos/maatschappijen/thumb/vattenfall.svg",
    "Mega": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/mega.svg",
    "Frank Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/frank-energie.svg",
    "Free Name": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/vrijopnaam.svg",
    "At | New Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/om-nieuwe-energie.svg",
    "Greenchoice": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/greenchoice.svg",
    "Budget Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/budget-energie.svg",
    "Clean Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/clean-energy.svg",
    "Vandebron": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/vandebron.svg",
    "United Consumers": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/united-consumers.svg",
    "Cool Blue Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/coolblue-energie.svg",
    "Oxxio": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/oxxio.svg",
    "Pure Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/pure-energie.svg",
    "Unive via Greenchoice": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/unive-via-greenchoice.svg",
    "Engie": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/engie.svg",
    "Innova Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/innova-energie.svg",
    "Just Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/gewoon-energie.svg",
    "Powerpeers": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/powerpeers.svg",
    "Next Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/nextenergy.svg",
    "Tibber": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/tibber.svg",
    "North Energy": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/noord-energie.svg",
    "Solar Plan": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/zonneplan.svg",
    "Hello Current": "https://www.independer-static.nl/images/logos/maatschappijen/thumb/hallostroom.svg"
}

def build_verbruik_data(gas, dal, piek, has_solar, feed_in_norm, feed_in_offpeak):
    data = {
        "gasverbruik": int(gas),
        "meterSoort": 2,
        "elektriciteitverbruikDubbelMeter": {
            "verbruikDal": int(dal),
            "verbruikPiek": int(piek)
        }
    }
    if has_solar:
        data["elektriciteitverbruikDubbelMeter"]["opwekkingDal"] = int(feed_in_norm or 0)
        data["elektriciteitverbruikDubbelMeter"]["opwekkingPiek"] = int(feed_in_offpeak or 0)
    return data

def build_independer_request_body(postcode, huisnummer, contract_kind, tarriff_period, show_tariff_period, verbruik_data):
    request_body = {
        "contractWensen": {
            "contractSoort": "ElektraEnGas",
            "doelgroep": 1,
            "extraBiedtDiensten": False,
            "extraHelptMetBesparen": False,
            "extraHelptMetInzichtInGebruik": False,
            "hasSmartMeter": True,
            "stroomGroenheid": 1,
            "contractKind": contract_kind,
        },
        "adres": {
            "postcode": postcode,
            "huisnummer": int(huisnummer),
            "huisnummertoevoeging": ""
        },
        "verbruik": verbruik_data,
        "creditDiscount": True
    }
    if show_tariff_period:
        request_body["contractWensen"]["tariffFixedPeriod"] = tarriff_period
    
    return request_body

def extract_and_format_independer_data(data, cost_type, contract_kind, has_solar):
    cost_column = (
        'contractTermAmounts_monthlyTermAmounts_termInclDiscountInclTaxReduction'
        if cost_type == "Monthly Cost"
        else 'contractTermAmounts_yearlyTermAmounts_termInclDiscountInclTaxReduction'
    )
    cost_label = "Monthly Cost (€)" if cost_type == "Monthly Cost" else "Yearly Cost (€)"

    df = pd.json_normalize(data, sep='_')

    if contract_kind in ("Vast", "Variabel"):
        tariff_columns = {
            "prijsdetails_stroomLeveringstariefHoog":  "Electricity Peak Tariff (High) per kWh (€)",
            "prijsdetails_stroomLeveringstariefLaag":  "Electricity Off-peak Tariff (Low) per kWh (€)",
            "prijsdetails_gasLeveringstarief": "Gas Tariff per m³ (€)"
        }
        if has_solar:
            tariff_columns["prijsdetails_stroomInkoopvergoeding"] = "Purchase fee per kWh (€)"

    elif contract_kind == "Dynamisch":
        tariff_columns = {
            "prijsdetails_stroomDynamischLeveringstarief": "Dynamic Electricity Tariff per kWh (€)",
            "prijsdetails_gasDynamischLeveringstarief": "Dynamic Gas Tariff per m³ (€)",
        }
        if has_solar:
            tariff_columns["prijsdetails_stroomInkoopvergoeding"] = "Purchase fee per kWh (€)"
            tariff_columns["prijsdetails_electricityFeedInCostPerKWh"] = "Feed-in cost per kWh (€)"
            tariff_columns["prijsdetails_gasInkoopvergoeding"] = "Purchase fee per m³ (€)"
    else:
        tariff_columns = {}

    base_columns = {
        'vendorName': 'Vendor Name',
        'naam': 'Plan name',
        'contractKind': 'Contract Type',
        cost_column: cost_label,
        'elektraGroenIndex': 'Stream',
        'gasGroenIndex': 'Gas',
        'productLabel': 'Contract Duration',
        'aandachtspunten': 'Description',
        'prijsdetails_stroomVasteLeveringskosten': 'Electricity Fixed delivery cost per month (€)',
        'prijsdetails_gasVasteLeveringskosten': 'Gas Fixed delivery cost per month (€)'
    }

    rename_map = {**base_columns, **tariff_columns}

    if "discountAmountPerYear" in df.columns:
        rename_map["discountAmountPerYear"] = "Discount per Year (€)"

    selected_columns = list(rename_map.keys())

    df = df[[col for col in selected_columns if col in df.columns]]
    df.rename(columns=rename_map, inplace=True)
    df["Logo"] = df["Vendor Name"].map(LOGO_URLS).fillna("")
    final_columns = ["Logo"] + [col for col in df.columns if col != "Logo"]
    df = df[final_columns]

    return df, cost_label

def fetch_independer_tariffs(postcode, huisnummer, contract_kind, show_tarriff_period, gas, dal, piek,
                  has_solar, feed_in_norm=None, feed_in_offpeak=None, cost_type="Monthly Cost", tarriff_period=None):
    try:
        verbruik_data = build_verbruik_data(gas, dal, piek, has_solar, feed_in_norm, feed_in_offpeak)
        request_body = build_independer_request_body(postcode, huisnummer, contract_kind, tarriff_period, 
                                          show_tarriff_period, verbruik_data)

        res = requests.post("https://energy-tarriff.onrender.com/independer-energy-tarriffs/", json=request_body)
        res.raise_for_status()
        data = res.json()

        return extract_and_format_independer_data(data, cost_type, contract_kind, has_solar)

    except Exception as e:
        return pd.DataFrame([{"Error": str(e)}]), None

def build_energievergelijk_request_body(postcode, huisnummer, contract_kind, tarriff_period, show_tariff_period, cost_type, durability):
    request_body = {"lang":"NL", "zipcode": postcode, "housenumber": huisnummer}
    if cost_type == "Monthly Cost":
        request_body["price_rate"] = "m"
    else:
        request_body["price_rate"] = "y"
    if contract_kind == "Vast" and tarriff_period == "OneYear":
        request_body["filters"] = ["2:16"]
    elif contract_kind == "Vast" and tarriff_period == "ThreeYear":
        request_body["filters"] = ["2:7"]
    elif contract_kind == "Variabel":
        request_body["filters"] = ["2:4"]
    elif contract_kind == "Dynamisch":
        request_body["filters"] = ["2:6"]
    elif contract_kind == "Best Contracts":
        request_body["filters"] = ["2:5"]

    if durability == "No Preference":
           request_body.setdefault("filters", []).append("1:1")
    else:
        request_body.setdefault("filters", []).append("1:2")
    return request_body

def extract_and_format_energievergelijk_data(data, cost_type):
    cost_label = "Monthly Cost (€)" if cost_type == "Monthly Cost" else "Yearly Cost (€)"

    df = pd.json_normalize(data, sep='_')

    if 'summary' in df.columns:
        df['summary'] = df['summary'].apply(lambda x: x[0] if isinstance(x, list) and x else None)


    base_columns = {
        'provider_name': 'Vendor Name',
        'provider_logo': 'Vendor Logo',
        'pricing_display_total': 'Total Price',
        'name': 'Contract Type',
        'pricing_details_power_tariff': 'Electricity tarriff per kWh (€)',
        'pricing_details_gas_tariff': 'Gas tarriff per m³ (€)',
        'summary': 'Energy Type',
        'pricing_details_discount_display_sum': 'Discount per Year',
        'pricing_details_discount_type': 'Discount Type',
        'terms_type': 'Term',
        'terms_end': 'Term End'
    }

    rename_map = {**base_columns}
    selected_columns = list(rename_map.keys())

    df = df[[col for col in selected_columns if col in df.columns]]
    df.rename(columns=rename_map, inplace=True)

    return df, cost_label

def fetch_energievergelijk_tariffs(postcode, huisnummer, contract_kind, show_tarriff_period, durability, cost_type="Monthly Cost", tarriff_period=None):
    try:
        request_body = build_energievergelijk_request_body(postcode, huisnummer, contract_kind, tarriff_period, 
                                          show_tarriff_period, cost_type, durability)

        res = requests.post("https://energy-tarriff.onrender.com/energievergelijk-energy-tarriffs/", json=request_body)
        res.raise_for_status()
        data = res.json()

        return extract_and_format_energievergelijk_data(data, cost_type)

    except Exception as e:
        return pd.DataFrame([{"Error": str(e)}]), None
