def build_mitre_analytics(mitre):

    tactics = {
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

        name = item["name"].lower()

        if "brute" in name:
            tactics["Credential Access"] += 1

        elif "powershell" in name:
            tactics["Execution"] += 1

        elif "sql" in name:
            tactics["Initial Access"] += 1

        elif "privilege" in name:
            tactics["Privilege Escalation"] += 1

        elif "command" in name:
            tactics["Execution"] += 1

        else:
            tactics["Discovery"] += 1

    return tactics