# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework that handles HTTP requests, validates input data, and persists data in memory or a database. You'll practice API design, request handling, response serialization, and error handling.

## 📝 Tasks

### 🛠️ Create a Task Management API

#### Description
Design and implement a REST API for managing tasks (create, read, update, delete operations). The API should support different HTTP methods and return appropriate status codes and error messages.

#### Requirements
Completed program should:

- Define a Task data model with fields like id, title, description, and completed status
- Implement GET endpoint to retrieve all tasks
- Implement GET endpoint to retrieve a single task by id
- Implement POST endpoint to create a new task with request body validation
- Implement PUT endpoint to update an existing task
- Implement DELETE endpoint to remove a task
- Return appropriate HTTP status codes (200, 201, 400, 404, 500 as applicable)
- Include proper error handling with descriptive error messages
- Use Pydantic models for request/response validation
- Use the provided `starter-code.py` as scaffolding and reference

### 🛠️ Add Filtering and Pagination (Optional)

#### Description
Extend your API with advanced features like filtering tasks by completion status and implementing pagination for list endpoints.

#### Requirements
Completed program should:

- Add query parameters to filter tasks by completed status
- Implement pagination with limit and offset/skip parameters
- Return metadata about pagination (total count, current page, etc.)
- Maintain backward compatibility with the basic list endpoint
