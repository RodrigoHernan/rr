para instalar las aplicaciones: 


USUARIOS
INSTALLED_APPS = [
    'rr.usuarios',
    ..
]
# en urlsprincipal 
path('login/', include('rr.usuarios.urls',namespace="login")),
# si tenes un super user lo tenes que crear de nuevo

TAREAS 
INSTALLED_APPS = [
    'rr.tareas',
    ..
]









if __name__ == '__main__':
    print('no es un ejecutable')