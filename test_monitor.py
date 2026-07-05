from monitor.log_monitor import start_monitor

from engine.security_engine import analyze_security


def callback(file):

    print("\n===================================")
    print("🚨 New Log Detected")
    print("===================================\n")

    result = analyze_security(file)

    print("\n========== ANALYSIS ==========\n")

    print("Risk Level :", result["risk"]["risk"])
    print("Risk Score :", result["risk"]["score"])
    print("Threats    :", result["threats"])
    print("MITRE      :", result["mitre"])
    print("IOCs       :", result["iocs"])

    print("\n==============================\n")


log_file = r"D:\project\AI-Security-Analyzer\logs\sample.log"

start_monitor(log_file, callback)