"""Task API endpoints."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

tasks = [
    {"id": 1, "task": "Aprender Flask", "completed": True},
    {"id": 2, "task": "Aprender FastAPI", "completed": False},
]

app = FastAPI()


class TaskCreate(BaseModel):
    """Represents a task.

    Attributes:
        id (int): The task ID.
        task (str): The task description.
        completed (bool): Whether the task is completed or not.
    """

    task: str
    completed: bool = False


class TaskResponse(BaseModel):
    """Represents a task response.

    Attributes:
        id (int): The task ID.
        task (str): The task description.
        completed (bool): Whether the task is completed or not.
    """

    id: int
    task: str
    completed: bool


@app.get("/")
def root():
    """Root endpoint that returns the API welcome message.

    Returns:
        dict: The API welcome message.
    """
    return {"message": "Welcome to the Task API created whit FastAPI"}


@app.get("/tasks")
def get_tasks():
    """Get tasks endpoint that returns the list of tasks.

    Returns:
        dict: The list of tasks.
    """
    return {"tasks": tasks}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """Get a task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.

    Returns:
        dict: The task data.
    """
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "task": task.task,
        "completed": task.completed,
    }

    tasks.append(new_task)

    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, item: TaskCreate):
    """Update a task by its ID.

    Args:
        task_id (int): The ID of the task to update.
        item (TaskCreate): The updated task data.

    Returns:
        TaskResponse: The updated task data.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = item.task
            task["completed"] = item.completed
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Delete a task by its ID.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        dict: The updated list of tasks.
    """
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
