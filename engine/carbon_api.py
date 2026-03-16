import json
import random
from datetime import datetime

ZONES = [
    "IN-SO",
    "SG",
    "US-VA",
    "US-OR",
    "DE",
    "IE",
    "JP"
]

def generate_carbon_data():

    results = {}

    for zone in ZONES:
        results[zone] = {
            "carbonIntensity": random.randint(80, 600),
            "datetime": str(datetime.now())
        }

    with open("data/carbon_data.json", "w") as file:
        json.dump(results, file, indent=4)

    print("Simulated carbon data generated!")

if __name__ == "__main__":
    generate_carbon_data()
