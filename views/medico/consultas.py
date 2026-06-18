import flet as ft


def vista_consultas():

    campo_paciente = ft.Dropdown(
        label="Paciente",
        width=450,
        hint_text="Seleccione un paciente",
        options=[
            ft.dropdown.Option("Juan Pérez - DNI 42123456"),
            ft.dropdown.Option("María Gómez - DNI 39876543"),
            ft.dropdown.Option("Carlos López - DNI 45123789"),
        ]
    )

    datos_paciente = ft.Container(
        padding=15,
        border_radius=10,
        bgcolor=ft.Colors.BLUE_GREY_700,
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Text(
                    "Datos del Paciente",
                    weight=ft.FontWeight.BOLD,
                    size=18
                ),
                ft.Text("Nombre: ---"),
                ft.Text("DNI: ---"),
                ft.Text("Grupo sanguíneo: ---"),
                ft.Text("Antecedentes: ---"),
            ]
        )
    )

    campo_sintomas = ft.TextField(
        label="Síntomas",
        multiline=True,
        min_lines=2,
        max_lines=4,
    )

    campo_diagnostico = ft.TextField(
        label="Diagnóstico"
    )

    campo_tratamiento = ft.TextField(
        label="Tratamiento",
        multiline=True,
        min_lines=2,
        max_lines=4,
    )

    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=20,
        controls=[

            ft.Text(
                "Nueva Consulta",
                size=32,
                weight=ft.FontWeight.BOLD
            ),

            campo_paciente,

            datos_paciente,

            ft.Container(
                padding=20,
                border_radius=15,
                bgcolor=ft.Colors.BLUE_GREY_800,
                content=ft.Column(
                    spacing=15,
                    controls=[
                        campo_sintomas,
                        campo_diagnostico,
                        campo_tratamiento,

                        ft.ElevatedButton(
                            "Guardar Consulta",
                            icon=ft.Icons.SAVE
                        )
                    ]
                )
            )
        ]
    )