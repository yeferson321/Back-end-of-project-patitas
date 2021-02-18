
from flask.views import MethodView
from flask import jsonify, request
import time



class registroUserControllers(MethodView):
    """
        registro
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(1)
        content = request.get_json()
        name = content.get("name")
        lastname=content.get("lastname")
        phone= content.get("phone")
        addres=content.get("addres")
        email = content.get("email")
        password = content.get("password")

        return jsonify({"registro ok": True, "name": name,  "lastname": lastname, "phone":phone, "addres":addres, "email": email}), 200
        

class LoginUserControllers(MethodView):
    """
        login 
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(1)
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")

        return jsonify({"registro ok": True, "email": email}), 200