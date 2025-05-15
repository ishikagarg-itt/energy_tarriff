from fastapi import FastAPI
from schemas.Tarriff import Tarriff
from fastapi.responses import JSONResponse

app = FastAPI()

response_data = {
    "id": 1973212332,
    "lastUpdateDate": "2025-05-08T14:36:31.243Z",
    "featuredProducts": {
        "labeledProducts": [
            {
                "productId": "10066",
                "labels": [
                    {
                        "shortText": "Goedkoopste variabele",
                        "color": "green",
                        "longDescription": "De verhouding tussen de prijs en wat je er voor terugkrijgt is bij dit product het best. Daarnaast is het het goedkoopste variabele contract in onze vergelijking."
                    }
                ],
                "source": "PersonalisationCandidateHighlighter"
            },
            {
                "productId": "11359",
                "labels": [
                    {
                        "shortText": "Hoge klantwaardering",
                        "color": "purple",
                        "longDescription": "Het beste product met een relatief hoge klantwaardering."
                    }
                ],
                "source": "PersonalisationCandidateHighlighter"
            },
            {
                "productId": "12098",
                "labels": [
                    {
                        "shortText": "Ook interessant",
                        "color": "purple",
                        "longDescription": "De verhouding tussen de prijs van dit contract en wat je er voor terugkrijgt is prima. Maar er zijn 2 betere energiedeals."
                    }
                ],
                "source": "PersonalisationCandidateHighlighter"
            }
        ],
        "highlightedProducts": [
            {
                "productId": "10066",
                "sortIndex": 0
            },
            {
                "productId": "11359",
                "sortIndex": 1
            },
            {
                "productId": "12098",
                "sortIndex": 2
            }
        ],
        "personalizationDiagnostics": {
            "usedStrategyName": "PrimaryPersonalizationStrategy - Energy",
            "status": 201
        }
    },
    "products": [
        {
            "id": 10066,
            "naam": "Flexcontract Nederlandse Groene Stroom en CO2-gecompenseerd Gas",
            "productLabel": "1 maand",
            "maatschappijId": 78,
            "isRetention": False,
            "isClosable": True,
            "contractSoort": "ElektraEnGas",
            "contractKind": "Variabel",
            "elektraTariefType": "Variabel",
            "gasTariefType": "Variabel",
            "looptijd": "VrijOpzegbaar",
            "contractDurationMonths": 1,
            "looptijdText": "1 maand",
            "smartMeterRequired": False,
            "toonAkkoordSlimmeMeter": False,
            "inzichtelijk": True,
            "helptBesparen": True,
            "overigeDiensten": True,
            "additionalConsentQuestion": "",
            "actieToelichting": "",
            "elektraGroenIndex": 2,
            "gasGroenIndex": 1,
            "priceQualityScore": -11.6826889458,
            "priceQualityScoreWithDiscount": -11.6826889458,
            "bestChoiceIndex": 0,
            "bestChoiceIndexWithDiscount": 0,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 76.77,
                    "termExclDiscountInclTaxReduction": 23.83,
                    "termInclDiscountExclTaxReduction": 76.77,
                    "termInclDiscountInclTaxReduction": 23.83
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 921.19,
                    "termExclDiscountInclTaxReduction": 286.00,
                    "termInclDiscountExclTaxReduction": 921.19,
                    "termInclDiscountInclTaxReduction": 286.00
                }
            },
            "aandachtspunten": [],
            "scoreOverview": {
                "averageScore": 7.1,
                "numberOfReviews": 155,
                "hasEnoughReviewsToShow": True
            },
            "prijsdetails": {
                "stroomLeveringstarief": 0.0,
                "stroomLeveringstariefHoog": 0.22995000,
                "stroomLeveringstariefLaag": 0.22995000,
                "stroomVasteLeveringskosten": 7.00000000,
                "stroomTerugleververgoeding": 0.01653000,
                "stroomTerugleververgoedingHoog": 0.01653000,
                "stroomTerugleververgoedingLaag": 0.01653000,
                "stroomVasteTerugleveringskosten": 0.0,
                "stroomDynamischLeveringstarief": 0.0,
                "stroomInkoopvergoeding": 0.0,
                "electricityFeedInCostPerKWh": 0.0,
                "gasLeveringstarief": 1.12195500,
                "gasVasteLeveringskosten": 7.00000000,
                "gasDynamischLeveringstarief": 0.0,
                "gasInkoopvergoeding": 0.0,
                "extraKosten": 0.0,
                "electricityTotalAnnualCost": -74.77450000,
                "gasTotalAnnualCost": 360.77399500
            }
        },
        {
            "id": 12098,
            "naam": "Nederlandse Groene stroom en Gas met CO2 compensatie Flex",
            "productLabel": "1 maand",
            "maatschappijId": 70,
            "isRetention": False,
            "isClosable": True,
            "contractSoort": "ElektraEnGas",
            "contractKind": "Variabel",
            "elektraTariefType": "Variabel",
            "gasTariefType": "Variabel",
            "looptijd": "VrijOpzegbaar",
            "contractDurationMonths": 1,
            "looptijdText": "1 maand",
            "bonusTekstLang": "",
            "bonusTekst": "",
            "discountAmount": 0.00000000,
            "smartMeterRequired": False,
            "toonAkkoordSlimmeMeter": False,
            "inzichtelijk": True,
            "helptBesparen": True,
            "overigeDiensten": True,
            "additionalConsentQuestion": "",
            "actieToelichting": "",
            "elektraGroenIndex": 2,
            "gasGroenIndex": 1,
            "priceQualityScore": -16.2809883656,
            "priceQualityScoreWithDiscount": -16.2809883656,
            "bestChoiceIndex": 2,
            "bestChoiceIndexWithDiscount": 2,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 81.56,
                    "termExclDiscountInclTaxReduction": 28.62,
                    "termInclDiscountExclTaxReduction": 81.56,
                    "termInclDiscountInclTaxReduction": 28.62
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 978.69,
                    "termExclDiscountInclTaxReduction": 343.50,
                    "termInclDiscountExclTaxReduction": 978.69,
                    "termInclDiscountInclTaxReduction": 343.50
                }
            },
            "aandachtspunten": [],
            "scoreOverview": {
                "averageScore": 7.6,
                "numberOfReviews": 27,
                "hasEnoughReviewsToShow": True
            },
            "prijsdetails": {
                "stroomLeveringstarief": 0.0,
                "stroomLeveringstariefHoog": 0.22821500,
                "stroomLeveringstariefLaag": 0.24572800,
                "stroomVasteLeveringskosten": 8.57083875,
                "stroomTerugleververgoeding": 0.02458400,
                "stroomTerugleververgoedingHoog": 0.02458400,
                "stroomTerugleververgoedingLaag": 0.02458400,
                "stroomVasteTerugleveringskosten": 0.0,
                "stroomDynamischLeveringstarief": 0.0,
                "stroomInkoopvergoeding": 0.0,
                "electricityFeedInCostPerKWh": 0.0,
                "gasLeveringstarief": 1.33081200,
                "gasVasteLeveringskosten": 8.57083875,
                "gasDynamischLeveringstarief": 0.0,
                "gasInkoopvergoeding": 0.0,
                "extraKosten": 0.0,
                "electricityTotalAnnualCost": -54.71457100,
                "gasTotalAnnualCost": 398.21233300
            }
        },
        {
            "id": 10079,
            "naam": "Nederlandse Windstroom & Aardgas met Natuur voor Morgen Variabel",
            "productLabel": "1 maand",
            "maatschappijId": 17,
            "isRetention": False,
            "isClosable": True,
            "contractSoort": "ElektraEnGas",
            "contractKind": "Variabel",
            "elektraTariefType": "Variabel",
            "gasTariefType": "Variabel",
            "looptijd": "VrijOpzegbaar",
            "contractDurationMonths": 1,
            "looptijdText": "Onbepaalde tijd",
            "smartMeterRequired": False,
            "toonAkkoordSlimmeMeter": False,
            "inzichtelijk": True,
            "helptBesparen": True,
            "overigeDiensten": True,
            "additionalConsentQuestion": "",
            "actieToelichting": "",
            "elektraGroenIndex": 2,
            "gasGroenIndex": 1,
            "priceQualityScore": -17.3470881722,
            "priceQualityScoreWithDiscount": -17.3470881722,
            "bestChoiceIndex": 3,
            "bestChoiceIndexWithDiscount": 3,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 82.68,
                    "termExclDiscountInclTaxReduction": 29.75,
                    "termInclDiscountExclTaxReduction": 82.68,
                    "termInclDiscountInclTaxReduction": 29.75
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 992.14,
                    "termExclDiscountInclTaxReduction": 356.95,
                    "termInclDiscountExclTaxReduction": 992.14,
                    "termInclDiscountInclTaxReduction": 356.95
                }
            },
            "aandachtspunten": [
                "Je betaalt de tarieven die je hier ziet voor één maand vanaf het begin van de levering. Na deze datum geldt een contract voor onbepaalde tijd met een opzegtermijn van 30 dagen. De op dat moment geldende variabele tarieven voor groene stroom en voor bosgecompenseerd gas zijn dan van toepassing.  Greenchoice zal uiterlijk 30 dagen voordat deze nieuwe tarieven ingaan, je hierover per e-mail informeren. Het contract is zonder boete op ieder moment opzegbaar."
            ],
            "scoreOverview": {
                "averageScore": 7.7,
                "numberOfReviews": 2180,
                "hasEnoughReviewsToShow": True
            },
            "prijsdetails": {
                "stroomLeveringstarief": 0.0,
                "stroomLeveringstariefHoog": 0.24643000,
                "stroomLeveringstariefLaag": 0.25853000,
                "stroomVasteLeveringskosten": 9.32000000,
                "stroomTerugleververgoeding": 0.16000000,
                "stroomTerugleververgoedingHoog": 0.16000000,
                "stroomTerugleververgoedingLaag": 0.16000000,
                "stroomVasteTerugleveringskosten": 0.0,
                "stroomDynamischLeveringstarief": 0.0,
                "stroomInkoopvergoeding": 0.0,
                "electricityFeedInCostPerKWh": 0.0,
                "gasLeveringstarief": 1.41882000,
                "gasVasteLeveringskosten": 8.188333333333333333333333333,
                "gasDynamischLeveringstarief": 0.0,
                "gasInkoopvergoeding": 0.0,
                "extraKosten": 0.0,
                "electricityTotalAnnualCost": -44.50750000,
                "gasTotalAnnualCost": 401.45498000
            }
        },
        {
            "id": 11359,
            "naam": "100% Nederlandse Zonnestroom en Gas met CO2 compensatie Variabel Energiezuinig",
            "productLabel": "1 maand",
            "maatschappijId": 45,
            "isRetention": False,
            "isClosable": True,
            "contractSoort": "ElektraEnGas",
            "contractKind": "Variabel",
            "elektraTariefType": "Variabel",
            "gasTariefType": "Variabel",
            "looptijd": "VrijOpzegbaar",
            "contractDurationMonths": 1,
            "looptijdText": "1 maand",
            "smartMeterRequired": False,
            "toonAkkoordSlimmeMeter": False,
            "inzichtelijk": True,
            "helptBesparen": True,
            "overigeDiensten": True,
            "additionalConsentQuestion": "",
            "actieToelichting": "",
            "elektraGroenIndex": 2,
            "gasGroenIndex": 1,
            "priceQualityScore": -13.2109883656,
            "priceQualityScoreWithDiscount": -13.2109883656,
            "bestChoiceIndex": 1,
            "bestChoiceIndexWithDiscount": 1,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 78.48,
                    "termExclDiscountInclTaxReduction": 25.55,
                    "termInclDiscountExclTaxReduction": 78.48,
                    "termInclDiscountInclTaxReduction": 25.55
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 941.77,
                    "termExclDiscountInclTaxReduction": 306.58,
                    "termInclDiscountExclTaxReduction": 941.77,
                    "termInclDiscountInclTaxReduction": 306.58
                }
            },
            "aandachtspunten": [],
            "scoreOverview": {
                "averageScore": 7.6,
                "numberOfReviews": 77,
                "hasEnoughReviewsToShow": True
            },
            "prijsdetails": {
                "stroomLeveringstarief": 0.0,
                "stroomLeveringstariefHoog": 0.22474200,
                "stroomLeveringstariefLaag": 0.22353200,
                "stroomVasteLeveringskosten": 8.00000000,
                "stroomTerugleververgoeding": 0.13400000,
                "stroomTerugleververgoedingHoog": 0.13400000,
                "stroomTerugleververgoedingLaag": 0.13400000,
                "stroomVasteTerugleveringskosten": 0.0,
                "stroomDynamischLeveringstarief": 0.0,
                "stroomInkoopvergoeding": 0.0,
                "electricityFeedInCostPerKWh": 0.0,
                "gasLeveringstarief": 1.15731300,
                "gasVasteLeveringskosten": 7.50000000,
                "gasDynamischLeveringstarief": 0.0,
                "gasInkoopvergoeding": 0.0,
                "extraKosten": 0.0,
                "electricityTotalAnnualCost": -63.33760000,
                "gasTotalAnnualCost": 369.92085700
            }
        }
    ],
    "notApplicableProducts": []
}

@app.post("/tarriffs")
def get_energy_tarriff_data(tarriff: Tarriff ):
    return JSONResponse(content=response_data)
