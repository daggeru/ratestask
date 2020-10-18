import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


if __name__ == ' __main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
