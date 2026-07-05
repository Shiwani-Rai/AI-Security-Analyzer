from datetime import datetime
import os
import threading
import uuid  # Added uuid import here

from flask import Flask, render_template, request, send_file

from engine.security_engine import analyze_security
import monitor_service
from report_generator.pdf_report import generate_pdf_report
import shared_data

app = Flask(__name__)


UPLOAD_FOLDER = "logs"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    # Get uploaded file
    logfile = request.files["logfile"]

    # Save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], logfile.filename)

    logfile.save(filepath)

    # Analyze the uploaded log
    result = analyze_security(filepath)

    print(result.keys())

    # Generate the PDF report based on analysis results
    pdf_path = generate_pdf_report(result)

    # Store the latest analysis globally via shared_data
    shared_data.latest_result = result
    shared_data.latest_pdf = pdf_path
    shared_data.last_updated = datetime.now().strftime("%d %b %Y %H:%M:%S")

    # ==========================
    # DEBUG OUTPUT
    # ==========================
    print("\n========== RESULT ==========\n")
    print(result)
    print("\n============================\n")

    # Send updated result details to HTML page
    return render_template(
        "result.html",
        result=result,
        pdf_path=pdf_path,
        last_updated=shared_data.last_updated,
        analyst="SOC Analyst",
        case_id=str(uuid.uuid4())[:8].upper(),
        version="v1.0",
    )


@app.route("/dashboard")
def dashboard():
    if shared_data.latest_result is None:
        return "No analysis available yet."

    # Pass the last_updated timestamp to the template
    return render_template(
        "result.html",
        result=shared_data.latest_result,
        pdf_path=shared_data.latest_pdf,
        last_updated=getattr(shared_data, "last_updated", None),
    )


@app.route("/api/dashboard")
def api_dashboard():
    return {
        "result": shared_data.latest_result,
        "last_updated": shared_data.last_updated,
    }


@app.route("/download_pdf")
def download_pdf():
    return send_file("reports/security_report.pdf", as_attachment=True)


if __name__ == "__main__":
    # Start the real-time monitor in a separate daemon thread
    monitor_thread = threading.Thread(target=monitor_service.start, daemon=True)
    monitor_thread.start()

    # Run the Flask app without the reloader to prevent duplicate threads
    app.run(debug=True, port=8000, use_reloader=False)