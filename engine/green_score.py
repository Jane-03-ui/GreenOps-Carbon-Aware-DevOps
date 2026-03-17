import json

# Map zones to AWS regions
zone_to_region = {
    "IN-SO": "ap-south-1",
    "SG": "ap-southeast-1",
    "US-VA": "us-east-1",
    "US-OR": "us-west-2",
    "DE": "eu-central-1",
    "IE": "eu-west-1",
    "JP": "ap-northeast-1"
}


def calculate_green_score(carbon):
    return max(0, 100 - (carbon / 5))


def find_best_region():
    with open("data/carbon_data.json", "r") as file:
        data = json.load(file)

    results = {}

    for zone, values in data.items():
        carbon = values["carbonIntensity"]
        score = calculate_green_score(carbon)

        region = zone_to_region.get(zone)

        results[region] = {
            "carbon": carbon,
            "green_score": score
        }

    # Find best region (highest score)
    best_region = max(results, key=lambda x: results[x]["green_score"])

    return results, best_region


if __name__ == "__main__":
    results, best = find_best_region()

    print("\n🌍 Region Scores:\n")

    for region, values in results.items():
        print(f"{region} → Carbon: {values['carbon']} | Score: {values['green_score']}")

    print(f"\n🌱 Best Region for Deployment: {best}")
