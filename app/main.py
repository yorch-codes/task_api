"""Task API endpoints."""

from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from app.db.database import Base, engine, get_db
from app.models.task import Task

Base.metadata.create_all(bind=engine)

app = FastAPI()


class TaskCreate(BaseModel):
    """Represents a task.

    Attributes:
        id (int): The task ID.
        task (str): The task description.
        completed (bool): Whether the task is completed or not.
    """

    task: str
    description: str = ""
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
    return db.query(Task).all()


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """Get a task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.

    Returns:
        dict: The task data.
    """
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """Create a new task.

    Args:
        task (TaskCreate): The task data to create.

    Returns:
        dict: The created task data.
    """
    new_task = Task(
        task=task.task,
        description=task.description,
        completed=task.completed,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, item: TaskCreate, db: Session = Depends(get_db)):
    """Update a task by its ID.

    Args:
        task_id (int): The ID of the task to update.
        item (TaskCreate): The updated task data.

    Returns:
        TaskResponse: The updated task data.
    """
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.task = item.task
    task.description = item.description
    task.completed = item.completed

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
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}
