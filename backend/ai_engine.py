def analyze_ticket(text):
    text = text.lower()

    if "login" in text:
        return {
            "category": "Access",
            "summary": "User cannot login",
            "severity": "Medium",
            "resolution": "auto",
            "department": "IT",
            "confidence": "90%"
        }

    elif "server" in text:
        return {
            "category": "Server",
            "summary": "Server issue detected",
            "severity": "Critical",
            "resolution": "assign",
            "department": "Engineering",
            "confidence": "95%"
        }

    elif "leave" in text:
        return {
            "category": "HR",
            "summary": "Leave request",
            "severity": "Low",
            "resolution": "assign",
            "department": "HR",
            "confidence": "88%"
        }

    return {
        "category": "Other",
        "summary": "General issue",
        "severity": "Low",
        "resolution": "assign",
        "department": "Support",
        "confidence": "80%"
    }