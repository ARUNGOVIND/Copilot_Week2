"""
FastAPI Todo Application - Starter Code
Complete this assignment by implementing the Todo and User management API.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# Initialize FastAPI application
app = FastAPI(title="Todo API", version="1.0.0")

# Data Models
class TodoCreate(BaseModel):
    """Model for creating a new todo"""
    title: str
    description: Optional[str] = None
    completed: bool = False


class Todo(TodoCreate):
    """Model for a todo item with an ID"""
    id: int


class UserCreate(BaseModel):
    """Model for creating a new user"""
    name: str
    email: EmailStr


class User(UserCreate):
    """Model for a user with an ID"""
    id: int


# In-memory storage
todos_db: List[dict] = []
users_db: List[dict] = []
next_todo_id = 1
next_user_id = 1


# TODO: Implement the following endpoints

# User Management Endpoints
# POST /users - Create a new user
# GET /users - Retrieve all users
# GET /users/{user_id} - Retrieve a specific user
# DELETE /users/{user_id} - Delete a user


# Todo Management Endpoints
# POST /todos - Create a new todo
# GET /todos - Retrieve all todos
# GET /todos/{todo_id} - Retrieve a specific todo
# PUT /todos/{todo_id} - Update a todo
# DELETE /todos/{todo_id} - Delete a todo
# GET /users/{user_id}/todos - Retrieve all todos for a specific user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)