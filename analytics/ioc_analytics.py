def build_ioc_analytics(iocs):

    total = (
        len(iocs["ips"]) +
        len(iocs["domains"]) +
        len(iocs["urls"]) +
        len(iocs["emails"]) +
        len(iocs["md5"]) +
        len(iocs["sha1"]) +
        len(iocs["sha256"]) +
        len(iocs["cves"])
    )

    return {
        "Total IOCs": total,
        "IP Addresses": len(iocs["ips"]),
        "Domains": len(iocs["domains"]),
        "URLs": len(iocs["urls"]),
        "Emails": len(iocs["emails"]),
        "MD5 Hashes": len(iocs["md5"]),
        "SHA1 Hashes": len(iocs["sha1"]),
        "SHA256 Hashes": len(iocs["sha256"]),
        "CVEs": len(iocs["cves"])
    }