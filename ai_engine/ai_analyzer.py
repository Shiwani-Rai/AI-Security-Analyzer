from ollama import chat

def analyze_with_ai(logs, threats, risk):

    formatted_logs = ""

    for log in logs[:30]:      # Limit to first 30 logs
        formatted_logs += (
            f"{log['date']} | "
            f"{log['level']} | "
            f"{log['message']}\n"
        )

    prompt = f"""
You are a Senior SOC Analyst working in a Security Operations Center.

Analyze the following security incident.

===========================
SECURITY OVERVIEW
===========================

Risk Score: {risk['score']}/100

Risk Level: {risk['risk']}

Detected Threats:
{chr(10).join("- " + t for t in threats) if threats else "- None"}

Number of Logs: {len(logs)}

===========================
SECURITY LOGS
===========================

{formatted_logs}

===========================
Generate a professional SOC Incident Report using the following format.

## Executive Summary

Provide a short overview of the incident.

## Security Findings

List the important findings.

## Risk Assessment

Explain why the incident is Low, Medium, High or Critical.

## MITRE ATT&CK Perspective

Explain what attacker behavior is observed.

## Recommended Actions

Provide immediate remediation steps.

## SOC Analyst Notes

Provide additional observations.

Keep the report concise, professional and easy to understand.
"""

    response = chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]