"""Test suite for the Task API."""

from fastapi.testclient import TestClient

from app.main import app, tasks

client = TestClient(app)

# Initial tasks for testing
INITIAL_TASKS = [
    {"id": 1, "task": "Aprender Flask", "completed": True},
    {"id": 2, "task": "Aprender FastAPI", "completed": False},
]


# Clean the tasks list before each test
def setup_function():
    """Set up the initial tasks before each test."""
    tasks.clear()
    tasks.extend(INITIAL_TASKS)


# Endpoints tests
def test_read_main():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Task API created whit FastAPI"
    }


def test_read_tasks():
    """Test the tasks endpoint."""
    response = client.get("/tasks")

    assert response.status_code == 200

    body = response.json()

    assert "tasks" in body
    assert isinstance(body["tasks"], list)


def test_create_task():
    """Test the create task endpoint."""
    response = client.post(
        "/tasks/", json={"task": "Aprender pytest", "completed": False}
    )

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 3
    assert body["task"] == "Aprender pytest"
    assert body["completed"] is False


def test_update_task():
    """Test the update task endpoint."""
    response = client.put(
        "/tasks/1", json={"task": "Aprender pytest", "completed": True}
    )

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 1
    assert body["task"] == "Aprender pytest"
    assert body["completed"] is True


def test_delete_task():
    """Test the delete task endpoint."""
    response = client.delete("/tasks/1")

    assert response.status_code == 200

    body = response.json()

    assert body["message"] == "Task deleted successfully"

    response = client.get("/tasks/1")

    assert response.status_code == 404


# Error tests
def test_get_task_not_found():
    """Test the get task not found endpoint."""
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_update_task_not_found():
    """Test the update task not found endpoint."""
    response = client.put(
        "/tasks/999",
        json={"task": "Test", "completed": False},
    )

    assert response.status_code == 404


def test_delete_task_not_found():
    """Test the delete task not found endpoint."""
    response = client.delete("/tasks/999")

    assert response.status_code == 404


def test_create_task_invalid_payload():
    """Test the create task invalid payload endpoint."""
    response = client.post("/tasks/", json={"completed": False})

    assert response.status_code == 422
