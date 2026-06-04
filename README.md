
# Task API

A simple API Tasks created whit FastAPI, use the local memory to store tasks.

---

## Features

* Create tasks
* Read tasks
* Update tasks
* Delete tasks

---

## Tech Stack

* Python 3
* FastAPI
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
python main.py
```

```bash
# Run the application in linux/MacOS
python3 main.py
```

Run the tests:

```bash
pytest
```

---

## Project Structure

```text
project/
├── README.md
├── main.py
├── docs/
│   ├── planning.md
│   ├── architecture.md
├── tests/
    ├── test_main.py
```

---

## API Documentation

Once the server is running, interactive documentation is available at:

[Swagger Interactive API Docs](http://localhost:8000/docs)

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

* [ ] Data persistence
* [ ] Authentication
* [ ] Authorization
* [ ] Deployment
* [X] API documentation
* [X] tests

---

## License

MIT
