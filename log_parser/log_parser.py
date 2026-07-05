import re


def read_logs(file_path):

    parsed_logs = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            log = {
                "date": "",
                "level": "INFO",
                "message": line,
                "ip": None,
                "email": None,
                "url": None
            }

            # --------------------------------------------------
            # Generic App Logs
            # Example:
            # 2026-06-27 INFO User Login Successful
            # --------------------------------------------------

            parts = line.split(" ", 2)

            if len(parts) == 3 and parts[1] in ["INFO", "WARNING", "ERROR"]:

                log["date"] = parts[0]
                log["level"] = parts[1]
                log["message"] = parts[2]

            # --------------------------------------------------
            # Apache / Nginx Access Logs
            # --------------------------------------------------

            ip_match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)

            if ip_match:

                log["ip"] = ip_match.group(1)

            # --------------------------------------------------
            # AWS S3 / Apache Timestamp
            # --------------------------------------------------

            date_match = re.search(r"\[([^\]]+)\]", line)

            if date_match:

                log["date"] = date_match.group(1)

            url_match = re.search(r'https?://[^\s"]+', line)

            if url_match:

                log["url"] = url_match.group(0)

            # --------------------------------------------------
            # Email
            # --------------------------------------------------

            email_match = re.search(
                r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                line
            )

            if email_match:

                log["email"] = email_match.group(0)

            parsed_logs.append(log)

    return parsed_logs