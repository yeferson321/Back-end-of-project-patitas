from controllers import registroUserControllers, LoginUserControllers


user = {
    "registro_user": "/api/v01/user/registro", "registro_user_controllers": registroUserControllers.as_view("registro_api"),
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api")
}

