from fastapi import FastAPI
from .api.user_routes import login_route, register_route
from .api.token_routes.token_routes import router as token_router
from fastapi.middleware.cors import CORSMiddleware
from .db.database import engine as userEngine
from .db.database import Base as UserBase

app = FastAPI()

UserBase.metadata.create_all(bind=userEngine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_route.router)
app.include_router(register_route.router)
app.include_router(token_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

