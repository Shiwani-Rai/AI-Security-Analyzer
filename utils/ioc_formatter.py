def build_ioc_table(iocs, vt_results):
    """
    Build a unified IOC table for the dashboard.
    """

    table = []

    # -------------------------
    # VirusTotal IP Results
    # -------------------------
    vt_lookup = {}

    for item in vt_results:
        vt_lookup[item["ip"]] = item

    # -------------------------
    # IP Addresses
    # -------------------------
    for ip in iocs["ips"]:

        vt = vt_lookup.get(ip)

        if vt:

            if vt["malicious"] > 0:
                reputation = "🔴 Malicious"

            elif vt["suspicious"] > 0:
                reputation = "🟠 Suspicious"

            else:
                reputation = "🟢 Clean"

            source = "VirusTotal"

        else:

            reputation = "⚪ Unknown"

            source = "Local"

        table.append({
            "ioc": ip,
            "type": "IP Address",
            "reputation": reputation,
            "source": source
        })

    # -------------------------
    # Domains
    # -------------------------
    for domain in iocs["domains"]:

        table.append({
            "ioc": domain,
            "type": "Domain",
            "reputation": "⚪ Unknown",
            "source": "Local"
        })

    # -------------------------
    # URLs
    # -------------------------
    for url in iocs["urls"]:

        table.append({
            "ioc": url,
            "type": "URL",
            "reputation": "⚪ Unknown",
            "source": "Local"
        })

    # -------------------------
    # SHA256
    # -------------------------
    for sha in iocs["sha256"]:

        table.append({
            "ioc": sha,
            "type": "SHA256",
            "reputation": "⚪ Unknown",
            "source": "Local"
        })

    return table