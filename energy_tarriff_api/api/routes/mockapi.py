from fastapi import FastAPI
from schemas.Tarriff import Tarriff
from fastapi.responses import JSONResponse

app = FastAPI()

response_data = {
    "id": 1203567943,
    "lastUpdateDate": "2025-05-15T14:28:19.503Z",
    "featuredProducts": {
        "labeledProducts": [
            {
                "productId": "10099",
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
                "productId": "10066",
                "labels": [
                    {
                        "shortText": "Beste Duurzaamheidslabel A",
                        "color": "purple",
                        "longDescription": "Het beste product met duurzaamheid A label."
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
            }
        ],
        "highlightedProducts": [
            {
                "productId": "10099",
                "sortIndex": 0
            },
            {
                "productId": "10066",
                "sortIndex": 1
            },
            {
                "productId": "11359",
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
            "id": 10169,
            "naam": "Particulier variabel Stroom en Gas",
            "productLabel": "1 maand",
            "maatschappijId": 88,
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
            "inzichtelijk": False,
            "helptBesparen": True,
            "overigeDiensten": True,
            "additionalConsentQuestion": "",
            "actieToelichting": "",
            "elektraGroenIndex": 1,
            "gasGroenIndex": 0,
            "priceQualityScore": -19.2719394348,
            "priceQualityScoreWithDiscount": -19.2719394348,
            "bestChoiceIndex": 5,
            "bestChoiceIndexWithDiscount": 6,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 80.12,
                    "termExclDiscountInclTaxReduction": 27.19,
                    "termInclDiscountExclTaxReduction": 80.12,
                    "termInclDiscountInclTaxReduction": 27.19
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 961.44,
                    "termExclDiscountInclTaxReduction": 326.25,
                    "termInclDiscountExclTaxReduction": 961.44,
                    "termInclDiscountInclTaxReduction": 326.25
                }
            },
            "aandachtspunten": [],
            "scoreOverview": {
                "averageScore": 5.8,
                "numberOfReviews": 4,
                "hasEnoughReviewsToShow": False
            },
            "prijsdetails": {
                "stroomLeveringstarief": 0.0,
                "stroomLeveringstariefHoog": 0.25959000,
                "stroomLeveringstariefLaag": 0.26806000,
                "stroomVasteLeveringskosten": 7.56250000,
                "stroomTerugleververgoeding": 0.10330579,
                "stroomTerugleververgoedingHoog": 0.10330579,
                "stroomTerugleververgoedingLaag": 0.10330579,
                "stroomVasteTerugleveringskosten": 0.0,
                "stroomDynamischLeveringstarief": 0.0,
                "stroomInkoopvergoeding": 0.0,
                "electricityFeedInCostPerKWh": 0.0,
                "gasLeveringstarief": 1.38806000,
                "gasVasteLeveringskosten": 7.56250000,
                "gasDynamischLeveringstarief": 0.0,
                "gasInkoopvergoeding": 0.0,
                "extraKosten": 0.0,
                "electricityTotalAnnualCost": -64.95583000,
                "gasTotalAnnualCost": 391.20734000
            }
        },
        {
            "id": 10099,
            "naam": "Variabele Groene stroom & Gas",
            "productLabel": "1 maand",
            "maatschappijId": 86,
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
            "bonusTekst": "€ 122,- korting",
            "discountAmount": 122.00000000,
            "discountAmountPerYear": 122.00,
            "smartMeterRequired": False,
            "toonAkkoordSlimmeMeter": False,
            "inzichtelijk": True,
            "helptBesparen": True,
            "overigeDiensten": True,
            "additionalConsentQuestion": "",
            "actieToelichting": "",
            "elektraGroenIndex": 1,
            "gasGroenIndex": 0,
            "priceQualityScore": -19.9543423802,
            "priceQualityScoreWithDiscount": -9.7843423802,
            "bestChoiceIndex": 6,
            "bestChoiceIndexWithDiscount": 0,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 81.14,
                    "termExclDiscountInclTaxReduction": 28.21,
                    "termInclDiscountExclTaxReduction": 70.98,
                    "termInclDiscountInclTaxReduction": 18.04
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 973.70,
                    "termExclDiscountInclTaxReduction": 338.51,
                    "termInclDiscountExclTaxReduction": 851.70,
                    "termInclDiscountInclTaxReduction": 216.51
                }
            },
            "aandachtspunten": [],
            "scoreOverview": {
                "averageScore": 5.7,
                "numberOfReviews": 119,
                "hasEnoughReviewsToShow": True
            },
            "prijsdetails": {
                "stroomLeveringstarief": 0.0,
                "stroomLeveringstariefHoog": 0.25326000,
                "stroomLeveringstariefLaag": 0.24347000,
                "stroomVasteLeveringskosten": 8.57000000,
                "stroomTerugleververgoeding": 0.05000000,
                "stroomTerugleververgoedingHoog": 0.05000000,
                "stroomTerugleververgoedingLaag": 0.05000000,
                "stroomVasteTerugleveringskosten": 0.0,
                "stroomDynamischLeveringstarief": 0.0,
                "stroomInkoopvergoeding": 0.0,
                "electricityFeedInCostPerKWh": 0.0,
                "gasLeveringstarief": 1.27645000,
                "gasVasteLeveringskosten": 8.57000000,
                "gasDynamischLeveringstarief": 0.0,
                "gasInkoopvergoeding": 0.0,
                "extraKosten": 0.0,
                "electricityTotalAnnualCost": -54.85348000,
                "gasTotalAnnualCost": 393.36405000
            }
        },
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
            "priceQualityScore": -11.6626889458,
            "priceQualityScoreWithDiscount": -11.6626889458,
            "bestChoiceIndex": 0,
            "bestChoiceIndexWithDiscount": 1,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 76.75,
                    "termExclDiscountInclTaxReduction": 23.81,
                    "termInclDiscountExclTaxReduction": 76.75,
                    "termInclDiscountInclTaxReduction": 23.81
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 920.96,
                    "termExclDiscountInclTaxReduction": 285.77,
                    "termInclDiscountExclTaxReduction": 920.96,
                    "termInclDiscountInclTaxReduction": 285.77
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
                "electricityTotalAnnualCost": -75.00445000,
                "gasTotalAnnualCost": 360.77399500
            }
        },
        {
            "id": 11450,
            "naam": "Europese Groene stroom en Europees gas variabel",
            "productLabel": "1 maand",
            "maatschappijId": 4,
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
            "elektraGroenIndex": 1,
            "gasGroenIndex": 0,
            "priceQualityScore": -17.9897396726,
            "priceQualityScoreWithDiscount": -17.9897396726,
            "bestChoiceIndex": 4,
            "bestChoiceIndexWithDiscount": 5,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 80.07,
                    "termExclDiscountInclTaxReduction": 27.14,
                    "termInclDiscountExclTaxReduction": 80.07,
                    "termInclDiscountInclTaxReduction": 27.14
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 960.82,
                    "termExclDiscountInclTaxReduction": 325.63,
                    "termInclDiscountExclTaxReduction": 960.82,
                    "termInclDiscountInclTaxReduction": 325.63
                }
            },
            "aandachtspunten": [
                "Gratis Stroom Cadeau in het weekend: Van 1 juni t/m 30 september 2025 krijgen Budget Energie klanten in het weekend tussen 12.00 en 17.00 uur Gratis Stroom. Activeer de actie in de Budget Thuis app, een slimme meter is verplicht. Lees de actievoorwaarden voor alle details."
            ],
            "scoreOverview": {
                "averageScore": 7.1,
                "numberOfReviews": 2785,
                "hasEnoughReviewsToShow": True
            },
            "prijsdetails": {
                "stroomLeveringstarief": 0.0,
                "stroomLeveringstariefHoog": 0.25963000,
                "stroomLeveringstariefLaag": 0.25830000,
                "stroomVasteLeveringskosten": 7.99000000,
                "stroomTerugleververgoeding": 0.02000000,
                "stroomTerugleververgoedingHoog": 0.02000000,
                "stroomTerugleververgoedingLaag": 0.02000000,
                "stroomVasteTerugleveringskosten": 0.0,
                "stroomDynamischLeveringstarief": 0.0,
                "stroomInkoopvergoeding": 0.0,
                "electricityFeedInCostPerKWh": 0.0,
                "gasLeveringstarief": 1.27432000,
                "gasVasteLeveringskosten": 7.99000000,
                "gasDynamischLeveringstarief": 0.0,
                "gasInkoopvergoeding": 0.0,
                "extraKosten": 0.0,
                "electricityTotalAnnualCost": -60.58667000,
                "gasTotalAnnualCost": 386.21448000
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
            "priceQualityScore": -16.2709883656,
            "priceQualityScoreWithDiscount": -16.2709883656,
            "bestChoiceIndex": 2,
            "bestChoiceIndexWithDiscount": 3,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 81.54,
                    "termExclDiscountInclTaxReduction": 28.61,
                    "termInclDiscountExclTaxReduction": 81.54,
                    "termInclDiscountInclTaxReduction": 28.61
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 978.46,
                    "termExclDiscountInclTaxReduction": 343.27,
                    "termInclDiscountExclTaxReduction": 978.46,
                    "termInclDiscountInclTaxReduction": 343.27
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
                "electricityTotalAnnualCost": -54.94278600,
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
            "priceQualityScore": -17.3270881722,
            "priceQualityScoreWithDiscount": -17.3270881722,
            "bestChoiceIndex": 3,
            "bestChoiceIndexWithDiscount": 4,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 82.66,
                    "termExclDiscountInclTaxReduction": 29.73,
                    "termInclDiscountExclTaxReduction": 82.66,
                    "termInclDiscountInclTaxReduction": 29.73
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 991.89,
                    "termExclDiscountInclTaxReduction": 356.70,
                    "termInclDiscountExclTaxReduction": 991.89,
                    "termInclDiscountInclTaxReduction": 356.70
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
                "electricityTotalAnnualCost": -44.75393000,
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
            "priceQualityScore": -13.1909883656,
            "priceQualityScoreWithDiscount": -13.1909883656,
            "bestChoiceIndex": 1,
            "bestChoiceIndexWithDiscount": 2,
            "contractTermAmounts": {
                "monthlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 78.46,
                    "termExclDiscountInclTaxReduction": 25.53,
                    "termInclDiscountExclTaxReduction": 78.46,
                    "termInclDiscountInclTaxReduction": 25.53
                },
                "yearlyTermAmounts": {
                    "termExclDiscountExclTaxReduction": 941.55,
                    "termExclDiscountInclTaxReduction": 306.36,
                    "termInclDiscountExclTaxReduction": 941.55,
                    "termInclDiscountInclTaxReduction": 306.36
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
                "electricityTotalAnnualCost": -63.56234200,
                "gasTotalAnnualCost": 369.92085700
            }
        }
    ],
    "notApplicableProducts": []
}

@app.post("/tarriffs")
def get_energy_tarriff_data(tarriff: Tarriff ):
    return JSONResponse(content=response_data)
