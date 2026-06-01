import flet as ft


def crear_sidebar(titulo, color, volver):

    return ft.Container(
        width=250,
        bgcolor=color,
        padding=20,
        content=ft.Column(
            controls=[

                ft.Text(
                    titulo,
                    size=25,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Divider(),

                ft.TextButton(
                    "Inicio",
                    icon=ft.Icons.HOME,
                    on_click=lambda e: volver()
                ),

                ft.TextButton(
                    "Pacientes",
                    icon=ft.Icons.PERSON
                ),

                ft.TextButton(
                    "Citas",
                    icon=ft.Icons.CALENDAR_MONTH
                ),

                ft.TextButton(
                    "Historial",
                    icon=ft.Icons.FOLDER
                )
            ]
        )
    )