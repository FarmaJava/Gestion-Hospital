import flet as ft

from components.sidebar import crear_sidebar



def vista_medico(volver):

    campo_busqueda = ft.TextField(
        label="Buscar paciente por DNI",
        prefix_icon=ft.Icons.SEARCH,
        width=400
    )

    campo_sintomas = ft.TextField(
        label="Síntomas",
        multiline=True,
        min_lines=2,
        max_lines=4
    )

    campo_diagnostico = ft.TextField(
        label="Diagnóstico"
    )

    campo_tratamiento = ft.TextField(
        label="Tratamiento",
        multiline=True,
        min_lines=2,
        max_lines=4
    )

    tabla_historial = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Diagnóstico")),
            ft.DataColumn(ft.Text("Observaciones")),
        ],
        rows=[]
    )

    datos_paciente = ft.Container(
        width=400,
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
                ft.Text("Antecedentes: ---")
            ]
        )
    )

    formulario_consulta = ft.Container(
        expand=True,
        padding=20,
        border_radius=15,
        bgcolor=ft.Colors.BLUE_GREY_800,
        content=ft.Column(
            spacing=15,
            controls=[

                ft.Text(
                    "Nueva Consulta",
                    size=22,
                    weight=ft.FontWeight.BOLD
                ),

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

    return ft.Row(
        expand=True,
        controls=[

            crear_sidebar(
               titulo="Panel Médico",
               color=ft.Colors.BLUE_GREY_900,
               volver=volver,
               opciones=[
                  ("Pacientes", ft.Icons.PERSON),
                  ("Consultas", ft.Icons.MEDICAL_SERVICES),
                  ("Historial", ft.Icons.FOLDER),
               ]
            ),

            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    controls=[

                        ft.Text(
                            "Consulta Médica",
                            size=32,
                            weight=ft.FontWeight.BOLD
                        ),

                        campo_busqueda,

                        ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                datos_paciente,
                                formulario_consulta
                            ]
                        ),

                        ft.Container(
                            margin=ft.margin.only(top=20),
                            padding=20,
                            border_radius=15,
                            bgcolor=ft.Colors.BLUE_GREY_800,
                            content=ft.Column(
                                controls=[

                                    ft.Text(
                                        "Historial Médico",
                                        size=22,
                                        weight=ft.FontWeight.BOLD
                                    ),

                                    tabla_historial
                                ]
                            )
                        )
                    ]
                )
            )
        ]
    )