import flet as ft


def vista_login(iniciar_sesion):

    campo_usuario = ft.TextField(
        label="Email",
        prefix_icon=ft.Icons.PERSON
    )

    campo_password = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK
    )

    formulario = ft.Container(
        width=450,
        padding=40,
        border_radius=20,
        bgcolor=ft.Colors.BLUE_GREY_800,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[

                ft.Icon(
                    ft.Icons.ACCOUNT_CIRCLE,
                    size=90
                ),

                ft.Text(
                    "Iniciar Sesión",
                    size=30,
                    weight=ft.FontWeight.BOLD
                ),

                campo_usuario,
                campo_password,

                ft.ElevatedButton(
                    "Ingresar",
                    icon=ft.Icons.LOGIN,
                    width=250,
                    on_click=lambda e: iniciar_sesion(
                        campo_usuario.value,
                        campo_password.value
                    )
                ),

            ]
        )
    )

    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.BLUE_GREY_900,
        content=formulario
    )