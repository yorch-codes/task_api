"""Test suite for the Task API."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


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
    assert isinstance(response.json(), list)


def test_create_task():
    """Test the create task endpoint."""
    response = client.post(
        "/tasks/",
        json={
            "task": "Aprender pytest",
            "description": "Testing",
            "completed": False,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["task"] == "Aprender pytest"
    assert body["description"] == "Testing"
    assert body["completed"] is False

    assert "id" in body
    assert "created_at" in body
    assert "updated_at" in body


def test_update_task():
    """Test the update task endpoint."""

    created = client.post(
        "/tasks/",
        json={
            "task": "Original",
            "description": "Original",
            "completed": False,
        },
    )

    task_id = created.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "task": "Aprender pytest",
            "description": "Actualizada",
            "completed": True,
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == task_id
    assert body["task"] == "Aprender pytest"
    assert body["description"] == "Actualizada"
    assert body["completed"] is True


def test_delete_task():
    """Test the delete task endpoint."""

    created = client.post(
        "/tasks/",
        json={
            "task": "Eliminar",
            "description": "",
            "completed": False,
        },
    )

    task_id = created.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    body = response.json()

    assert body["message"] == "Task deleted successfully"

    response = client.get(f"/tasks/{task_id}")

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
