from fastapi import FastAPI
from energy_tarriff_api.schemas.energievergelijk.Tarriff import Tarriff
from fastapi.responses import JSONResponse

app = FastAPI()

response_data = [
    {
        "id": 4,
        "name": "Dynamisch",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/4",
        "provider": {
            "name": "Zonneplan",
            "logo": "https://api.energievergelijk.nl/storage/logo/zonneplan-logo-green.svg"
        },
        "terms": {
            "type": "Dynamisch: stroomtarieven verschillen per uur, gastarieven per dag",
            "end": "Dagelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,230",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,155",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,000",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PERCENTAGE",
                    "total_sum": 0,
                    "display_sum": 15,
                    "label": "Bespaar 15%",
                    "title": "Bespaar 15% met verbruiksinzicht",
                    "description": "De Zonneplan energiemeter krijg je na overstap gratis in bruikleen en geeft je live energieinzicht. Hiermee bespaar je al snel <strong class=\"marker orange-small\">15%</strong> extra op je verbruik. <a href=\"https://api.energievergelijk.nl/vergelijker/out/4\" target=\"_blank\" rel=\"nofollow\">Check deze deal hier</a>."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 22,
                "description": "Gratis energiemeter",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 47,
                "description": "Inclusief Zonnebonus",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 49,
                "description": "Altijd inzicht in je kosten",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 9679,
            "summary": {
                "total": 163,
                "price": {
                    "number": "8,7",
                    "percentage": 87
                },
                "service": {
                    "number": "8,8",
                    "percentage": 88
                },
                "general": {
                    "number": "8,7",
                    "percentage": 87
                },
                "average": {
                    "number": "8,8",
                    "percentage": 88
                }
            }
        },
        "summary": [
            {
                "description": "Dynamisch",
                "type": "standard"
            },
            {
                "description": "Vrij opzegbaar",
                "type": "standard"
            },
            {
                "description": "Bespaar 15%",
                "type": "discount"
            }
        ]
    },
    {
        "id": 6,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/6",
        "provider": {
            "name": "Oxxio",
            "logo": "https://api.energievergelijk.nl/storage/logo/Oxxio.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -100,
            "display_total": "-100,00",
            "details": {
                "power": {
                    "tariff": "0,247",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,218",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,182",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,172",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 100,
                    "display_sum": 100,
                    "label": "Tot € 100 korting",
                    "title": "Tot € 100 korting",
                    "description": "Nu tijdelijk met <strong class=\"marker orange-small\">€ 100,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota. De hoogte van de korting is afhankelijk van je verbruik en postcode (<a href=\"https://api.energievergelijk.nl/vergelijker/out/6\" target=\"_blank\" rel=\"nofollow\">vul hier in</a>)."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 5,
                "description": "100% Europese windstroom",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 23,
                "description": "Onderdeel van Eneco",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 511,
            "summary": {
                "total": 207,
                "price": {
                    "number": "7,2",
                    "percentage": 72
                },
                "service": {
                    "number": "7,2",
                    "percentage": 72
                },
                "general": {
                    "number": "7,3",
                    "percentage": 73
                },
                "average": {
                    "number": "7,2",
                    "percentage": 72
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            },
            {
                "description": "Tot € 100 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 9,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/9",
        "provider": {
            "name": "Vattenfall",
            "logo": "https://api.energievergelijk.nl/storage/logo/Vattenfall-logo.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,290",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,245",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,168",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "€ 0 korting",
                    "title": "€ 0 korting",
                    "description": "Nu met eenmalig <strong class=\"marker orange-small\">€ 0,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota. Claim je korting <a href=\"https://api.energievergelijk.nl/vergelijker/out/9\" target=\"_blank\" rel=\"nofollow\">hier</a>."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 1,
                "description": "Al 2 miljoen klanten",
                "description_long": "",
                "icon": "plus-compare"
            },
            {
                "id": 11,
                "description": "Persoonlijk bespaaradvies",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 12,
                "description": "Goed bereikbare klantenservice",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 461,
            "summary": {
                "total": 976,
                "price": {
                    "number": "7,7",
                    "percentage": 77
                },
                "service": {
                    "number": "8,1",
                    "percentage": 81
                },
                "general": {
                    "number": "8,0",
                    "percentage": 80
                },
                "average": {
                    "number": "7,9",
                    "percentage": 79
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 10,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/10",
        "provider": {
            "name": "Vattenfall",
            "logo": "https://api.energievergelijk.nl/storage/logo/Vattenfall-logo.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,327",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,394",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,168",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 1,
                "description": "Al 2 miljoen klanten",
                "description_long": "",
                "icon": "plus-compare"
            },
            {
                "id": 4,
                "description": "Vast termijnbedrag",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 6,
                "description": "100% groene stroom en gas",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 461,
            "summary": {
                "total": 976,
                "price": {
                    "number": "7,7",
                    "percentage": 77
                },
                "service": {
                    "number": "8,1",
                    "percentage": 81
                },
                "general": {
                    "number": "8,0",
                    "percentage": 80
                },
                "average": {
                    "number": "7,9",
                    "percentage": 79
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 13,
        "name": "Variabel",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/13",
        "provider": {
            "name": "Essent",
            "logo": "https://api.energievergelijk.nl/storage/logo/Essent.svg"
        },
        "terms": {
            "type": "Variabel: tarieven wijzigen elke drie maanden of vaker",
            "end": "Maandelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,272",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,392",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,055",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 14,
                "description": "Al 2,5 miljoen klanten",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 15,
                "description": "Groene stroom",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 466,
            "summary": {
                "total": 1064,
                "price": {
                    "number": "8,2",
                    "percentage": 82
                },
                "service": {
                    "number": "8,4",
                    "percentage": 84
                },
                "general": {
                    "number": "8,5",
                    "percentage": 85
                },
                "average": {
                    "number": "8,4",
                    "percentage": 84
                }
            }
        },
        "summary": [
            {
                "description": "Variabel",
                "type": "standard"
            },
            {
                "description": "Maandelijks opzegbaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 14,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": ""
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/14",
        "provider": {
            "name": "BudgetEnergie",
            "logo": "https://api.energievergelijk.nl/storage/logo/Budget-Energie.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -100,
            "display_total": "-100,00",
            "details": {
                "power": {
                    "tariff": "0,247",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,220",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,020",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 100,
                    "display_sum": 100,
                    "label": "Tot € 100 korting",
                    "title": "Tot € 100 korting",
                    "description": "Nu eenmalig tot <strong class=\"marker orange-small\">€ 100,-</strong> bonus. Dit bedrag krijg je als extra korting op je jaarnota. De hoogte van de korting is afhankelijk van je verbruik en postcode (<a href=\"https://api.energievergelijk.nl/vergelijker/out/14\" target=\"_blank\" rel=\"nofollow\">vul hier in</a>)."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 9,
                "description": "Al 1,2 miljoen klanten",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 19,
                "description": "100% groene stroom",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 50,
                "description": "Gratis stroom in het weekend",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 509,
            "summary": {
                "total": 617,
                "price": {
                    "number": "8,3",
                    "percentage": 83
                },
                "service": {
                    "number": "7,9",
                    "percentage": 79
                },
                "general": {
                    "number": "8,1",
                    "percentage": 81
                },
                "average": {
                    "number": "8,1",
                    "percentage": 81
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            },
            {
                "description": "Tot € 100 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 15,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/15",
        "provider": {
            "name": "BudgetEnergie",
            "logo": "https://api.energievergelijk.nl/storage/logo/Budget-Energie.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -18.333333333333332,
            "display_total": "-18,33",
            "details": {
                "power": {
                    "tariff": "0,238",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,289",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,020",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 18.333333333333332,
                    "display_sum": 55,
                    "label": "Tot € 55 korting",
                    "title": "Tot € 55 korting",
                    "description": "Nu tijdelijk tot <strong class=\"marker orange-small\">€ 55,-</strong> bonus. Dit bedrag krijg je verdeeld over drie jaar bij iedere jaarrekening. De hoogte van de korting is afhankelijk van je verbruik en postcode (<a href=\"https://api.energievergelijk.nl/vergelijker/out/15\" target=\"_blank\" rel=\"nofollow\">vul hier in</a>)."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 9,
                "description": "Al 1,2 miljoen klanten",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 10,
                "description": "Heldere energie-app",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 50,
                "description": "Gratis stroom in het weekend",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 509,
            "summary": {
                "total": 617,
                "price": {
                    "number": "8,3",
                    "percentage": 83
                },
                "service": {
                    "number": "7,9",
                    "percentage": 79
                },
                "general": {
                    "number": "8,1",
                    "percentage": 81
                },
                "average": {
                    "number": "8,1",
                    "percentage": 81
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            },
            {
                "description": "Tot € 55 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 16,
        "name": "Variabel",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/16",
        "provider": {
            "name": "BudgetEnergie",
            "logo": "https://api.energievergelijk.nl/storage/logo/Budget-Energie.svg"
        },
        "terms": {
            "type": "Variabel: tarieven wijzigen elke drie maanden of vaker",
            "end": "Maandelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,259",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,274",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,020",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 9,
                "description": "Al 1,2 miljoen klanten",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 10,
                "description": "Heldere energie-app",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 509,
            "summary": {
                "total": 617,
                "price": {
                    "number": "8,3",
                    "percentage": 83
                },
                "service": {
                    "number": "7,9",
                    "percentage": 79
                },
                "general": {
                    "number": "8,1",
                    "percentage": 81
                },
                "average": {
                    "number": "8,1",
                    "percentage": 81
                }
            }
        },
        "summary": [
            {
                "description": "Variabel",
                "type": "standard"
            },
            {
                "description": "Maandelijks opzegbaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 19,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/19",
        "provider": {
            "name": "Coolblue",
            "logo": "https://api.energievergelijk.nl/storage/logo/coolblue.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,246",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,273",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,035",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "€ 200 Coolblue tegoed",
                    "title": "€ 200 Coolblue tegoed",
                    "description": "Je ontvangt drie maanden nadat je levering start CoolblueTegoed. Je kunt dit tegoed vrij besteden bij Coolblue."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 4,
                "description": "Vast termijnbedrag",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 12,
                "description": "Goed bereikbare klantenservice",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 5247,
            "summary": {
                "total": 61,
                "price": {
                    "number": "6,9",
                    "percentage": 69
                },
                "service": {
                    "number": "5,9",
                    "percentage": 59
                },
                "general": {
                    "number": "5,9",
                    "percentage": 59
                },
                "average": {
                    "number": "6,2",
                    "percentage": 62
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 20,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/20",
        "provider": {
            "name": "Coolblue",
            "logo": "https://api.energievergelijk.nl/storage/logo/coolblue.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,240",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,331",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,035",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "€ 300 Coolblue tegoed",
                    "title": "€ 300 Coolblue tegoed",
                    "description": "Je ontvangt drie maanden nadat je levering start CoolblueTegoed. Je kunt dit tegoed vrij besteden bij Coolblue."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 4,
                "description": "Vast termijnbedrag",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 12,
                "description": "Goed bereikbare klantenservice",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 5247,
            "summary": {
                "total": 61,
                "price": {
                    "number": "6,9",
                    "percentage": 69
                },
                "service": {
                    "number": "5,9",
                    "percentage": 59
                },
                "general": {
                    "number": "5,9",
                    "percentage": 59
                },
                "average": {
                    "number": "6,2",
                    "percentage": 62
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 22,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/22",
        "provider": {
            "name": "Eneco",
            "logo": "https://api.energievergelijk.nl/storage/logo/Eneco.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,251",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,349",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,192",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,182",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 26,
                "description": "100% groene stroom uit NL",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 38,
                "description": "3 jaar geen verrassingen",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 434,
            "summary": {
                "total": 822,
                "price": {
                    "number": "7,7",
                    "percentage": 77
                },
                "service": {
                    "number": "7,9",
                    "percentage": 79
                },
                "general": {
                    "number": "7,9",
                    "percentage": 79
                },
                "average": {
                    "number": "7,8",
                    "percentage": 78
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 23,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/23",
        "provider": {
            "name": "Energiedirect",
            "logo": "https://api.energievergelijk.nl/storage/logo/Energiedirect.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -16.666666666666668,
            "display_total": "-16,67",
            "details": {
                "power": {
                    "tariff": "0,256",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,370",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,050",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 16.666666666666668,
                    "display_sum": 50,
                    "label": "€ 50 korting",
                    "title": "€ 50 korting",
                    "description": "Nu tijdelijk tot <strong class=\"marker orange-small\">€ 50,-</strong> bonus. Dit bedrag ontvang je als extra korting op je eerste jaarnota. De hoogte van de korting is afhankelijk van je verbruik en postcode (<a href=\"https://api.energievergelijk.nl/vergelijker/out/23\" target=\"_blank\" rel=\"nofollow\">vul hier in</a>)."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 8,
                "description": "Onderdeel van Essent",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 33,
                "description": "3 jaar lang zekerheid",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 474,
            "summary": {
                "total": 602,
                "price": {
                    "number": "8,2",
                    "percentage": 82
                },
                "service": {
                    "number": "8,1",
                    "percentage": 81
                },
                "general": {
                    "number": "8,3",
                    "percentage": 83
                },
                "average": {
                    "number": "8,2",
                    "percentage": 82
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            },
            {
                "description": "€ 50 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 24,
        "name": "Variabel",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/24",
        "provider": {
            "name": "Energiedirect",
            "logo": "https://api.energievergelijk.nl/storage/logo/Energiedirect.svg"
        },
        "terms": {
            "type": "Variabel: tarieven wijzigen elke drie maanden of vaker",
            "end": "Maandelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,258",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,382",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,050",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 7,
                "description": "Prettige energie-app",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 18,
                "description": "Tijdig bericht bij wijzigingen",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 474,
            "summary": {
                "total": 602,
                "price": {
                    "number": "8,2",
                    "percentage": 82
                },
                "service": {
                    "number": "8,1",
                    "percentage": 81
                },
                "general": {
                    "number": "8,3",
                    "percentage": 83
                },
                "average": {
                    "number": "8,2",
                    "percentage": 82
                }
            }
        },
        "summary": [
            {
                "description": "Variabel",
                "type": "standard"
            },
            {
                "description": "Maandelijks opzegbaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 25,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/25",
        "provider": {
            "name": "Essent",
            "logo": "https://api.energievergelijk.nl/storage/logo/Essent.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -25,
            "display_total": "-25,00",
            "details": {
                "power": {
                    "tariff": "0,225",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,210",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,055",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 25,
                    "display_sum": 25,
                    "label": "Tot € 25 korting",
                    "title": "Tot € 25 korting",
                    "description": "Nu tijdelijk tot <strong class=\"marker orange-small\">€ 25,-</strong> bonus. Dit bedrag krijg je als extra korting op je jaarnota. De hoogte van de korting is afhankelijk van je verbruik en postcode (<a href=\"https://api.energievergelijk.nl/vergelijker/out/25\" target=\"_blank\" rel=\"nofollow\">vul hier in</a>)."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 14,
                "description": "Al 2,5 miljoen klanten",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 15,
                "description": "Groene stroom",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 466,
            "summary": {
                "total": 1064,
                "price": {
                    "number": "8,2",
                    "percentage": 82
                },
                "service": {
                    "number": "8,4",
                    "percentage": 84
                },
                "general": {
                    "number": "8,5",
                    "percentage": 85
                },
                "average": {
                    "number": "8,4",
                    "percentage": 84
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            },
            {
                "description": "Tot € 25 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 27,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": None,
        "provider": {
            "name": "Greenchoice",
            "logo": "https://api.energievergelijk.nl/storage/logo/greenchoice.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,245",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,246",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,160",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,148",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 6,
                "description": "100% groene stroom en gas",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 7,
                "description": "Prettige energie-app",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 503,
            "summary": {
                "total": 378,
                "price": {
                    "number": "7,9",
                    "percentage": 79
                },
                "service": {
                    "number": "8,2",
                    "percentage": 82
                },
                "general": {
                    "number": "8,2",
                    "percentage": 82
                },
                "average": {
                    "number": "8,1",
                    "percentage": 81
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 28,
        "name": "Vast (2 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": None,
        "provider": {
            "name": "Greenchoice",
            "logo": "https://api.energievergelijk.nl/storage/logo/greenchoice.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan twee jaar lang vast",
            "end": " Na twee jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,245",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,248",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,160",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,152",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 6,
                "description": "100% groene stroom en gas",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 7,
                "description": "Prettige energie-app",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 503,
            "summary": {
                "total": 378,
                "price": {
                    "number": "7,9",
                    "percentage": 79
                },
                "service": {
                    "number": "8,2",
                    "percentage": 82
                },
                "general": {
                    "number": "8,2",
                    "percentage": 82
                },
                "average": {
                    "number": "8,1",
                    "percentage": 81
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "2 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 29,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": None,
        "provider": {
            "name": "Greenchoice",
            "logo": "https://api.energievergelijk.nl/storage/logo/greenchoice.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,243",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,294",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,160",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,152",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 6,
                "description": "100% groene stroom en gas",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 7,
                "description": "Prettige energie-app",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 503,
            "summary": {
                "total": 378,
                "price": {
                    "number": "7,9",
                    "percentage": 79
                },
                "service": {
                    "number": "8,2",
                    "percentage": 82
                },
                "general": {
                    "number": "8,2",
                    "percentage": 82
                },
                "average": {
                    "number": "8,1",
                    "percentage": 81
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 31,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/31",
        "provider": {
            "name": "Innova Energie",
            "logo": "https://api.energievergelijk.nl/storage/logo/InnovaEnergie-01.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -100,
            "display_total": "-100,00",
            "details": {
                "power": {
                    "tariff": "0,258",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,233",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,061",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 100,
                    "display_sum": 100,
                    "label": "Tot € 100 korting",
                    "title": "Tot € 100 korting",
                    "description": "Nu met eenmalig tot <strong class=\"marker orange-small\">€ 100,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota. De hoogte van de korting is afhankelijk van je verbruik (<a href=\"https://api.energievergelijk.nl/vergelijker/out/31\" target=\"_blank\" rel=\"nofollow\">vul hier in</a>)."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 11,
                "description": "Persoonlijk bespaaradvies",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 18,
                "description": "Tijdig bericht bij wijzigingen",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 46,
                "description": "Klantscore kan beter",
                "description_long": None,
                "icon": "minus-compare"
            }
        ],
        "reviews": {
            "id": 722,
            "summary": {
                "total": 232,
                "price": {
                    "number": "7,0",
                    "percentage": 70
                },
                "service": {
                    "number": "6,6",
                    "percentage": 66
                },
                "general": {
                    "number": "6,5",
                    "percentage": 65
                },
                "average": {
                    "number": "6,7",
                    "percentage": 67
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            },
            {
                "description": "Tot € 100 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 32,
        "name": "Vast (2 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/32",
        "provider": {
            "name": "Innova Energie",
            "logo": "https://api.energievergelijk.nl/storage/logo/InnovaEnergie-01.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan twee jaar lang vast",
            "end": " Na twee jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -50,
            "display_total": "-50,00",
            "details": {
                "power": {
                    "tariff": "0,256",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,250",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,050",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 50,
                    "display_sum": 100,
                    "label": "Tot € 100 korting",
                    "title": "Tot € 100 korting",
                    "description": "Nu met eenmalig tot <strong class=\"marker orange-small\">€ 100,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota. Nu met eenmalig tot <strong class=\"marker orange-small\">€ 100,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota. De hoogte van de korting is afhankelijk van je verbruik (<a href=\"https://api.energievergelijk.nl/vergelijker/out/32\" target=\"_blank\" rel=\"nofollow\">vul hier in</a>)."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 18,
                "description": "Tijdig bericht bij wijzigingen",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 45,
                "description": "2 jaar lang zekerheid",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 46,
                "description": "Klantscore kan beter",
                "description_long": None,
                "icon": "minus-compare"
            }
        ],
        "reviews": {
            "id": 722,
            "summary": {
                "total": 232,
                "price": {
                    "number": "7,0",
                    "percentage": 70
                },
                "service": {
                    "number": "6,6",
                    "percentage": 66
                },
                "general": {
                    "number": "6,5",
                    "percentage": 65
                },
                "average": {
                    "number": "6,7",
                    "percentage": 67
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "2 jaar",
                "type": "standard"
            },
            {
                "description": "Tot € 100 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 33,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/33",
        "provider": {
            "name": "Innova Energie",
            "logo": "https://api.energievergelijk.nl/storage/logo/InnovaEnergie-01.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -33.333333333333336,
            "display_total": "-33,33",
            "details": {
                "power": {
                    "tariff": "0,252",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,269",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,061",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 33.333333333333336,
                    "display_sum": 100,
                    "label": "Tot € 100 korting",
                    "title": "Tot € 100 korting",
                    "description": "Nu met eenmalig tot <strong class=\"marker orange-small\">€ 100,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota. De hoogte van de korting is afhankelijk van je verbruik (<a href=\"https://api.energievergelijk.nl/vergelijker/out/33\" target=\"_blank\" rel=\"nofollow\">vul hier in</a>)."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 17,
                "description": "Deskundige klantenservice",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 18,
                "description": "Tijdig bericht bij wijzigingen",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 46,
                "description": "Klantscore kan beter",
                "description_long": None,
                "icon": "minus-compare"
            }
        ],
        "reviews": {
            "id": 722,
            "summary": {
                "total": 232,
                "price": {
                    "number": "7,0",
                    "percentage": 70
                },
                "service": {
                    "number": "6,6",
                    "percentage": 66
                },
                "general": {
                    "number": "6,5",
                    "percentage": 65
                },
                "average": {
                    "number": "6,7",
                    "percentage": 67
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            },
            {
                "description": "Tot € 100 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 42,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/42",
        "provider": {
            "name": "OM",
            "logo": "https://api.energievergelijk.nl/storage/logo/OM-nieuwe-energie.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,253",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,286",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,027",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 28,
                "description": "Lokale groene energie uit NL",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 30,
                "description": "Geen winstoogmerk",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 613,
            "summary": {
                "total": 26,
                "price": {
                    "number": "8,5",
                    "percentage": 85
                },
                "service": {
                    "number": "8,7",
                    "percentage": 87
                },
                "general": {
                    "number": "8,7",
                    "percentage": 87
                },
                "average": {
                    "number": "8,6",
                    "percentage": 86
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 43,
        "name": "Variabel",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/43",
        "provider": {
            "name": "OM",
            "logo": "https://api.energievergelijk.nl/storage/logo/OM-nieuwe-energie.svg"
        },
        "terms": {
            "type": "Variabel: tarieven wijzigen elke drie maanden of vaker",
            "end": "Maandelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,242",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,331",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,027",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 28,
                "description": "Lokale groene energie uit NL",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 30,
                "description": "Geen winstoogmerk",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 613,
            "summary": {
                "total": 26,
                "price": {
                    "number": "8,5",
                    "percentage": 85
                },
                "service": {
                    "number": "8,7",
                    "percentage": 87
                },
                "general": {
                    "number": "8,7",
                    "percentage": 87
                },
                "average": {
                    "number": "8,6",
                    "percentage": 86
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Variabel",
                "type": "standard"
            },
            {
                "description": "Maandelijks opzegbaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 44,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/44",
        "provider": {
            "name": "Oxxio",
            "logo": "https://api.energievergelijk.nl/storage/logo/Oxxio.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,243",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,347",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,192",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,182",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "Tot € 0 korting",
                    "title": "Tot € 0 korting",
                    "description": "Nu tijdelijk tot <strong class=\"marker orange-small\">€ 0</strong> bonus. De korting wordt jaarlijks in gelijke delen verrekend bij je jaarafrekening."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 4,
                "description": "Vast termijnbedrag",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 5,
                "description": "100% Europese windstroom",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 511,
            "summary": {
                "total": 207,
                "price": {
                    "number": "7,2",
                    "percentage": 72
                },
                "service": {
                    "number": "7,2",
                    "percentage": 72
                },
                "general": {
                    "number": "7,3",
                    "percentage": 73
                },
                "average": {
                    "number": "7,2",
                    "percentage": 72
                }
            }
        },
        "summary": [
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 45,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/45",
        "provider": {
            "name": "Powerpeers",
            "logo": "https://api.energievergelijk.nl/storage/logo/powerpeers-logo-nav.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,335",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,311",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,150",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "€ 0 korting",
                    "title": "€ 0 korting",
                    "description": "Nu tijdelijk met <strong class=\"marker orange-small\">€ 0,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 31,
                "description": "Onderdeel van Vattenfall",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 32,
                "description": "100% groene energie",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 2619,
            "summary": {
                "total": 9,
                "price": {
                    "number": "8,4",
                    "percentage": 84
                },
                "service": {
                    "number": "9,4",
                    "percentage": 94
                },
                "general": {
                    "number": "9,8",
                    "percentage": 98
                },
                "average": {
                    "number": "8,2",
                    "percentage": 82
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 46,
        "name": "Variabel",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/46",
        "provider": {
            "name": "Powerpeers",
            "logo": "https://api.energievergelijk.nl/storage/logo/powerpeers-logo-nav.svg"
        },
        "terms": {
            "type": "Variabel: tarieven wijzigen elke drie maanden of vaker",
            "end": "Maandelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,304",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,517",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,150",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 31,
                "description": "Onderdeel van Vattenfall",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 32,
                "description": "100% groene energie",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 2619,
            "summary": {
                "total": 9,
                "price": {
                    "number": "8,4",
                    "percentage": 84
                },
                "service": {
                    "number": "9,4",
                    "percentage": 94
                },
                "general": {
                    "number": "9,8",
                    "percentage": 98
                },
                "average": {
                    "number": "8,2",
                    "percentage": 82
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Variabel",
                "type": "standard"
            },
            {
                "description": "Maandelijks opzegbaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 47,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/47",
        "provider": {
            "name": "Pure Energie",
            "logo": "https://api.energievergelijk.nl/storage/logo/PureEnergie.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -70,
            "display_total": "-70,00",
            "details": {
                "power": {
                    "tariff": "0,254",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,246",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,060",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 70,
                    "display_sum": 70,
                    "label": "€ 70 korting",
                    "title": "€ 70 korting",
                    "description": "Nu tijdelijk met <strong class=\"marker orange-small\">€ 70,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 13,
                "description": "Korte telefonische wachttijd",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 26,
                "description": "100% groene stroom uit NL",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 520,
            "summary": {
                "total": 53,
                "price": {
                    "number": "8,8",
                    "percentage": 88
                },
                "service": {
                    "number": "8,8",
                    "percentage": 88
                },
                "general": {
                    "number": "8,7",
                    "percentage": 87
                },
                "average": {
                    "number": "8,7",
                    "percentage": 87
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            },
            {
                "description": "€ 70 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 48,
        "name": "Variabel",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/48",
        "provider": {
            "name": "Pure Energie",
            "logo": "https://api.energievergelijk.nl/storage/logo/PureEnergie.svg"
        },
        "terms": {
            "type": "Variabel: tarieven wijzigen elke drie maanden of vaker",
            "end": "Maandelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,297",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,368",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,145",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 6,
                "description": "100% groene stroom en gas",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 17,
                "description": "Deskundige klantenservice",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 520,
            "summary": {
                "total": 53,
                "price": {
                    "number": "8,8",
                    "percentage": 88
                },
                "service": {
                    "number": "8,8",
                    "percentage": 88
                },
                "general": {
                    "number": "8,7",
                    "percentage": 87
                },
                "average": {
                    "number": "8,7",
                    "percentage": 87
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Variabel",
                "type": "standard"
            },
            {
                "description": "Maandelijks opzegbaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 50,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/50",
        "provider": {
            "name": "United Consumers",
            "logo": "https://api.energievergelijk.nl/storage/logo/united-consumers.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -180,
            "display_total": "-180,00",
            "details": {
                "power": {
                    "tariff": "0,264",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,244",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,100",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 180,
                    "display_sum": 180,
                    "label": "€ 180 korting",
                    "title": "€ 180 korting",
                    "description": "Nu tijdelijk met <strong class=\"marker orange-small\">€ 180,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 4,
                "description": "Vast termijnbedrag",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 6,
                "description": "100% groene stroom en gas",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 607,
            "summary": {
                "total": 253,
                "price": {
                    "number": "8,9",
                    "percentage": 89
                },
                "service": {
                    "number": "9,0",
                    "percentage": 90
                },
                "general": {
                    "number": "9,0",
                    "percentage": 90
                },
                "average": {
                    "number": "9,0",
                    "percentage": 90
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            },
            {
                "description": "€ 180 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 51,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/51",
        "provider": {
            "name": "United Consumers",
            "logo": "https://api.energievergelijk.nl/storage/logo/united-consumers.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -80,
            "display_total": "-80,00",
            "details": {
                "power": {
                    "tariff": "0,284",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,311",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,100",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 80,
                    "display_sum": 240,
                    "label": "€ 240 korting",
                    "title": "€ 240 korting",
                    "description": "Nu tijdelijk met <strong class=\"marker orange-small\">€ 240,-</strong>. Deze korting wordt in drie delen uitgekeerd op je jaarnota."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 6,
                "description": "100% groene stroom en gas",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 12,
                "description": "Goed bereikbare klantenservice",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 13,
                "description": "Korte telefonische wachttijd",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 607,
            "summary": {
                "total": 253,
                "price": {
                    "number": "8,9",
                    "percentage": 89
                },
                "service": {
                    "number": "9,0",
                    "percentage": 90
                },
                "general": {
                    "number": "9,0",
                    "percentage": 90
                },
                "average": {
                    "number": "9,0",
                    "percentage": 90
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            },
            {
                "description": "€ 240 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 52,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/52",
        "provider": {
            "name": "Vandebron",
            "logo": "https://api.energievergelijk.nl/storage/logo/Vandebron.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -125,
            "display_total": "-125,00",
            "details": {
                "power": {
                    "tariff": "0,253",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,247",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,140",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 125,
                    "display_sum": 125,
                    "label": "€ 125 korting",
                    "title": "€ 125 korting",
                    "description": "Nu tijdelijk met <strong class=\"marker orange-small\">€ 125,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota. Claim je korting <a href=\"https://api.energievergelijk.nl/vergelijker/out/52\" target=\"_blank\" rel=\"nofollow\">hier</a>."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 13,
                "description": "Korte telefonische wachttijd",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 24,
                "description": "100% Nederlandse groene stroom",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 516,
            "summary": {
                "total": 118,
                "price": {
                    "number": "7,7",
                    "percentage": 77
                },
                "service": {
                    "number": "7,9",
                    "percentage": 79
                },
                "general": {
                    "number": "7,9",
                    "percentage": 79
                },
                "average": {
                    "number": "7,8",
                    "percentage": 78
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            },
            {
                "description": "€ 125 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 53,
        "name": "Vast (2 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/53",
        "provider": {
            "name": "Vandebron",
            "logo": "https://api.energievergelijk.nl/storage/logo/Vandebron.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan twee jaar lang vast",
            "end": " Na twee jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -75,
            "display_total": "-75,00",
            "details": {
                "power": {
                    "tariff": "0,250",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,298",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,140",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 75,
                    "display_sum": 150,
                    "label": "€ 150 korting",
                    "title": "€ 150 korting",
                    "description": "Nu tijdelijk met <strong class=\"marker orange-small\">€ 150,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je laatste jaarnota."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 26,
                "description": "100% groene stroom uit NL",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 45,
                "description": "2 jaar lang zekerheid",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 516,
            "summary": {
                "total": 118,
                "price": {
                    "number": "7,7",
                    "percentage": 77
                },
                "service": {
                    "number": "7,9",
                    "percentage": 79
                },
                "general": {
                    "number": "7,9",
                    "percentage": 79
                },
                "average": {
                    "number": "7,8",
                    "percentage": 78
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "2 jaar",
                "type": "standard"
            },
            {
                "description": "€ 150 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 54,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/54",
        "provider": {
            "name": "Vandebron",
            "logo": "https://api.energievergelijk.nl/storage/logo/Vandebron.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -50,
            "display_total": "-50,00",
            "details": {
                "power": {
                    "tariff": "0,247",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,333",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,140",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 50,
                    "display_sum": 150,
                    "label": "€ 150 korting",
                    "title": "€ 150 korting",
                    "description": "Nu tijdelijk met<strong class=\"marker orange-small\">€ 150,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je laatste jaarnota."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 26,
                "description": "100% groene stroom uit NL",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 37,
                "description": "3 jaar geen prijsstijging",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 516,
            "summary": {
                "total": 118,
                "price": {
                    "number": "7,7",
                    "percentage": 77
                },
                "service": {
                    "number": "7,9",
                    "percentage": 79
                },
                "general": {
                    "number": "7,9",
                    "percentage": 79
                },
                "average": {
                    "number": "7,8",
                    "percentage": 78
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            },
            {
                "description": "€ 150 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 55,
        "name": "Variabel",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/55",
        "provider": {
            "name": "Vandebron",
            "logo": "https://api.energievergelijk.nl/storage/logo/Vandebron.svg"
        },
        "terms": {
            "type": "Variabel: tarieven wijzigen elke drie maanden of vaker",
            "end": "Maandelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,244",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,362",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,140",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 17,
                "description": "Deskundige klantenservice",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 24,
                "description": "100% Nederlandse groene stroom",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 516,
            "summary": {
                "total": 118,
                "price": {
                    "number": "7,7",
                    "percentage": 77
                },
                "service": {
                    "number": "7,9",
                    "percentage": 79
                },
                "general": {
                    "number": "7,9",
                    "percentage": 79
                },
                "average": {
                    "number": "7,8",
                    "percentage": 78
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Variabel",
                "type": "standard"
            },
            {
                "description": "Maandelijks opzegbaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 56,
        "name": "Variabel",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/56",
        "provider": {
            "name": "Vattenfall",
            "logo": "https://api.energievergelijk.nl/storage/logo/Vattenfall-logo.svg"
        },
        "terms": {
            "type": "Variabel: tarieven wijzigen elke drie maanden of vaker",
            "end": "Maandelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,272",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,285",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,140",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 1,
                "description": "Al 2 miljoen klanten",
                "description_long": "",
                "icon": "plus-compare"
            },
            {
                "id": 24,
                "description": "100% Nederlandse groene stroom",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 461,
            "summary": {
                "total": 976,
                "price": {
                    "number": "7,7",
                    "percentage": 77
                },
                "service": {
                    "number": "8,1",
                    "percentage": 81
                },
                "general": {
                    "number": "8,0",
                    "percentage": 80
                },
                "average": {
                    "number": "7,9",
                    "percentage": 79
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Variabel",
                "type": "standard"
            },
            {
                "description": "Maandelijks opzegbaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 58,
        "name": "Vast (1 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/58",
        "provider": {
            "name": "Engie",
            "logo": "https://api.energievergelijk.nl/storage/logo/Engie.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan één jaar lang vast",
            "end": " Na één jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -50,
            "display_total": "-50,00",
            "details": {
                "power": {
                    "tariff": "0,276",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,227",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,125",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,115",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 50,
                    "display_sum": 50,
                    "label": "€ 50 korting",
                    "title": "€ 50 korting",
                    "description": "Nu met eenmalig <strong class=\"marker orange-small\">€ 50,-</strong> bonus. Dit bedrag krijg je als <strong>extra korting</strong> op je jaarnota. Claim je korting <a href=\"https://api.energievergelijk.nl/vergelijker/out/58\" target=\"_blank\" rel=\"nofollow\">hier</a>."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 26,
                "description": "100% groene stroom uit NL",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 48,
                "description": "Inzicht en besparen via energie-app",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 478,
            "summary": {
                "total": 279,
                "price": {
                    "number": "8,4",
                    "percentage": 84
                },
                "service": {
                    "number": "8,5",
                    "percentage": 85
                },
                "general": {
                    "number": "8,6",
                    "percentage": 86
                },
                "average": {
                    "number": "8,5",
                    "percentage": 85
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "1 jaar",
                "type": "standard"
            },
            {
                "description": "€ 50 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 59,
        "name": "Vast (3 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/59",
        "provider": {
            "name": "Engie",
            "logo": "https://api.energievergelijk.nl/storage/logo/Engie.svg"
        },
        "terms": {
            "type": "Meerjarig: tarieven staan drie jaar vast",
            "end": "Na drie jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": -50,
            "display_total": "-50,00",
            "details": {
                "power": {
                    "tariff": "0,265",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,309",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,125",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,115",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 50,
                    "display_sum": 150,
                    "label": "€ 150 korting",
                    "title": "€ 150 korting",
                    "description": "Nu tijdelijk tot <strong class=\"marker orange-small\">>€ 150</strong> bonus. De korting wordt jaarlijks in gelijke delen verrekend bij je jaarafrekening."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 12,
                "description": "Goed bereikbare klantenservice",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 26,
                "description": "100% groene stroom uit NL",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 478,
            "summary": {
                "total": 279,
                "price": {
                    "number": "8,4",
                    "percentage": 84
                },
                "service": {
                    "number": "8,5",
                    "percentage": 85
                },
                "general": {
                    "number": "8,6",
                    "percentage": 86
                },
                "average": {
                    "number": "8,5",
                    "percentage": 85
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "3 jaar",
                "type": "standard"
            },
            {
                "description": "€ 150 korting",
                "type": "discount"
            }
        ]
    },
    {
        "id": 60,
        "name": "Vast (2 jaar)",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/60",
        "provider": {
            "name": "Powerpeers",
            "logo": "https://api.energievergelijk.nl/storage/logo/powerpeers-logo-nav.svg"
        },
        "terms": {
            "type": "Jaarcontract: tarieven staan twee jaar lang vast",
            "end": " Na twee jaar op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,359",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,339",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,150",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "€ 0 korting",
                    "title": "€ 0 korting",
                    "description": "Nu tijdelijk tot <strong class=\"marker orange-small\">€ 0</strong> bonus. Dit bedrag ontvang je in twee delen als extra korting op je jaarnota’s. De hoogte van de korting is afhankelijk van je verbruik en postcode (<a href=\"https://api.energievergelijk.nl/vergelijker/out/60\" target=\"_blank\" rel=\"nofollow\">vul hier in</a>)."
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 31,
                "description": "Onderdeel van Vattenfall",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 32,
                "description": "100% groene energie",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 2619,
            "summary": {
                "total": 9,
                "price": {
                    "number": "8,4",
                    "percentage": 84
                },
                "service": {
                    "number": "9,4",
                    "percentage": 94
                },
                "general": {
                    "number": "9,8",
                    "percentage": 98
                },
                "average": {
                    "number": "8,2",
                    "percentage": 82
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Vast",
                "type": "standard"
            },
            {
                "description": "2 jaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 61,
        "name": "Variabel",
        "feature": {
            "active": False,
            "label": None
        },
        "out": "https://api.energievergelijk.nl/vergelijker/out/61",
        "provider": {
            "name": "Engie",
            "logo": "https://api.energievergelijk.nl/storage/logo/Engie.svg"
        },
        "terms": {
            "type": "Variabel: tarieven wijzigen elke drie maanden of vaker",
            "end": "Maandelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,275",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,280",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,125",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,115",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 15,
                "description": "Groene stroom",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 25,
                "description": "CO2-gecompenseerd gas",
                "description_long": None,
                "icon": "plus-compare"
            }
        ],
        "reviews": {
            "id": 478,
            "summary": {
                "total": 279,
                "price": {
                    "number": "8,4",
                    "percentage": 84
                },
                "service": {
                    "number": "8,5",
                    "percentage": 85
                },
                "general": {
                    "number": "8,6",
                    "percentage": 86
                },
                "average": {
                    "number": "8,5",
                    "percentage": 85
                }
            }
        },
        "summary": [
            {
                "icon": "leaf.svg",
                "description": "100% groen uit Nederland",
                "label": "Duurzaamheid",
                "type": "highlight"
            },
            {
                "description": "Variabel",
                "type": "standard"
            },
            {
                "description": "Maandelijks opzegbaar",
                "type": "standard"
            }
        ]
    },
    {
        "id": 70,
        "name": "Dynamisch",
        "feature": {
            "active": False,
            "label": None
        },
        "out": None,
        "provider": {
            "name": "ANWB energie",
            "logo": "https://api.energievergelijk.nl/storage/logo/ANWB-1.svg"
        },
        "terms": {
            "type": "Dynamisch: stroomtarieven verschillen per uur, gastarieven per dag",
            "end": "Dagelijks op te zeggen, zonder boete"
        },
        "pricing": {
            "total": 0,
            "display_total": "0,00",
            "details": {
                "power": {
                    "tariff": "0,261",
                    "consumption": 0,
                    "total_sum": 0,
                    "tax_reduction": 0,
                    "display_sum": "0,00"
                },
                "gas": {
                    "tariff": "1,111",
                    "consumption": None,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in": {
                    "tariff": "0,000",
                    "consumption": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "feed_in_cost": {
                    "tariff": "0,000",
                    "fee": 0,
                    "label": "",
                    "total_kwh": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "fixed_cost": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "operator": {
                    "power": 0,
                    "gas": 0,
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "bruto": {
                    "total_sum": 0,
                    "display_sum": "0,00"
                },
                "discount": {
                    "type": "PRICE",
                    "total_sum": 0,
                    "display_sum": 0,
                    "label": "",
                    "title": "",
                    "description": ""
                },
                "summary": {
                    "power": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "gas": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    },
                    "feed_in": {
                        "total_sum": 0,
                        "display_sum": "0,00"
                    }
                }
            }
        },
        "features": [
            {
                "id": 2,
                "description": "Energie tegen inkoopprijs",
                "description_long": None,
                "icon": "plus-compare"
            },
            {
                "id": 3,
                "description": "Slimme meter verplicht",
                "description_long": None,
                "icon": "minus-compare"
            }
        ],
        "reviews": {
            "id": 5509,
            "summary": {
                "total": 401,
                "price": {
                    "number": "7,6",
                    "percentage": 76
                },
                "service": {
                    "number": "6,4",
                    "percentage": 64
                },
                "general": {
                    "number": "6,8",
                    "percentage": 68
                },
                "average": {
                    "number": "6,9",
                    "percentage": 69
                }
            }
        },
        "summary": [
            {
                "description": "Dynamisch",
                "type": "standard"
            },
            {
                "description": "Vrij opzegbaar",
                "type": "standard"
            }
        ]
    }
]

@app.post("/energievergelijk-tarriffs")
def get_energy_tarriff_data(tarriff: Tarriff ):
    return JSONResponse(content=response_data)
