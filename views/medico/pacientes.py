import flet as ft

from database.models.paciente import Paciente


def vista_pacientes():

    paciente_model = Paciente()

    txt_nombre = ft.Text("Nombre: ---")
    txt_dni = ft.Text("DNI: ---")
    txt_sangre = ft.Text("Grupo sanguíneo: ---")
    txt_antecedentes = ft.Text("Antecedentes: ---")
    txt_telefono = ft.Text("Teléfono: ---")
    txt_direccion = ft.Text("Dirección: ---")

    campo_busqueda = ft.TextField(
        label="Buscar por DNI",
        prefix_icon=ft.Icons.SEARCH,
        width=350
    )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("DNI")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Apellido")),
        ],
        rows=[]
    )

    datos_paciente = ft.Container(
        margin=ft.margin.only(top=20),
        padding=20,
        border_radius=15,
        bgcolor=ft.Colors.BLUE_GREY_800,
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Text(
                    "Paciente Seleccionado",
                    size=22,
                    weight=ft.FontWeight.BOLD
                ),
                txt_nombre,
                txt_dni,
                txt_sangre,
                txt_antecedentes,
                txt_telefono,
                txt_direccion,
            ]
        )
    )

    def seleccionar_paciente(paciente):

        txt_dni.value = f"DNI: {paciente[1]}"
        txt_nombre.value = f"Nombre: {paciente[2]} {paciente[3]}"
        txt_telefono.value = f"Teléfono: {paciente[5]}"
        txt_direccion.value = f"Dirección: {paciente[6]}"
        txt_sangre.value = f"Grupo sanguíneo: {paciente[7]}"
        txt_antecedentes.value = f"Antecedentes: {paciente[8]}"

        if datos_paciente.page:
            datos_paciente.update()

    def cargar_tabla(lista):

        tabla.rows.clear()

        for paciente in lista:

            tabla.rows.append(

                ft.DataRow(

                    cells=[
                        ft.DataCell(ft.Text(str(paciente[1]))),
                        ft.DataCell(ft.Text(str(paciente[2]))),
                        ft.DataCell(ft.Text(str(paciente[3]))),
                    ],

                    on_select_change=lambda e, p=paciente: seleccionar_paciente(p)

                )

            )

        if tabla.page:
            tabla.update()

    def buscar(e):

        dni = campo_busqueda.value.strip()

        if dni == "":
            cargar_tabla(paciente_model.listar_todos())
            return

        resultados = [

            p for p in paciente_model.listar_todos()
            if str(p[1]).startswith(dni)

        ]
        cargar_tabla(resultados)

    campo_busqueda.on_change = buscar

    pacientes = paciente_model.listar_todos()

    for paciente in pacientes:

        tabla.rows.append(

            ft.DataRow(

                cells=[
                    ft.DataCell(ft.Text(str(paciente[1]))),
                    ft.DataCell(ft.Text(str(paciente[2]))),
                    ft.DataCell(ft.Text(str(paciente[3]))),
                ],

                on_select_change=lambda e, p=paciente: seleccionar_paciente(p)

            )

        )

    return ft.Column(

        scroll=ft.ScrollMode.AUTO,

        controls=[

            ft.Text(
                "Pacientes",
                size=32,
                weight=ft.FontWeight.BOLD
            ),

            campo_busqueda,

            ft.Container(
                margin=ft.margin.only(top=15),
                padding=20,
                border_radius=15,
                bgcolor=ft.Colors.BLUE_GREY_800,
                content=tabla
            ),

            datos_paciente

        ]

    )