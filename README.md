# Task Tracker CLI App (FastAPI)

A simple CLI-based application to manage tasks effectively using FastAPI. This app allows you to add, update, delete, and list tasks stored in a JSON file.

## Features

- **Add a Task**: Create a new task with a description.
- **Update a Task**: Modify an existing task’s details.
- **Delete a Task**: Permanently remove a task by its ID.
- **Mark Task Status**: Change task status to `todo`, `in-progress`, or `done`.
- **List Tasks**: View all tasks or filter tasks by status (`todo`, `in-progress`, `done`).

## Task Properties

Each task includes:

- `id`: Unique identifier.
- `description`: Task description.
- `status`: Task status (`todo`, `in-progress`, `done`).
- `createdAt`: Timestamp of task creation.
- `updatedAt`: Timestamp of last update.

## Getting Started

### Prerequisites

- Python 3.8 or later installed.
- FastAPI and Uvicorn installed:
  ```
  pip install fastapi uvicorn
  ```

### Installation

1. Clone this repository:

```
git clone https://github.com/Peter-TMK/Task_Tracker_CLI__FastAPI
```

2. Navigate to the project directory:

```
cd task-tracker-cli
```

3. Install dependencies:

```
pip install -r requirements.txt
```

### Run the Application

**_Start the FastAPI server:_**

```
uvicorn main:app --reload
```

The app will be available at http://127.0.0.1:8000

### API Endpoints

**_Add a Task_**

```
POST /tasks
```

Request: Query parameter description
Response:

```
{
  "message": "Task added successfully",
  "task": {
    "id": 1,
    "description": "Your task description",
    "status": "todo",
    "createdAt": "timestamp",
    "updatedAt": "timestamp"
  }
}
```

**_Update a Task_**

```
PUT /tasks/{task_id}
```

Request: Query parameter description
Response:

```
{
  "message": "Task updated successfully",
  "task": {
    "id": 1,
    "description": "Updated task description",
    "status": "todo",
    "createdAt": "timestamp",
    "updatedAt": "timestamp"
  }
}
```

**_Delete a Task_**

```
DELETE /tasks/{task_id}
```

Response:

```
{
  "message": "Task with ID 1 has been deleted successfully"
}
```

**_Mark a Task as In Progress_**

```
PATCH /tasks/{task_id}/mark-in-progress
```

Response:

```
{
  "message": "Task status updated to 'in-progress'",
  "task": { ... }
}
```

**_Mark a Task as Done_**

```
PATCH /tasks/{task_id}/mark-done
```

Response:

```
{
  "message": "Task status updated to 'done'",
  "task": { ... }
}
```

**_List All Tasks_**

```
GET /tasks
```

Response:

```
{
  "tasks": [
    { "id": 1, "description": "Task 1", "status": "todo", ... },
    { "id": 2, "description": "Task 2", "status": "done", ... }
  ]
}
```

**_List Tasks by Status_**

```
GET /tasks/status/{status}
```

Request: Replace {status} with todo, in-progress, or done.
Response:

```
{
  "tasks": [
    { "id": 1, "description": "Task 1", "status": "todo", ... }
  ]
}
```

**_JSON File Structure_**

Tasks are stored in a tasks.json file in the project directory:

```
[
  {
    "id": 1,
    "description": "Example task",
    "status": "todo",
    "createdAt": "timestamp",
    "updatedAt": "timestamp"
  }
]
```

### Error Handling

- Invalid task ID: Returns 404 Not Found.
- Invalid status for filtering: Returns 400 Bad Request.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

### License

This project is licensed under the MIT License.

```

Feel free to adjust the repository URL, license, or contributing guidelines as necessary. Let me know if you’d like further refinements! 😊
```
