def build_timeline(logs, threats):
    """
    Build a simple event timeline from parsed logs.
    """

    timeline = []

    for log in logs:

        event = {
            "time": log.get("date", "Unknown"),
            "level": log.get("level", "INFO"),
            "message": log.get("message", "")
        }

        timeline.append(event)

    # Sort by time if available
    timeline = sorted(
        timeline,
        key=lambda x: x["time"]
    )

    return timeline