from fastapi import FastAPI
from fastapi import HTTPException
from datetime import datetime
from crud import read_tasks, write_tasks
from models import Task

app = FastAPI()

# Root endpoint
@app.get('/')
def read_root():
    return {'message': 'Welcome to the Task Tracker CLI API!'}

# add a task
@app.post('/tasks')
def add_task(description: str):
    tasks = read_tasks()
    task_id = max([task.id for task in tasks], default=0) + 1
    new_task = Task(
        id = task_id,
        description = description,
        status = "todo",
        createdAt = datetime.now(),
        updatedAt = None
    )
    tasks.append(new_task)
    write_tasks(tasks)
    return {'message': 'Task added successfully', 'task': new_task}

# update a task
@app.put('/tasks/{task_id}')
def update_task(task_id:int, description:str):
    tasks = read_tasks()
    for task in tasks:
        # print(task)
        if task.id == task_id:
            task.description = description
            task.updatedAt = datetime.now()
            write_tasks(tasks)
            return {'message': 'Task updated successfully', 'task': task}

    # If no task with the given ID is found, raise an exception
    raise HTTPException(status_code=404, detail='Task NOT found!')

# update a task status to 'in-progress'
@app.patch('/tasks/{task_id}/in_progress')
def task_in_progress(task_id: int):
    tasks = read_tasks()
    for task in tasks:
        if task.id == task_id:
            task.status = 'in_progress'
            task.updatedAt = datetime.now()
            write_tasks(tasks)
            return {'message': 'Task status has been updated to \'in-progress\' ', 'task': task}
    # If no task with the given ID is found, raise an exception
    raise HTTPException(status_code=404, detail='Task NOT found!')

# update a task status to 'done'
@app.patch('/tasks/{task_id}/done')
def task_done(task_id: int):
    tasks = read_tasks()
    for task in tasks:
        if task.id == task_id:
            task.status = 'done'
            task.updatedAt = datetime.now()
            write_tasks(tasks)
            print({'message': 'Task status has been updated to \'done\' ', 'task': task})
            return {'message': 'Task status has been updated to \'done\' ', 'task': task}
    # If no task with the given ID is found, raise an exception
    raise HTTPException(status_code=404, detail='Task NOT found!')

# delete a task by ID
@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    tasks = read_tasks()
    not_deleted_tasks = [task for task in tasks if task.id != task_id]

    if len(tasks) == len(not_deleted_tasks):
        raise HTTPException(status_code=404, detail='Task NOT found!')
    write_tasks(not_deleted_tasks)
    return {"message": f"Task with ID {task_id} has been deleted successfully"}

# list all tasks
@app.get('/tasks')
def list_all_tasks():
    tasks = read_tasks()
    return tasks

# list tasks by status
@app.get('/tasks/status/{status}')
def list_tasks_by_status(status: str):
    tasks = read_tasks()
    valid_statuses = {'todo', 'in_progress', 'done'}
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail='Status NOT found!')

    tasks = read_tasks()
    filtered_tasks = [task for task in tasks if task.status == status]
    return {'tasks': filtered_tasks}
