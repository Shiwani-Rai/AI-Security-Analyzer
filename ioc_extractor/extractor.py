import re


def extract_iocs(logs):

    ips = set()
    emails = set()
    urls = set()
    domains = set()
    md5_hashes = set()
    sha1_hashes = set()
    sha256_hashes = set()
    cves = set()

    # -------------------------
    # Regex Patterns
    # -------------------------

    ip_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    url_pattern = r"https?://[^\s\"']+"

    domain_pattern = r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"

    md5_pattern = r"\b[a-fA-F0-9]{32}\b"

    sha1_pattern = r"\b[a-fA-F0-9]{40}\b"

    sha256_pattern = r"\b[a-fA-F0-9]{64}\b"

    cve_pattern = r"CVE-\d{4}-\d{4,7}"

    # -------------------------
    # Scan every log
    # -------------------------

    for log in logs:

        message = log["message"]

        ips.update(re.findall(ip_pattern, message))

        emails.update(re.findall(email_pattern, message))

        urls.update(re.findall(url_pattern, message))

        domains.update(re.findall(domain_pattern, message))

        md5_hashes.update(re.findall(md5_pattern, message))

        sha1_hashes.update(re.findall(sha1_pattern, message))

        sha256_hashes.update(re.findall(sha256_pattern, message))

        cves.update(re.findall(cve_pattern, message))

    return {

        "ips": sorted(list(ips)),

        "emails": sorted(list(emails)),

        "urls": sorted(list(urls)),

        "domains": sorted(list(domains)),

        "md5": sorted(list(md5_hashes)),

        "sha1": sorted(list(sha1_hashes)),

        "sha256": sorted(list(sha256_hashes)),

        "cves": sorted(list(cves))

    }