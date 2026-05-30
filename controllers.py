from flask import render_template, request
import config


def show_home():

    todos = list(
        config.collection.find(
            {
                "status": "active"
            }
        )
    )

    return render_template(
        "index.html",
        todos=todos,
        history_mode=False
    )


def show_history():

    todos = list(
        config.collection.find()
    )

    return render_template(
        "index.html",
        todos=todos,
        history_mode=True
    )


def add_todo():

    task = request.form["task"]

    config.collection.insert_one(
        {
            "task": task,
            "status": "active"
        }
    )

    return show_home()


def delete_Todo(index):

    active_todos = list(
        config.collection.find(
            {
                "status": "active"
            }
        )
    )

    config.collection.update_one(
        {
            "_id": active_todos[index]["_id"]
        },
        {
            "$set": {
                "status": "inactive"
            }
        }
    )

    return show_home()


def update_todo(index):

    task = request.form["task"]

    active_todos = list(
        config.collection.find(
            {
                "status": "active"
            }
        )
    )

    config.collection.update_one(
        {
            "_id": active_todos[index]["_id"]
        },
        {
            "$set": {
                "task": task
            }
        }
    )

    return show_home()


def edit_todo(index):

    active_todos = list(
        config.collection.find(
            {
                "status": "active"
            }
        )
    )

    return render_template(
        "edit.html",
        index=index,
        todo=active_todos[index]["task"]
    )