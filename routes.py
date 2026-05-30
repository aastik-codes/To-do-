from app import app
from controllers import *

@app.route("/")
def home():
    return show_home()

@app.route("/test")
def test():
    return "works"

@app.route("/add", methods=["POST"])
def add():
    return add_todo()

@app.route("/delete/<int:index>")
def delete(index):
    return delete_Todo(index)

@app.route("/update/<int:index>", methods=["POST"])
def update(index):
    return update_todo(index)

@app.route("/edit/<int:index>")
def edit(index):
    return edit_todo(index)

print("ROUTES FILES EXECUTED")