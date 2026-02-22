# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you'll build a modern REST API using the FastAPI framework. You'll learn how to create endpoints, handle HTTP requests and responses, work with request validation, and structure a professional API that can serve data to client applications.

## 📝 Tasks

### 🛠️ Create a Basic Todo API

#### Description
Build a simple REST API that manages a list of todo items. The API should support creating, retrieving, updating, and deleting todos. You'll use FastAPI to define endpoints and manage request/response handling.

#### Requirements
Your API must:

- Define endpoints for GET (retrieve all todos), GET (retrieve by ID), POST (create), PUT (update), and DELETE operations
- Use proper HTTP status codes (200 for success, 201 for created, 404 for not found)
- Validate request data using Pydantic models
- Store todos in memory (a list or dictionary)
- Include clear error messages for invalid requests
- Test all endpoints using the interactive API documentation (`/docs`)


### 🛠️ Add User Management

#### Description
Extend your API with user management functionality. Create endpoints to manage users and associate todos with specific users.

#### Requirements
Your implementation should:

- Create a User model with fields like id, name, and email
- Add endpoints to create, retrieve, and delete users
- Associate todos with users (each todo belongs to a user)
- Add filtering capability to retrieve todos for a specific user
- Implement input validation for email format and required fields
- Return appropriate error responses for invalid data