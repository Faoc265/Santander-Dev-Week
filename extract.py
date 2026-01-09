users = [
    {
        "id": 4,
        "name": "Juan",
        "account": {
            "id": 7,
            "number": "00001-1",
            "agency": "0001",
            "balance": 0.0,
            "limit": 500.0
        },
        "card": {
            "id": 4,
            "number": "**** **** **** 1111",
            "limit": 1000.0
        }
    },
    {
        "id": 5,
        "name": "Juvenal",
        "account": {
            "id": 8,
            "number": "00002-2",
            "agency": "0001",
            "balance": 0.0,
            "limit": 500.0
        },
        "card": {
            "id": 5,
            "number": "**** **** **** 2222",
            "limit": 1000.0
        }
    },
    {
        "id": 6,
        "name": "Adenilson",
        "account": {
            "id": 9,
            "number": "00003-3",
            "agency": "0001",
            "balance": 0.0,
            "limit": 500.0
        },
        "card": {
            "id": 6,
            "number": "**** **** **** 3333",
            "limit": 1000.0
        }
    }
]

import json
print(json.dumps(users, indent=2, ensure_ascii=False))