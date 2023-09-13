from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

""" This line creates all the tables(from models in models.py file) in sqlalchemy after checking if there is any new model.
    But the problem is, if you want to add or delete a column from a table, you have to delete whole table and create a new one with changes.
    That's why we use alembic,  alembic will automatically check the changes. You just have to create a revision and upgrade.
    As alembic will handle database migration, we no longer need this line to create the tables
"""
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# origins = [
#     "https://www.google.com",
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

origins = ["*"]    #this means i am allowing all origins to access my api

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def index():
    return "Hello"