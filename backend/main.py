from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import ticket, employee, analytics

app = FastAPI()

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ticket.router)
app.include_router(employee.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message": "AI Ticketing System Running"}