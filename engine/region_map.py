# Map AWS EC2 regions to Electricity Maps zones

region_map = {
    "ap-south-1": "IN-SO",        # Mumbai
    "ap-southeast-1": "SG",       # Singapore
    "us-east-1": "US-VA",         # Virginia
    "us-west-2": "US-OR",         # Oregon
    "eu-west-1": "IE",            # Ireland
    "eu-central-1": "DE",         # Frankfurt
    "ap-northeast-1": "JP"        # Tokyo
}

def get_regions():
    return list(region_map.keys())

def get_zone(region):
    return region_map.get(region)
