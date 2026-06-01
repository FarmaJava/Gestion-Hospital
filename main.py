import flet as ft

from views.menu_principal import vista_menu_principal
from views.medico import vista_medico
from views.secretaria import vista_secretaria


class HospitalApp:

    def __init__(self, page: ft.Page):
        self.page = page

        self.configurar_pagina()
        self.ir_menu_principal()

    def configurar_pagina(self):
        self.page.title = "Sistema Hospitalario"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.window_width = 1400
        self.page.window_height = 850
        self.page.padding = 0

    # =========================
    # NAVEGACIÓN
    # =========================

    def cambiar_vista(self, vista):
        self.page.clean()
        self.page.add(vista)
        self.page.update()

    def ir_menu_principal(self):
        self.cambiar_vista(
            vista_menu_principal(
                ir_medico=self.ir_medico,
                ir_secretaria=self.ir_secretaria
            )
        )

    def ir_medico(self):
        self.cambiar_vista(
            vista_medico(
                volver=self.ir_menu_principal
            )
        )

    def ir_secretaria(self):
        self.cambiar_vista(
            vista_secretaria(
                volver=self.ir_menu_principal
            )
        )


def main(page: ft.Page):
    HospitalApp(page)


ft.run(main)