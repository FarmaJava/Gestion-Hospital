import flet as ft


def vista_historial():

    tabla = ft.DataTable(

        columns=[

            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Diagnóstico")),
            ft.DataColumn(ft.Text("Observaciones")),
        ],

        rows=[]
    )

    return ft.Column(

        controls=[

            ft.Text(
                "Historial Médico",
                size=32,
                weight=ft.FontWeight.BOLD
            ),

            ft.Container(

                padding=20,

                border_radius=15,

                bgcolor=ft.Colors.BLUE_GREY_800,

                content=tabla
            )
        ]
    )