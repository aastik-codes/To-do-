from flask import Flask
from config import *
from config import HOST, PORT


app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    startmongo()
    app.run(host=HOST, port=PORT, debug=True)