
# Architecture

## Folder Structure

```text
src/
├── main.py
├── generator.py
└── templates.py
```

## Component Diagram

```mermaid
flowchart TD

    A[main.py<br>CLI Entry Point]
    B[generator.py<br>File & Folder Creation]
    C[templates.py<br>Markdown Templates]

    A --> B
    B --> C
```

## Responsibilities

### main.py
- recibe argumentos
- inicia ejecución

### generator.py
- crea estructura
- escribe archivos

### templates.py
- contiene templates
- centraliza contenido markdown
```

