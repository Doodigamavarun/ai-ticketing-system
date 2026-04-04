from fastapi import APIRouter

router = APIRouter()

employees = [
    {"name": "Varun", "department": "IT", "skills": ["Access"], "load": 2, "available": True},
    {"name": "Ravi", "department": "HR", "skills": ["Leave"], "load": 1, "available": True},
]
@router.get("/employees")
def get_employees():
    return employees
