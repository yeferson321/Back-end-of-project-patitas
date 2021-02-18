
from flask.views import MethodView
from flask import jsonify, request
import time



class LoginUserControllers(MethodView):
    """
        registro
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(1)
        content = request.get_json()
        name = content.get("name")
        email = content.get("email")
        password = content.get("password")

        return jsonify({"registro ok": True, "name": name, "email": email, "password": password}), 200
        
