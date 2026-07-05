from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf_report(result):

    reports_folder = "reports"

    if not os.path.exists(reports_folder):
        os.makedirs(reports_folder)

    pdf_path = os.path.join(
        reports_folder,
        "security_report.pdf"
    )

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>AI Security Analyzer Report</b>", styles["Title"])
    )

    story.append(
        Paragraph("<br/><br/>", styles["Normal"])
    )

    story.append(
        Paragraph(
            f"<b>Risk Level:</b> {result['risk']['risk']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk Score:</b> {result['risk']['score']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Detected Threats</b>", styles["Heading2"])
    )

    if result["threats"]:

        for threat in result["threats"]:

            story.append(
                Paragraph(f"• {threat}", styles["Normal"])
            )

    else:

        story.append(
            Paragraph("No threats detected.", styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Indicators of Compromise</b>", styles["Heading2"])
    )

    for ip in result["iocs"]["ips"]:

        story.append(
            Paragraph(ip, styles["Normal"])
        )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>Incident Summary</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            result["incident"]["threat"],
            styles["Normal"]
        )
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    story.append(
        Paragraph("<b>AI Analysis</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            result["ai_report"].replace("\n", "<br/>"),
            styles["Normal"]
        )
    )

    doc.build(story)

    return pdf_path