def build_mitre_statistics(mitre):

    stats = {
        "Initial Access": 0,
        "Execution": 0,
        "Persistence": 0,
        "Privilege Escalation": 0,
        "Defense Evasion": 0,
        "Credential Access": 0,
        "Discovery": 0,
        "Lateral Movement": 0,
        "Collection": 0,
        "Exfiltration": 0
    }

    for item in mitre:

        name = item["name"]

        if "Brute" in name:
            stats["Initial Access"] += 1

        elif "PowerShell" in name:
            stats["Execution"] += 1

        elif "Credential" in name:
            stats["Credential Access"] += 1

        elif "Discovery" in name:
            stats["Discovery"] += 1

        elif "Lateral" in name:
            stats["Lateral Movement"] += 1

        elif "Exfiltration" in name:
            stats["Exfiltration"] += 1

        else:
            stats["Execution"] += 1

    return stats