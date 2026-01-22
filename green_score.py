import json

# Load carbon data
with open("carbon_data.json", "r") as file:
    data = json.load(file)

def calculate_green_score(region):
    renewable = region["renewable_percentage"]
    carbon = region["carbon_intensity"]

    score = (renewable * 0.7) + ((500 - carbon) * 0.3)
    return score

best_region = None
best_score = -1

for region_code, region_data in data.items():
    score = calculate_green_score(region_data)
    print(f"{region_code} Green Score: {score:.2f}")

    if score > best_score:
        best_score = score
        best_region = region_code

print("\n🌱 Best Region for Deployment:", best_region)
