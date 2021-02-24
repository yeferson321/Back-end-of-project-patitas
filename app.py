from flask import Flask
from routes import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule(user["registro_user"], view_func=user["registro_user_controllers"])
app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
app.add_url_rule(user["adopcion_user"], view_func=user["adopcion_user_controllers"])
app.add_url_rule(user["mascota_user"], view_func=user["mascota_user_controllers"])

