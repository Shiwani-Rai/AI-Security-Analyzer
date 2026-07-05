def build_threat_statistics(vt_results):

    stats = {
        "clean": 0,
        "malicious": 0,
        "suspicious": 0,
        "unknown": 0
    }

    if not vt_results:
        stats["unknown"] = 0
        return stats

    for item in vt_results:

        if item["malicious"] > 0:
            stats["malicious"] += 1

        elif item["suspicious"] > 0:
            stats["suspicious"] += 1

        else:
            stats["clean"] += 1

    return stats