import flet as ft


def tarjeta_menu(icono, titulo, color, accion):

    return ft.Container(
        width=250,
        height=220,
        bgcolor=color,
        border_radius=20,
        padding=20,
        animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[

                ft.Icon(icono, size=70),

                ft.Text(
                    titulo,
                    size=25,
                    weight=ft.FontWeight.BOLD
                ),

                ft.ElevatedButton(
                    "Ingresar",
                    width=150,
                    on_click=lambda e: accion()
                )
            ]
        )
    )



def vista_menu_principal(ir_medico, ir_secretaria):

    return ft.Container(
        expand=True,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[

                ft.Icon(
                    ft.Icons.LOCAL_HOSPITAL,
                    size=100,
                    color=ft.Colors.BLUE
                ),

                ft.Text(
                    "Sistema Hospitalario",
                    size=40,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    "Seleccione un módulo",
                    size=18,
                    color=ft.Colors.GREY_400
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40,
                    controls=[

                        tarjeta_menu(
                            ft.Icons.MEDICAL_SERVICES,
                            "Médico",
                            ft.Colors.BLUE_900,
                            ir_medico
                        ),

                        tarjeta_menu(
                            ft.Icons.EVENT_NOTE,
                            "Secretaria",
                            ft.Colors.GREEN_900,
                            ir_secretaria
                        )
                    ]
                )
            ]
        )
    )