
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
        email = content.get("email")
        password = content.get("password")

        return jsonify({"registro ok": True, "name": name,  "lastname": lastname, "phone":phone, "email": email}), 200
        

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

class adopcionUserControllers(MethodView):
    """
         adopcion
     """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(2)
        content = request.get_json()
        namepet = content.get("namepet")
        raze=content.get("raze")
        ide= content.get("ide")
        age=content.get("age")
        email = content.get("email")
        

        return jsonify({"registro ok": True, "namepet": namepet,  "raze": raze, "ide":ide, "age":age, "email": email}), 200

class mascotaUserControllers(MethodView):
    """
         mascota
     """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(2)
        content = request.get_json()
        nameMas = content.get("nameMas")
        idMas=content.get("idMas")
        raz=content.get("raz")
        ageM=content.get("ageM")
       
        

        return jsonify({"registro ok": True, "nameMas": nameMas,  "idMas": idMas, "raz":raz, "ageM":ageM}), 200