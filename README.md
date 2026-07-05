# 🛡️ AI Security Analyzer

> **AI-powered Web-Based SOC Security Analysis Tool**

## 📌 Overview

AI Security Analyzer is a Flask-based web application that helps
Security Operations Center (SOC) analysts analyze log files, detect
cyber threats, extract Indicators of Compromise (IOCs), map attacks to
the MITRE ATT&CK framework, enrich findings using VirusTotal and IP
geolocation, and generate AI-assisted incident reports.

The goal is to automate repetitive log analysis tasks and present the
results through an interactive dashboard and downloadable PDF report.

------------------------------------------------------------------------

# ✨ Features

-   📄 Log parsing
-   🚨 Threat detection
-   📊 Risk scoring
-   🌐 IOC extraction (IPs, URLs, domains, emails, hashes, CVEs)
-   🎯 MITRE ATT&CK mapping
-   🛡️ VirusTotal threat intelligence
-   🌍 IP geolocation
-   🤖 AI-generated SOC report using Ollama (Llama 3.2)
-   📈 Interactive dashboard
-   📅 Timeline generation
-   🔗 Attack path visualization
-   📘 Incident response playbook
-   📄 PDF report generation

------------------------------------------------------------------------

# 🏗️ High-Level Workflow

``` text
Upload Log File
      │
      ▼
 Log Parser
      │
      ▼
 Threat Detection
      │
      ├── IOC Extraction
      ├── MITRE Mapping
      ├── Risk Analysis
      ├── VirusTotal Lookup
      ├── IP Geolocation
      ├── AI Analysis
      ▼
 Interactive Dashboard
      ▼
 PDF Report
```

------------------------------------------------------------------------

# 📂 Project Structure

``` text
AI-Security-Analyzer/
├── analytics/
├── ai_engine/
├── detector/
├── engine/
├── filters/
├── ioc_extractor/
├── log_parser/
├── static/
├── templates/
├── threat_intelligence/
├── utils/
├── visualization/
├── app.py
├── security_engine.py
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

# 🧠 How It Works

## 1. Log Parser

Reads uploaded log files and converts each entry into structured
records.

## 2. Threat Detection

Looks for attack indicators such as: - Brute Force - SQL Injection -
XSS - Malware - PowerShell - Credential Dumping - Reverse Shell -
Privilege Escalation - Data Exfiltration

## 3. Risk Analysis

Assigns a LOW, MEDIUM or HIGH risk score based on detected events.

## 4. IOC Extraction

Extracts: - IP addresses - URLs - Domains - Email addresses - MD5 -
SHA1 - SHA256 - CVE IDs

## 5. MITRE ATT&CK Mapping

Maps detected threats to relevant MITRE ATT&CK techniques.

## 6. Threat Intelligence

Checks extracted IP addresses against VirusTotal and displays reputation
and detection statistics.

## 7. AI Analysis

Uses Ollama with Llama 3.2 to generate: - Executive summary - Findings -
Risk assessment - Recommendations - SOC analyst notes

------------------------------------------------------------------------

# 📊 Dashboard

The dashboard displays:

-   Executive Summary
-   Risk Meter
-   Detection Confidence
-   Threat Severity
-   MITRE Coverage
-   IOC Dashboard
-   VirusTotal Results
-   Timeline
-   Attack Path
-   AI Report

------------------------------------------------------------------------

# 🚀 Installation

``` bash
git clone https://github.com/<your-username>/AI-Security-Analyzer.git
cd AI-Security-Analyzer
pip install -r requirements.txt
python app.py
```

------------------------------------------------------------------------

# 🧪 Testing

Use three sample log files:

-   sample_normal_logs.txt
-   sample_attack_logs.txt
-   sample_web_attack_logs.txt

Verify: - Risk score changes - Threats detected - MITRE mapping
updates - IOC extraction works - VirusTotal results appear - PDF report
downloads

------------------------------------------------------------------------

# 🔮 Future Enhancements

-   SIEM integration
-   Real-time monitoring
-   Email alerts
-   User authentication
-   Threat hunting dashboards
-   Cloud log ingestion

------------------------------------------------------------------------

# 🙌 Author

**Shiwani Rai**

Electronics & Communication Graduate \| Aspiring SOC Analyst \|
Cybersecurity Enthusiast
