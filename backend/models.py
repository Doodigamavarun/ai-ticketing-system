from pydantic import BaseModel

class Ticket(BaseModel):
    title: str
    description: str
    status: str = "New"
