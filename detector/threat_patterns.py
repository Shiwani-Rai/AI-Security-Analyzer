def detect_patterns(logs):

    threats = []

    for log in logs:

        message = log["message"].lower()

        # -------------------------
        # Brute Force
        # -------------------------
        if (
            "multiple login attempts" in message
            or "authentication failed" in message
            or "failed login" in message
            or "invalid password" in message
            or "login failed" in message
        ):
            threats.append("Possible Brute Force Attack")

        # -------------------------
        # SSH Brute Force
        # -------------------------
        if (
            "failed password" in message
            or "invalid user" in message
            or "authentication failure" in message
        ):
            threats.append("SSH Brute Force")

        # -------------------------
        # SQL Injection
        # -------------------------
        if (
            "union select" in message
            or "' or '1'='1" in message
            or "sql injection" in message
            or "drop table" in message
            or "select * from" in message
        ):
            threats.append("Possible SQL Injection")

        # -------------------------
        # Cross Site Scripting
        # -------------------------
        if (
            "<script>" in message
            or "javascript:" in message
            or "onerror=" in message
            or "xss" in message
        ):
            threats.append("Possible Cross Site Scripting (XSS)")

        # -------------------------
        # Port Scan
        # -------------------------
        if (
            "port scan" in message
            or "nmap" in message
            or "masscan" in message
        ):
            threats.append("Possible Port Scanning")

        # -------------------------
        # Malware
        # -------------------------
        if (
            "malware" in message
            or "trojan" in message
            or "worm" in message
            or "virus" in message
            or "ransomware" in message
        ):
            threats.append("Possible Malware Activity")

        # -------------------------
        # PowerShell
        # -------------------------
        if (
            "powershell" in message
            or "invoke-expression" in message
            or "iex " in message
        ):
            threats.append("PowerShell Execution Detected")

        # -------------------------
        # Reverse Shell
        # -------------------------
        if (
            "nc -e" in message
            or "bash -i" in message
            or "/bin/sh" in message
            or "/bin/bash" in message
        ):
            threats.append("Possible Reverse Shell")

        # -------------------------
        # Directory Traversal
        # -------------------------
        if (
            "../" in message
            or "..\\" in message
            or "/etc/passwd" in message
        ):
            threats.append("Directory Traversal Attempt")

        # -------------------------
        # Command Injection
        # -------------------------
        if (
            "cmd.exe" in message
            or "whoami" in message
            or "&&" in message
            or ";cat" in message
        ):
            threats.append("Possible Command Injection")

        # -------------------------
        # Reconnaissance
        # -------------------------
        if (
            "recon" in message
            or "enum" in message
            or "fingerprint" in message
        ):
            threats.append("Reconnaissance Activity")

        # -------------------------
        # Suspicious User Agent
        # -------------------------
        if (
            "curl/" in message
            or "python-requests" in message
            or "sqlmap" in message
            or "nikto" in message
        ):
            threats.append("Suspicious User Agent")

        # -------------------------
        # AWS Access Denied (Step 1)
        # -------------------------
        if (
            "accessdenied" in message
            or "403" in message
        ):
            threats.append("Unauthorized Resource Access")

        # -------------------------
        # Internal Server Error (Step 2)
        # -------------------------
        if (
            "500 internalerror" in message
            or "internalerror" in message
        ):
            threats.append("Server Internal Error")

        # -------------------------
        # Object Enumeration (Step 3)
        # -------------------------
        if (
            "rest.get.object" in message
            or "listbucket" in message
        ):
            threats.append("Possible Object Enumeration")

        # -------------------------
        # Suspicious Upload (Step 4)
        # -------------------------
        if (
            "rest.put.object" in message
            or "put /" in message
        ):
            threats.append("File Upload Activity")

        # -------------------------
        # AWS SDK Activity (Step 5)
        # -------------------------
        if (
            "aws-sdk" in message
        ):
            threats.append("Automated Cloud API Activity")

        # -------------------------
        # Credential Dumping
        # -------------------------
        if (
            "mimikatz" in message
            or "lsass" in message
        ):
            threats.append("Credential Dumping")

        # -------------------------
        # Web Shell
        # -------------------------
        if (
            "cmd.php" in message
            or "shell.php" in message
            or "webshell" in message
        ):
            threats.append("Possible Web Shell")

        # -------------------------
        # Suspicious File Download
        # -------------------------
        if (
            "wget " in message
            or "curl " in message
            or "certutil" in message
        ):
            threats.append("Suspicious File Download")

        # -------------------------
        # Privilege Escalation
        # -------------------------
        if (
            "sudo su" in message
            or "privilege escalation" in message
            or "administrator privileges" in message
        ):
            threats.append("Privilege Escalation")

        # -------------------------
        # Data Exfiltration
        # -------------------------
        if (
            "scp " in message
            or "ftp upload" in message
            or "exfiltration" in message
        ):
            threats.append("Possible Data Exfiltration")

    return sorted(list(set(threats)))