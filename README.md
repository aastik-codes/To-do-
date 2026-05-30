# Todo App

A simple beginner Todo application built using Flask and MongoDB. Supports all 4 CRUD operations:

1. Add Todos
2. Update Todos
3. Delete Todos
4. View Todos

---

# Tech Stack Used

1. Python
2. Flask
3. MongoDB
4. HTML
5. CSS

---

# Project Structure

```text
todo-app/
│
├── app.py          -> Contains app initialization and MongoDB connection setup
├── routes.py       -> Contains all routes and calls controller functions
├── controllers.py  -> Contains business logic functions used by routes
├── config.py       -> Contains MongoDB configuration
├── .env            -> Contains environment variables such as MONGO_URI
├── templates/      -> Contains HTML templates rendered by Flask
├── static/         -> Contains CSS files
└── README.md
```

---

# Environment Variables

Create a `.env` file and add:

```env
MONGO_URI=your_mongodb_connection_string
```

---

# How to Run

1. Create and activate a virtual environment.
2. Install required dependencies.
3. Start a virtual Environment
4. In terminal run " python app.py"

