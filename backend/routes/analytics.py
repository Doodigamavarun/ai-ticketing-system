from fastapi import APIRouter
from routes.ticket import tickets

router = APIRouter()

@router.get("/analytics")
def stats():
    total = len(tickets)
    resolved = len([t for t in tickets if t["status"] == "Resolved"])
    assigned = len([t for t in tickets if t["status"] == "Assigned"])

    # 🤖 Auto resolved
    auto_resolved = len([t for t in tickets if "auto_response" in t])

    # 📊 Department-wise count
    dept_count = {}
    for t in tickets:
        dept = t["ai"]["department"]
        dept_count[dept] = dept_count.get(dept, 0) + 1

    # 📈 Category count
    category_count = {}
    for t in tickets:
        cat = t["ai"]["category"]
        category_count[cat] = category_count.get(cat, 0) + 1

    # ✅ Success rate
    success_rate = (auto_resolved / total * 100) if total > 0 else 0

    return {
        "total_tickets": total,
        "resolved": resolved,
        "assigned": assigned,
        "auto_resolved": auto_resolved,
        "department_load": dept_count,
        "category_breakdown": category_count,
        "auto_resolution_success_rate": f"{success_rate:.2f}%"
    }