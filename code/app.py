# Package imports
from flask import Flask
from flask_restful import Api

# App initialization
app = Flask(__name__)
api = Api(app)

# Run the app
app.run(port=5000, debug=True)
