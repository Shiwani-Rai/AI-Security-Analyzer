from collections import Counter


def build_analytics(threats, mitre, iocs, risk):

    analytics = {}

    # -------------------------
    # Threat Distribution
    # -------------------------
    analytics["threat_distribution"] = dict(
        Counter(threats)
    )

    # -------------------------
    # MITRE Distribution
    # -------------------------
    mitre_ids = []

    for item in mitre:
        mitre_ids.append(item["id"])

    analytics["mitre_distribution"] = dict(
        Counter(mitre_ids)
    )

    # -------------------------
    # IOC Distribution
    # -------------------------
    analytics["ioc_distribution"] = {

        "IPs": len(iocs["ips"]),

        "Domains": len(iocs["domains"]),

        "URLs": len(iocs["urls"]),

        "SHA256": len(iocs["sha256"]),

        "Emails": len(iocs["emails"])

    }

    # -------------------------
    # Risk Distribution
    # -------------------------
    analytics["risk_distribution"] = {

        risk["risk"]: 1

    }

    return analytics