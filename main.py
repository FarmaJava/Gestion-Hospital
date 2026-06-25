import flet as ft
from database.models.usuario import Usuario
from views.medico.dashboard import vista_medico
from views.secretaria import vista_secretaria
from views.admin import vista_admin
from views.login import vista_login

class HospitalApp:

    def __init__(self, page: ft.Page):
        self.page = page
        self.configurar_pagina()
        self.ir_login()

    def configurar_pagina(self):
        self.page.title = "Sistema Hospitalario"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.window_width = 1400
        self.page.window_height = 850
        self.page.padding = 0

    def cambiar_vista(self, vista):
        self.page.clean()
        self.page.add(vista)
        self.page.update()

    def ir_login(self):
        self.cambiar_vista(
            vista_login(
                iniciar_sesion=self.iniciar_sesion
            )
        )

    def iniciar_sesion(self, usuario, password):
        user = Usuario()
        datos = user.login(usuario, password)

        if datos:
            rol = datos[5] #rol corresponde a la quinta columna de usuario
            if rol == "Administrador":
               self.ir_admin()

            elif rol == "Medico":
               self.ir_medico()

            elif rol == "Secretaria":
               self.ir_secretaria()
      
        else:
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Usuario o contraseña incorrectos")
            )
            self.page.snack_bar.open = True
            self.page.update()

    #vistas
    def ir_medico(self):
        self.cambiar_vista(
            vista_medico(
                volver=self.ir_login
            )
        )

    def ir_secretaria(self):
        self.cambiar_vista(
            vista_secretaria(
                volver=self.ir_login
            )
        )
    def ir_admin(self):
        user = Usuario()
        self.cambiar_vista(
 
        vista_admin(
            volver=self.ir_login,
            usuarios=user.listar_todos(),
            crear_usuario=self.crear_usuario_admin,
            eliminar_usuario=self.eliminar_usuario,
            editar_usuario=self.editar_usuario
        )
    )
        
    def crear_usuario_admin(self, nombre, usuario, email, password, rol):
        nuevo = Usuario()
        nuevo.nombre = nombre
        nuevo.usuario = usuario
        nuevo.email = email
        nuevo.contraseña = password
        nuevo.rol = rol

        if nuevo.registrar():
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Usuario creado correctamente.")
            )

        self.page.snack_bar.open = True
        self.page.update()
        self.ir_admin() 
        
    def eliminar_usuario(self, id_usuario):
        user = Usuario()
        user.eliminar(id_usuario)
        self.ir_admin()  
        
    def editar_usuario(self, id_usuario):
        print(id_usuario)     
        
def main(page: ft.Page):
    HospitalApp(page)


ft.run(main)