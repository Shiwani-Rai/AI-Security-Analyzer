def generate_playbook(threats):

    playbook = []

    for threat in threats:

        t = threat.lower()

        if "brute" in t:

            playbook.append({
                "title": "Brute Force Attack",
                "containment": "Block the source IP address.",
                "investigation": "Review authentication logs.",
                "recovery": "Force password reset for affected accounts."
            })

        elif "sql" in t:

            playbook.append({
                "title": "SQL Injection",
                "containment": "Block malicious requests using WAF.",
                "investigation": "Review database logs.",
                "recovery": "Patch vulnerable application."
            })

        elif "powershell" in t:

            playbook.append({
                "title": "PowerShell Execution",
                "containment": "Isolate the endpoint.",
                "investigation": "Collect PowerShell logs.",
                "recovery": "Run antivirus and EDR scan."
            })

        elif "malware" in t:

            playbook.append({
                "title": "Malware Infection",
                "containment": "Disconnect infected device.",
                "investigation": "Collect memory and disk artifacts.",
                "recovery": "Reimage system if necessary."
            })

        else:

            playbook.append({
                "title": threat,
                "containment": "Investigate suspicious activity.",
                "investigation": "Review related logs.",
                "recovery": "Follow SOC procedures."
            })

    return playbook