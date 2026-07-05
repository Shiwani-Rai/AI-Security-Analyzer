def build_attack_path(threats):

    attack_flow = []

    # Initial Access
    if any("Brute" in t for t in threats):
        attack_flow.append("🔐 Initial Access - Brute Force")

    if any("SQL" in t for t in threats):
        attack_flow.append("🌐 Initial Access - SQL Injection")

    if any("XSS" in t for t in threats):
        attack_flow.append("🌐 Initial Access - Cross Site Scripting")

    # Discovery
    if any("Port" in t for t in threats):
        attack_flow.append("🔍 Discovery - Network Scanning")

    if any("Recon" in t for t in threats):
        attack_flow.append("🛰 Discovery - Reconnaissance")

    # Execution
    if any("PowerShell" in t for t in threats):
        attack_flow.append("💻 Execution - PowerShell")

    if any("Command Injection" in t for t in threats):
        attack_flow.append("⚙ Execution - Command Injection")

    if any("Reverse Shell" in t for t in threats):
        attack_flow.append("🐚 Execution - Reverse Shell")

    # Credential Access
    if any("Credential" in t for t in threats):
        attack_flow.append("🔑 Credential Access")

    # Privilege Escalation
    if any("Privilege" in t for t in threats):
        attack_flow.append("⬆ Privilege Escalation")

    # Persistence
    if any("Web Shell" in t for t in threats):
        attack_flow.append("🕸 Persistence - Web Shell")

    # Malware
    if any("Malware" in t for t in threats):
        attack_flow.append("🦠 Malware Execution")

    if any("Ransomware" in t for t in threats):
        attack_flow.append("💣 Ransomware Impact")

    # Collection / Exfiltration
    if any("Data Exfiltration" in t for t in threats):
        attack_flow.append("📤 Data Exfiltration")

    if not attack_flow:
        attack_flow.append("✅ No attack chain detected")

    return attack_flow