
# Planning

## Idea

Quiero crear un API simple para gestionar tareas.

## Problem

Crear endpoints para CRUD de tareas.

## Objetive

Crear un API RESTful para gestionar tareas.

## MVP (Do it)

Para mantenerlo aterrizado:

```shell
✓ crud de tareas
✓ persistencia de datos en memoria
✓ FastAPI
✓ test unitarios
```

## Don't do it (v1)

Aquí nos protegemos.

```shell
✗ no persistencia en base de datos
✗ Docker automático
✗ FastAPI templates
✗ IA
✗ configuración avanzada
```

## Flow

```shell
Usuario ejecuta proyecto
↓
usuario consume endpoints
↓
Se crean, leen, actualizan, eliminan tareas
↓
Se cierra el programa
↓
Se eliminan las tareas en memoria
```
