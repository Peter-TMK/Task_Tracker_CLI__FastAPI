import json
from datetime import datetime
from models import Task
from typing import List
from fastapi import HTTPException


# File path for JSON database
DB_FILE = 'database.json'

def read_tasks() -> List[Task]:
    try:
        with open(DB_FILE,'r') as file:
            data = file.read().strip()
            if not data:
                return []  # Handle empty file
            tasks = json.loads(data)
            # return [Task(**task) for task in json.load(file)] # Error occurs here
            return [Task(**task) for task in tasks] # Error occurs here
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        with open(DB_FILE,'w') as file:
            file.write('[]') # Reset to an empty list
        raise HTTPException(status_code=500, detail=f"JSON Decode Error: {str(e)}")

def write_tasks(tasks: List[Task]):
    with open(DB_FILE,'w') as file:
        json.dump([task.model_dump() for task in tasks], file, indent=4, default=str)
