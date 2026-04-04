from fastapi import APIRouter
from ai_engine import analyze_ticket

router = APIRouter()

tickets = []

# 👨‍💼 Employee directory
employees = [
    {"name": "Varun", "department": "IT", "skills": ["Access"], "load": 2, "available": True},
    {"name": "Ravi", "department": "HR", "skills": ["Leave"], "load": 1, "available": True},
    {"name": "Anil", "department": "Finance", "skills": ["Billing"], "load": 3, "available": True},
]

# 🎯 Assign best employee
def assign_employee(department):
    available_employees = [
        emp for emp in employees
        if emp["department"] == department and emp["available"]
    ]

    if not available_employees:
        return "No available employee"

    best = min(available_employees, key=lambda x: x["load"])
    best["load"] += 1
    return best["name"]


# 🎫 Create ticket
@router.post("/ticket")
def create_ticket(ticket: dict):
    ai_result = analyze_ticket(ticket["description"])

    ticket["ai"] = ai_result

    if ai_result["resolution"] == "auto":
        ticket["status"] = "Resolved"
        ticket["auto_response"] = f"""
        Hi, your issue '{ticket['title']}' has been resolved.
        Please try resetting your password.
        Was this helpful? Yes / No
        """
    else:
        ticket["status"] = "Assigned"
        assigned = assign_employee(ai_result["department"])
        ticket["assigned_to"] = assigned

    tickets.append(ticket)
    return ticket


# 🔄 Update status
@router.put("/ticket/{index}")
def update_status(index: int, status: str):
    tickets[index]["status"] = status
    return tickets[index]


# 📋 Get all tickets (VERY IMPORTANT ✅)
@router.get("/tickets")
def get_tickets():
    return tickets