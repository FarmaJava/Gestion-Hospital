import flet as ft
from database.models.sidebar import crear_sidebar

def vista_secretaria(volver):
    campo_nombre = ft.TextField(
        label="Paciente",
        width=250
    )
    
    campo_dni = ft.TextField(
        label="DNI",
        width=180
    )
    
    campo_medico = ft.Dropdown(
        label="Médico",
        width=220,
        options=[
            ft.dropdown.Option("Dr. Gómez"),
            ft.dropdown.Option("Dra. Martínez"),
            ft.dropdown.Option("Dr. López"),
        ]
    )

    campo_fecha = ft.TextField(
        label="Fecha",
        hint_text="DD/MM/AAAA",
        width=150
    )

    campo_hora = ft.TextField(
        label="Hora",
        hint_text="HH:MM",
        width=120
    )

#citas
    tabla_citas = ft.DataTable(
        expand=True,
        columns=[
            ft.DataColumn(ft.Text("Paciente")),
            ft.DataColumn(ft.Text("DNI")),
            ft.DataColumn(ft.Text("Médico")),
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Hora")),
        ],
        rows=[]
    )

    def agendar_cita(e):
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(campo_nombre.value)),
                ft.DataCell(ft.Text(campo_dni.value)),
                ft.DataCell(ft.Text(campo_medico.value)),
                ft.DataCell(ft.Text(campo_fecha.value)),
                ft.DataCell(ft.Text(campo_hora.value)),
            ]
        )

        tabla_citas.rows.append(nueva_fila)
        campo_nombre.value = ""    #limpia campos
        campo_dni.value = ""
        campo_medico.value = None
        campo_fecha.value = ""
        campo_hora.value = ""

        e.page.update()

    return ft.Row(
        expand=True,
        controls=[
            crear_sidebar(
                 titulo="Panel Secretaria",
                 color=ft.Colors.GREEN_900,
                 volver=volver,
                 opciones=[
                     ("Pacientes", ft.Icons.PERSON),
                     ("Citas", ft.Icons.CALENDAR_MONTH),
                     ("Agenda", ft.Icons.EVENT),
                 ]
            ),

            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    controls=[

                        ft.Text(
                            "Gestión de Citas",
                            size=32,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Container(
                            padding=20,
                            border_radius=15,
                            bgcolor=ft.Colors.BLUE_GREY_800,
                            content=ft.Column(
                                spacing=20,
                                controls=[

                                    ft.Text(
                                        "Nueva Cita",
                                        size=22,
                                        weight=ft.FontWeight.BOLD
                                    ),

                                    ft.Row(
                                        wrap=True,
                                        spacing=15,
                                        run_spacing=15,
                                        controls=[

                                            campo_nombre,
                                            campo_dni,
                                            campo_medico,
                                            campo_fecha,
                                            campo_hora,

                                        ]
                                    ),

                                    ft.ElevatedButton(
                                        "Agendar Cita",
                                        icon=ft.Icons.ADD,
                                        on_click=agendar_cita
                                    )

                                ]
                            )
                        ),

                        ft.Container(
                            margin=ft.margin.only(top=20),
                            padding=20,
                            border_radius=15,
                            bgcolor=ft.Colors.BLUE_GREY_800,
                            content=ft.Column(
                                controls=[

                                    ft.Text(
                                        "Citas Programadas",
                                        size=22,
                                        weight=ft.FontWeight.BOLD
                                    ),

                                    ft.Divider(),

                                    tabla_citas

                                ]
                            )
                        )

                    ]
                )
            )
        ]
    )