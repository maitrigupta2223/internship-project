from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(results, score):

    doc = SimpleDocTemplate("reports/audit_report.pdf")
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Linux Security Audit Report", styles['Title']))
    content.append(Spacer(1,10))
    content.append(Paragraph(f"Security Score: {score}%", styles['Heading2']))

    for name, result in results.items():

        status = "PASS" if result[0] else "FAIL"

        content.append(Spacer(1,10))
        content.append(Paragraph(f"{name}: {status}", styles['Normal']))
        content.append(Paragraph(result[1], styles['Normal']))

    doc.build(content)
