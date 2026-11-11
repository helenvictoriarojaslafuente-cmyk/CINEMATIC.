#1_Login

import json
ARCHIVO_JSON = "usuarios_datos.json"

lista_usuarios = []

def cargar_usuarios_json():
    global lista_usuarios
    archivo = open(ARCHIVO_JSON, "r", encoding="utf-8")
    lista_usuarios = json.load(archivo)
    archivo.close()

def guardar_usuarios_json():
    archivo = open(ARCHIVO_JSON, "w", encoding="utf-8")
    json.dump(lista_usuarios, archivo, indent=4, ensure_ascii=False)
    archivo.close()

def registrar_usuario():
    global lista_usuarios
    print("")
    print("    CINEMATIC - CREAR CUENTA    ")
    print("")

    while True:
        usuario = input("Ingrese su nombre de usuario: ").strip()

        usuario_repetido = False
        for perfil in lista_usuarios:
            if perfil["usuario"].lower() == usuario.lower():
                usuario_repetido = True
                break

        if usuario_repetido == True:
            print("Este usuario ya existe. Intente con otro.")
            print("")

        elif not usuario.isalpha():
            print("El usuario solo puede contener letras. Intente nuevamente.")
            print("")

        else: 
            contraseña = input("Ingrese su contraseña: ").strip()
            
            if not contraseña:
                print("La contraseña no puede estar vacía.")
                print("")
            else: 
                nuevo_perfil = {
                    "usuario": usuario,
                    "contraseña": contraseña,
                    "rol": "cliente"
                }
                lista_usuarios.append(nuevo_perfil)
                guardar_usuarios_json()

                print("Cuenta creada con éxito.")
                print("")

                break

def iniciar_sesion():
    print("")
    print("   CINEMATIC - INICIAR SESIÓN    ")
    print("")

    while True:
        usuario_login = input("Introduce tu Usuario: ").strip()
        if usuario_login.isalpha():
            break
        else:
            print("El usuario solo puede contener letras. Intente de nuevo.")
            print("")

    while True:
        contraseña_login = input("Introduce tu Contraseña: ").strip()
        if contraseña_login.isdigit():
            break
        else:
            print("La contraseña solo puede contener números. Intente de nuevo.")
            print("")

    for perfil in lista_usuarios:
        if perfil["usuario"].lower() == usuario_login.lower() and perfil["contraseña"] == contraseña_login:
            print("Acceso concedido. Cargando interfaz....")
            print()
            return perfil

    print("El usuario o la contraseña son incorrectos. Intenta nuevamente.")
    return False

cargar_usuarios_json()