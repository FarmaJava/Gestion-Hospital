import flet as ft


def vista_pacientes():

    campo_busqueda = ft.TextField(
        label="Buscar paciente por DNI",
        prefix_icon=ft.Icons.SEARCH,
        width=400
    )

    datos_paciente = ft.Container(
        width=450,
        padding=20,
        border_radius=15,
        bgcolor=ft.Colors.BLUE_GREY_800,
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Text(
                    "Datos del Paciente",
                    size=22,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text("Nombre: ---"),
                ft.Text("DNI: ---"),
                ft.Text("Grupo sanguíneo: ---"),
                ft.Text("Antecedentes: ---"),
            ]
        )
    )

    return ft.Column(
        controls=[
            ft.Text(
                "Pacientes",
                size=32,
                weight=ft.FontWeight.BOLD
            ),

            campo_busqueda,

            ft.Container(
                margin=ft.margin.only(top=20),
                content=datos_paciente
            )
        ]
    )