from models.usuario import Usuario

u = Usuario()

u.usuario = "admin"
u.contraseña = "1234"
u.rol = "secretaria"

if u.registrar():
    print("Usuario guardado correctamente")
else:
    print("Error al guardar usuario")