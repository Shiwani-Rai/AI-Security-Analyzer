from datetime import datetime

def generate_html_report(ai_report, threats, risk):

    threat_list = ""

    if threats:
        for threat in threats:
            threat_list += f"<li>{threat}</li>"
    else:
        threat_list = "<li>No threats detected</li>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Security Report</title>

    <style>

    body {{
        background:#f4f6f9;
        font-family:Arial;
        margin:40px;
    }}

    .container {{
        background:white;
        padding:30px;
        border-radius:10px;
        box-shadow:0px 0px 10px gray;
    }}

    h1 {{
        color:#d32f2f;
        text-align:center;
    }}

    h2 {{
        color:#1565c0;
    }}

    pre {{
        white-space:pre-wrap;
        font-size:15px;
    }}

    </style>

</head>

<body>

<div class="container">

<h1>AI Security Incident Report</h1>

<p><b>Generated:</b> {datetime.now()}</p>

<h2>Risk Level</h2>

<p>{risk["risk"]}</p>

<h2>Detected Threats</h2>

<ul>

{threat_list}

</ul>

<h2>AI Security Analysis</h2>

<pre>

{ai_report}

</pre>

</div>

</body>

</html>
"""

    with open("reports/security_report.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("\nHTML report generated successfully!")