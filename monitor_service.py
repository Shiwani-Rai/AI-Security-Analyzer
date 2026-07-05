from monitor.log_monitor import start_monitor
from engine.security_engine import analyze_security
from report_generator.pdf_report import generate_pdf_report
import shared_data
from datetime import datetime


LOG_FILE = r"D:\project\AI-Security-Analyzer\logs\sample.log"


def callback(file):

    print("\n========== AUTO ANALYSIS ==========\n")

    result = analyze_security(file)

    pdf = generate_pdf_report(result)

    shared_data.latest_result = result
    shared_data.latest_pdf = pdf
    shared_data.last_updated = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    print("Dashboard Updated Successfully!")

    print("\n===================================\n")


def start():

    print("Starting Real-Time Monitor...")

    start_monitor(LOG_FILE, callback)