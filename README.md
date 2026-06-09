
# Task API

A simple API Tasks created whit FastAPI, use the PostgreSQL database to store tasks with SQLAlchemy ORM.

---

## Features

* Create tasks
* Read tasks
* Update tasks
* Delete tasks

---

## Tech Stack

* Python3
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pytest

---

## Installation

Clone the repository:

```bash
git clone git@github.com:yorch-codes/task_api.git
cd task_api
```

Create environment and install dependencies:

### Using uv

```bash
# Create environment with uv
uv venv
```

```bash
# Use uv to install dependencies
uv pip install -r requirements.txt
```

### Using pip

```bash
# Create environment with pip in windows
python -m venv venv
```

```bash
# Create environment with pip in linux/macOS
python3 -m venv venv
```

```bash
# Use pip to install dependencies
pip install -r requirements.txt
```

---

## Usage

Run the project:

```bash
# Run the application in windows
uvicorn app.main:app --reload
```

```bash
# Run the application in linux/MacOS
uvicorn app.main:app --reload
```

Run the tests:

```bash
pytest
```

---

## Project Structure

```text
task_api/
├── README.md
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── task.py
│   ├── main.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
├── docs/
│   ├── planning.md
│   ├── architecture.md
├── tests/
    ├── test_main.py
├── postman/
│   ├── Task_API.postman_collection.json
├── requirements.txt
├── .env
├── .gitignore
```

---

## API Documentation

Once the server is running, interactive documentation is available at:

[Swagger Interactive API Docs](http://localhost:8000/docs)
[ReDoc API Docs](http://localhost:8000/redoc)

### Postman Collection

A Postman collection is included in the repository:

[Postman Collection](postman/Task_API.postman_collection.json)

Import it into Postman to test all endpoints quickly.

---

## Aditional Documentation

Project documentation:

* Planning → [Planning](docs/planning.md)
* Architecture → [Architecture](docs/architecture.md)

---

## Roadmap

Planned improvements:

* [X] Data persistence
* [ ] Authentication
* [ ] Authorization
* [ ] Deployment
* [X] API documentation
* [X] tests

---

## License

MIT
