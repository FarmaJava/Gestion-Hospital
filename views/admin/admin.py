import flet as ft

from components.sidebar import crear_sidebar


def vista_admin(
        volver,
        usuarios,
        crear_usuario,
        eliminar_usuario,
        editar_usuario
):

    campo_nombre = ft.TextField(label="Nombre completo")

    campo_usuario = ft.TextField(label="Usuario")

    campo_email = ft.TextField(label="Email")

    campo_password = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True
    )

    campo_rol = ft.Dropdown(
        label="Rol",
        width=220,
        options=[
            ft.dropdown.Option("Administrador"),
            ft.dropdown.Option("Medico"),
            ft.dropdown.Option("Secretaria")
        ]
    )

    tabla = ft.DataTable(
        expand=True,
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Usuario")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Rol")),
            ft.DataColumn(ft.Text("Acciones"))
        ],
        rows=[]
    )

    for usuario in usuarios:

        tabla.rows.append(

            ft.DataRow(
                cells=[

                    ft.DataCell(ft.Text(usuario[1])),
                    ft.DataCell(ft.Text(usuario[2])),
                    ft.DataCell(ft.Text(usuario[3])),
                    ft.DataCell(ft.Text(usuario[5])),

                    ft.DataCell(

                        ft.Row(

                            controls=[

                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    tooltip="Editar",
                                    on_click=lambda e, id=usuario[0]: editar_usuario(id)
                                ),

                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color="red",
                                    tooltip="Eliminar",
                                    on_click=lambda e, id=usuario[0]: eliminar_usuario(id)
                                )
                            ]
                        )
                    )
                ]
            )
        )

    return ft.Row(

        expand=True,

        controls=[

        crear_sidebar(
            titulo="Administrador",
            color=ft.Colors.BLUE_GREY_900,
            volver=volver,
            opciones=[
                 ("Usuarios", ft.Icons.GROUP),
                 ("Empleados", ft.Icons.BADGE),
                 ("Reportes", ft.Icons.ANALYTICS),
            ]
        ),

            ft.Container(

                expand=True,

                padding=20,

                content=ft.Column(

                    scroll=ft.ScrollMode.AUTO,

                    controls=[

                        ft.Text(
                            "Administración de Usuarios",
                            size=32,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Container(

                            bgcolor=ft.Colors.BLUE_GREY_800,

                            padding=20,

                            border_radius=15,

                            content=ft.Column(

                                controls=[

                                    ft.Text(
                                        "Crear nuevo empleado",
                                        size=22,
                                        weight=ft.FontWeight.BOLD
                                    ),

                                    campo_nombre,
                                    campo_usuario,
                                    campo_email,
                                    campo_password,
                                    campo_rol,

                                    ft.ElevatedButton(

                                        "Crear Usuario",

                                        icon=ft.Icons.PERSON_ADD,

                                        on_click=lambda e: crear_usuario(
                                            campo_nombre.value,
                                            campo_usuario.value,
                                            campo_email.value,
                                            campo_password.value,
                                            campo_rol.value
                                        )
                                    )
                                ]
                            )
                        ),

                        ft.Container(

                            margin=ft.margin.only(top=20),

                            bgcolor=ft.Colors.BLUE_GREY_800,

                            padding=20,

                            border_radius=15,

                            content=ft.Column(

                                controls=[

                                    ft.Text(
                                        "Usuarios registrados",
                                        size=22,
                                        weight=ft.FontWeight.BOLD
                                    ),

                                    tabla
                                ]
                            )
                        )
                    ]
                )
            )
        ]
    )