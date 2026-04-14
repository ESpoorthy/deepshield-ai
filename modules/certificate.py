import uuid
import json

def generate_certificate(score, verdict):
    cert_id = str(uuid.uuid4())

    data = {
        "id": cert_id,
        "score": score,
        "verdict": verdict
    }

    try:
        with open("data/ledger.json", "r") as f:
            ledger = json.load(f)
    except:
        ledger = []

    ledger.append(data)

    with open("data/ledger.json", "w") as f:
        json.dump(ledger, f, indent=4)

    return cert_id
