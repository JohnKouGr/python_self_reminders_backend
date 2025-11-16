from flask import Flask
from enviroment.run_config import FLASK_DEBUG, FLASK_HOST, FLASK_PORT

# Blueprint imports
from endpoints.ep_users import app as ap1

app = Flask(__name__)

# Blueprints
app.register_blueprint(ap1)

__flaskHost = FLASK_HOST
__flaskPort = FLASK_PORT
__flaskDebug = FLASK_DEBUG 

#if __name__ == '__main__':
app.run(host=__flaskHost, port=__flaskPort, debug=__flaskDebug) # type: ignore







