from controllers import LoginUserControllers


user = {
    "registro_user": "/api/v01/user/registro", "registro_user_controllers": LoginUserControllers.as_view("registro_api"),
}

