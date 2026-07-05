# from log_parser.log_parser import read_logs
# from detector.threat_detector import analyze_logs
# from detector.risk_analyzer import calculate_risk
# from detector.incident_summary import generate_summary
# from detector.threat_patterns import detect_patterns
# from ai_engine.ai_analyzer import analyze_with_ai
# from report_generator.html_report import generate_html_report
# from ioc_extractor.extractor import extract_iocs
from engine.security_engine import analyze_security




# result = analyze_security("logs/sample.log")

# print(result)




# logs = read_logs("logs/sample.log")
# iocs = extract_iocs(logs)

# print("\n=== INDICATORS OF COMPROMISE ===\n")

# print("IP Addresses:")
# for ip in iocs["ips"]:
#     print("-", ip)

# print("\nEmail Addresses:")
# for email in iocs["emails"]:
#     print("-", email)

# print("\nURLs:")
# for url in iocs["urls"]:
#     print("-", url)

# print("\n=== SECURITY LOGS ===\n")

# print("\n=== PARSED LOGS ===\n")

# for log in logs:
#     print(log)

# results = analyze_logs(logs)
# risk_data = calculate_risk(results)
# incident = generate_summary(results, risk_data)
# threats = detect_patterns(logs)



# print("\n=== SECURITY SUMMARY ===\n")

# print(f"INFO Events: {results['INFO']}")
# print(f"WARNING Events: {results['WARNING']}")
# print(f"ERROR Events: {results['ERROR']}")

# print("\n=== RISK ANALYSIS ===\n")

# print(f"Risk Score: {risk_data['score']}")
# print(f"Risk Level: {risk_data['risk']}")

# print("\n=== INCIDENT SUMMARY ===\n")

# for finding in incident["findings"]:
#     print("-", finding)

# print("\nThreat Assessment:")
# print(incident["threat"])

# print("\nRecommendations:")

# for rec in incident["recommendations"]:
#     print("-", rec)
    
# print("\n=== THREAT DETECTION ===\n")

# if threats:
#     for threat in threats:
#         print("-", threat)

# else:
#     print("No known threats detected.")
    
# print("\n=== AI SECURITY ANALYSIS ===\n")

# ai_report = analyze_with_ai(
#     logs,
#     threats,
#     risk_data
# )

# print(ai_report)   

# generate_html_report(
#     ai_report,
#     threats,
#     risk_data
# )