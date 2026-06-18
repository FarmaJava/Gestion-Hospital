import flet as ft

from components.sidebar import crear_sidebar

from views.medico.pacientes import vista_pacientes
from views.medico.consultas import vista_consultas
from views.medico.historial import vista_historial


class VistaMedico(ft.Row):

    def __init__(self, volver):

        super().__init__(expand=True)

        self.contenido = ft.Container(
            expand=True,
            padding=20,
            content=vista_pacientes()  # Vista inicial
        )

        self.controls = [

            crear_sidebar(

                titulo="Panel Médico",

                color=ft.Colors.BLUE_GREY_900,

                volver=volver,

                opciones=[

                    (
                        "Pacientes",
                        ft.Icons.PERSON,
                        self.mostrar_pacientes
                    ),

                    (
                        "Consultas",
                        ft.Icons.MEDICAL_SERVICES,
                        self.mostrar_consultas
                    ),

                    (
                        "Historial",
                        ft.Icons.FOLDER,
                        self.mostrar_historial
                    ),

                ]

            ),

            self.contenido
        ]

    def mostrar_pacientes(self):
        self.contenido.content = vista_pacientes()
        self.update()

    def mostrar_consultas(self):
        self.contenido.content = vista_consultas()
        self.update()

    def mostrar_historial(self):
        self.contenido.content = vista_historial()
        self.update()


def vista_medico(volver):
    return VistaMedico(volver)