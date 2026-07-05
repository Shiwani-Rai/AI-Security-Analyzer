def analyze_logs(logs):
    info_count = 0
    warning_count = 0
    error_count = 0

    for log in logs:
        if "INFO" in log:
            info_count += 1

        elif "WARNING" in log:
            warning_count += 1

        elif "ERROR" in log:
            error_count += 1

    return {
        "INFO": info_count,
        "WARNING": warning_count,
        "ERROR": error_count
    }