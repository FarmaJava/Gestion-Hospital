import flet as ft


def crear_sidebar(titulo, color, volver, opciones):

    controles = [

        ft.Text(
            titulo,
            size=25,
            weight=ft.FontWeight.BOLD
        ),

        ft.Divider()

    ]

    for texto, icono, accion in opciones:

        controles.append(

            ft.TextButton(
                texto,
                icon=icono,
                on_click=lambda e, accion=accion: accion()
            )

        )

    controles.append(ft.Container(expand=True))

    controles.append(ft.Divider())

    controles.append(

        ft.TextButton(
            "Cerrar sesión",
            icon=ft.Icons.LOGOUT,
            on_click=lambda e: volver()
        )

    )

    return ft.Container(

        width=250,

        bgcolor=color,

        padding=20,

        content=ft.Column(
            expand=True,
            controls=controles
        )

    )