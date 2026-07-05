def map_to_mitre(threats):

    mitre = []

    for threat in threats:

        threat = threat.lower()

        if "brute" in threat:
            mitre.append({"id": "T1110", "name": "Brute Force"})

        elif "sql" in threat:
            mitre.append({"id": "T1190", "name": "Exploit Public-Facing Application"})

        elif "powershell" in threat:
            mitre.append({"id": "T1059", "name": "Command and Scripting Interpreter"})

        elif "credential" in threat:
            mitre.append({"id": "T1003", "name": "OS Credential Dumping"})

        elif "malware" in threat:
            mitre.append({"id": "T1204", "name": "User Execution"})

        elif "ransomware" in threat:
            mitre.append({"id": "T1486", "name": "Data Encrypted for Impact"})

        elif "phishing" in threat:
            mitre.append({"id": "T1566", "name": "Phishing"})

        elif "reverse shell" in threat:
            mitre.append({"id": "T1059", "name": "Command and Scripting Interpreter"})

        elif "command injection" in threat:
            mitre.append({"id": "T1059", "name": "Command and Scripting Interpreter"})

        elif "directory traversal" in threat:
            mitre.append({"id": "T1083", "name": "File and Directory Discovery"})

        elif "port scanning" in threat:
            mitre.append({"id": "T1046", "name": "Network Service Scanning"})

        elif "reconnaissance" in threat:
            mitre.append({"id": "T1595", "name": "Active Scanning"})

        elif "web shell" in threat:
            mitre.append({"id": "T1505.003", "name": "Web Shell"})

        elif "file download" in threat:
            mitre.append({"id": "T1105", "name": "Ingress Tool Transfer"})

        elif "privilege escalation" in threat:
            mitre.append({"id": "T1068", "name": "Exploitation for Privilege Escalation"})

        elif "exfiltration" in threat:
            mitre.append({"id": "T1048", "name": "Exfiltration Over Alternative Protocol"})

        elif "unauthorized resource access" in threat:
            mitre.append({"id": "T1078", "name": "Valid Accounts"})

        elif "object enumeration" in threat:
            mitre.append({"id": "T1087", "name": "Account Discovery"})

        elif "automated cloud api activity" in threat:
            mitre.append({"id": "T1526", "name": "Cloud Service Discovery"})

        elif "server internal error" in threat:
            mitre.append({"id": "T1499", "name": "Endpoint Denial of Service"})

        elif "suspicious user agent" in threat:
            mitre.append({"id": "T1583", "name": "Acquire Infrastructure"})

    # Remove duplicate mappings
    unique = []
    seen = set()

    for item in mitre:
        if item["id"] not in seen:
            unique.append(item)
            seen.add(item["id"])

    return unique