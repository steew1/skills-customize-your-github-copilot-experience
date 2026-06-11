"""
Task Management REST API starter code
Students should expand on this foundation to complete the assignment.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(title="Task Management API", version="1.0.0")

# Data Models using Pydantic
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# In-memory data store (replace with database in production)
tasks_db: dict = {}
next_id = 1

# API Endpoints

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to Task Management API"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    """Retrieve all tasks"""
    # TODO: Implement this endpoint
    pass

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """Retrieve a single task by ID"""
    # TODO: Implement this endpoint
    pass

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """Create a new task"""
    # TODO: Implement this endpoint
    pass

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskBase):
    """Update an existing task"""
    # TODO: Implement this endpoint
    pass

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    """Delete a task"""
    # TODO: Implement this endpoint
    pass

# Optional: Advanced filtering and pagination
@app.get("/tasks/filter", response_model=List[Task])
def filter_tasks(completed: Optional[bool] = None, skip: int = 0, limit: int = 10):
    """Filter and paginate tasks"""
    # TODO: Implement this endpoint (optional)
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
