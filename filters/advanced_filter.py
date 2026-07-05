def filter_logs(logs, keyword):

    if not keyword:
        return logs

    keyword = keyword.lower()

    filtered = []

    for log in logs:

        text = " ".join(str(value) for value in log.values()).lower()

        if keyword in text:
            filtered.append(log)

    return filtered