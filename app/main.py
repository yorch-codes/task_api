"""Task API endpoints."""

from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import Base, engine, get_db
from app.models.task import Task

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Create & Response Task Models
class TaskCreate(BaseModel):
    """Represents a task.

    Attributes:
        task (str): The task title.
        description (str): The task description.
        completed (bool): Task status.
    """

    task: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)
    completed: bool = False


class TaskResponse(BaseModel):
    """Represents a task response."""

    id: int
    task: str
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Endpoints
@app.get("/")
def root():
    """Root endpoint that returns the API welcome message.

    Returns:
        dict: The API welcome message.
    """
    return {"message": "Welcome to the Task API created whit FastAPI"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    """Get tasks endpoint that returns the list of tasks.

    Returns:
        dict: The list of tasks.
    """
    stmt = select(Task).order_by(Task.id.asc())
    result = db.execute(stmt).scalars().all()
    return result


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """Get a task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.

    Returns:
        dict: The task data.
    """
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@app.post("/tasks/", response_model=TaskResponse)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    """Create a new task.

    Args:
        payload (TaskCreate): The task data to create.

    Returns:
        dict: The created task data.
    """
    new_task = Task(
        task=payload.task,
        description=payload.description,
        completed=payload.completed,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int, payload: TaskCreate, db: Session = Depends(get_db)
):
    """Update a task by its ID.

    Args:
        task_id (int): The ID of the task to update.
        item (TaskCreate): The updated task data.

    Returns:
        TaskResponse: The updated task data.
    """
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    task.task = payload.task
    task.description = payload.description
    task.completed = payload.completed

    db.commit()
    db.refresh(task)

    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        dict: The updated list of tasks.
    """
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}
