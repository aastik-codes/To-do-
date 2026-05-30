from flask import Flask
from config import *

app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    startmongo()
    app.run(debug=True)