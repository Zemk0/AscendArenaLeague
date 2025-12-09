from fastapi import FastAPI
from routers import users, teams, tournaments

app = FastAPI(title="Tournament API")

app.include_router(users.router)
app.include_router(teams.router)
app.include_router(tournaments.router)

@app.get("/")
async def root():
    return {"message": "Tournament API is running"}
