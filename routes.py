from controllers import registroUserControllers, LoginUserControllers, adopcionUserControllers, mascotaUserControllers


user = {
    "registro_user": "/api/v01/user/registro", "registro_user_controllers": registroUserControllers.as_view("registro_api"),
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "adopcion_user": "/api/v01/user/adopcion", "adopcion_user_controllers": adopcionUserControllers.as_view("adopcion_api"),
    "mascota_user": "/api/v01/user/mascota", "mascota_user_controllers": mascotaUserControllers.as_view("mascota_api"),
}

