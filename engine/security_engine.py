import traceback
from log_parser.log_parser import read_logs
from detector.threat_detector import analyze_logs
from detector.risk_analyzer import calculate_risk
from detector.incident_summary import generate_summary
from detector.threat_patterns import detect_patterns
from ioc_extractor.extractor import extract_iocs
from ai_engine.ai_analyzer import analyze_with_ai
from detector.mitre_mapper import map_to_mitre
from threat_intelligence.virustotal import check_ip
from threat_intelligence.geolocation import get_ip_info
from utils.ioc_formatter import build_ioc_table
from utils.timeline_builder import build_timeline
from utils.analytics import build_analytics
from analytics.ioc_analytics import build_ioc_analytics  
from analytics.threat_severity import build_threat_severity  
from filters.advanced_filter import filter_logs
from analytics.threat_statistics import build_threat_statistics
from engine.incident_playbook import generate_playbook  
from visualization.attack_path import build_attack_path
from analytics.mitre_statistics import build_mitre_statistics
from analytics.detection_confidence import build_detection_confidence

# NOTE: Ensure build_attack_path is imported from its correct module here, e.g.:
# from utils.attack_path_builder import build_attack_path

def analyze_security(file_path):
    logs = read_logs(file_path)
    filtered_logs = filter_logs(logs, "")

    summary = analyze_logs(logs)

    threats = detect_patterns(logs)
    attack_path = build_attack_path(threats)

    risk_data = calculate_risk(summary, threats)

    incident = generate_summary(summary, risk_data)
    
    mitre = map_to_mitre(threats)
    
    mitre_statistics = build_mitre_statistics(mitre) 

    iocs = extract_iocs(logs)
    
    # -----------------------------
    # VirusTotal IP Analysis
    # -----------------------------
    vt_results = []
    for ip in iocs["ips"]:
        result = check_ip(ip)
        if result:
            vt_results.append({
                "ip": ip,
                "country": result.get("country", "Unknown"),
                "reputation": result.get("reputation", "Unknown"),
                "malicious": result.get("malicious", 0),
                "suspicious": result.get("suspicious", 0),
                "harmless": result.get("harmless", 0),
                "undetected": result.get("undetected", 0)
            })
        
    threat_statistics = build_threat_statistics(vt_results)

    geo_results = []
    for ip in iocs["ips"]:
        geo_results.append(get_ip_info(ip))
    
    ioc_table = build_ioc_table(iocs, vt_results)

    ioc_analytics = build_ioc_analytics(iocs)

    threat_severity = build_threat_severity(threats)  

    timeline = build_timeline(logs, threats)

    analytics = build_analytics(threats, mitre, iocs, risk_data)

    ai_report = analyze_with_ai(logs, threats, risk_data)

    playbook = generate_playbook(threats)  

    detection_confidence = build_detection_confidence(threats, risk_data)

    return {
        "logs": filtered_logs,
        "summary": summary,
        "risk": risk_data,
        "incident": incident,
        "threats": threats,
        "attack_path": attack_path,
        "mitre": mitre,
        "mitre_statistics": mitre_statistics,
        "iocs": iocs,
        "virustotal": vt_results,
        "threat_statistics": threat_statistics,
        "geolocation": geo_results,
        "ioc_table": ioc_table,
        "ioc_analytics": ioc_analytics,
        "threat_severity": threat_severity,
        "timeline": timeline,
        "analytics": analytics,
        "ai_report": ai_report,
        "playbook": playbook,
        "detection_confidence": detection_confidence
    }