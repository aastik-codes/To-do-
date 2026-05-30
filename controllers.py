from flask import render_template, request
import config 


def show_home():

    todos = list(config.collection.find())

    return render_template(
        "index.html",
        todos=todos
    )


def add_todo():

    task = request.form["task"]

    config.collection.insert_one(
        {
            "task": task
        }
    )

    return show_home()


def delete_Todo(index):

    todos = list(config.collection.find())

    config.collection.delete_one(
        {
            "_id": todos[index]["_id"]
        }
    )

    return show_home()


def update_todo(index):

    task = request.form["task"]

    todos = list(config.collection.find())

    config.collection.update_one(
        {
            "_id": todos[index]["_id"]
        },
        {
            "$set": {
                "task": task
            }
        }
    )

    return show_home()


def edit_todo(index):

    todos = list(config.collection.find())

    return render_template(
        "edit.html",
        index=index,
        todo=todos[index]["task"]
    )