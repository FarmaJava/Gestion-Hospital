import flet as ft

from components.sidebar import crear_sidebar


def vista_secretaria(volver):

    # =========================================
    # CAMPOS DEL FORMULARIO
    # =========================================

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

    # =========================================
    # TABLA DE CITAS
    # =========================================

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

    # =========================================
    # FUNCIÓN AGENDAR
    # =========================================

    def agendar_cita(e):

        # Validación básica
        if (
            campo_nombre.value == ""
            or campo_dni.value == ""
            or campo_medico.value is None
            or campo_fecha.value == ""
            or campo_hora.value == ""
        ):

            page = e.page

            page.snack_bar = ft.SnackBar(
                ft.Text("Complete todos los campos")
            )

            page.snack_bar.open = True
            page.update()

            return

        # Agregar fila a la tabla
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

        # Limpiar campos
        campo_nombre.value = ""
        campo_dni.value = ""
        campo_medico.value = None
        campo_fecha.value = ""
        campo_hora.value = ""

        # Actualizar interfaz
        e.page.update()

    # =========================================
    # VISTA PRINCIPAL
    # =========================================

    return ft.Row(
        expand=True,
        controls=[

            # =========================================
            # SIDEBAR
            # =========================================

            crear_sidebar(
                "Panel Secretaria",
                ft.Colors.GREEN_900,
                volver
            ),

            # =========================================
            # CONTENIDO
            # =========================================

            ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    controls=[

                        # TÍTULO
                        ft.Text(
                            "Gestión de Citas",
                            size=32,
                            weight=ft.FontWeight.BOLD
                        ),

                        # =========================================
                        # FORMULARIO
                        # =========================================

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

                        # =========================================
                        # TABLA
                        # =========================================

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