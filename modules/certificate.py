import uuid
import json
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_certificate(score, verdict):
    cert_id = str(uuid.uuid4())

    data = {
        "id": cert_id,
        "score": score,
        "verdict": verdict,
        "timestamp": str(datetime.datetime.now())
    }

    # Save to ledger (blockchain simulation)
    try:
        with open("data/ledger.json", "r") as f:
            ledger = json.load(f)
    except:
        ledger = []

    ledger.append(data)

    with open("data/ledger.json", "w") as f:
        json.dump(ledger, f, indent=4)

    # ================= CREATE PDF =================
    file_name = f"certificate_{cert_id}.pdf"

    doc = SimpleDocTemplate(file_name, pagesize=letter)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("<b>DeepShield AI Certificate</b>", styles['Title']))
    content.append(Spacer(1, 20))

    content.append(Paragraph(f"Certificate ID: {cert_id}", styles['Normal']))
    content.append(Paragraph(f"Date: {data['timestamp']}", styles['Normal']))
    content.append(Spacer(1, 20))

    content.append(Paragraph(f"Authenticity Score: {score:.2f}%", styles['Normal']))
    content.append(Spacer(1, 20))

    content.append(Paragraph(f"<b>Final Verdict: {verdict}</b>", styles['Normal']))

    doc.build(content)

    # return BOTH id + file
    return cert_id, file_name
