import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_KEY = os.getenv("VT_API_KEY")


HEADERS = {
    "x-apikey": API_KEY
}

def check_ip(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    response = requests.get(
        url,
        headers=HEADERS
    )

    print("\n========== VIRUSTOTAL ==========")
    print("Checking:", ip)
    print("Status:", response.status_code)
    print("Response:", response.text[:500])
    print("================================\n")

    if response.status_code != 200:
        return None

    data = response.json()
    
    attributes = data["data"]["attributes"]

    stats = attributes["last_analysis_stats"]

    return {
        "country": attributes.get("country", "Unknown"),
        "reputation": attributes.get("reputation", "Unknown"),
        "malicious": stats.get("malicious", 0),
        "suspicious": stats.get("suspicious", 0),
        "harmless": stats.get("harmless", 0),
        "undetected": stats.get("undetected", 0)
    }
    # stats = data["data"]["attributes"]["last_analysis_stats"]

    # return {
    #     "malicious": stats["malicious"],
    #     "suspicious": stats["suspicious"],
    #     "harmless": stats["harmless"],
    #     "undetected": stats["undetected"]
    # }