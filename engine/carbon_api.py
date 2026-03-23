import requests
import json
from datetime import datetime

API_KEY = "gbN2vcahyK7U39cG9t4G"

ZONES = {
    "ap-south-1": "IN-SO",
    "ap-southeast-1": "SG",
    "us-east-1": "US-VA",
    "us-west-2": "US-OR",
    "eu-central-1": "DE",
    "eu-west-1": "IE",
    "ap-northeast-1": "JP"
}

def fetch_carbon_data():
    data = {}

    for region, zone in ZONES.items():
        url = f"https://api.electricitymap.org/v3/carbon-intensity/latest?zone={zone}"

        headers = {
            "auth-token": API_KEY
        }

        try:
            response = requests.get(url, headers=headers)
            result = response.json()

            data[zone] = {
                "carbonIntensity": result.get("carbonIntensity", 0),
                "datetime": str(datetime.now())
            }

        except Exception as e:
            print(f"Error fetching {zone}: {e}")

    with open("data/carbon_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Real-time carbon data updated!")

if __name__ == "__main__":
    fetch_carbon_data()
