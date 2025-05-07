import flet as ft
import random

class SettingsView(ft.Container):
    def __init__(self, page: ft.Page, purple_color: str, white_color: str, yellow_color: str, grey_color: str):
        super().__init__(expand=True)
        self.page = page
        self.purple_color = purple_color
        self.white_color = white_color
        self.yellow_color = yellow_color
        self.grey_color = grey_color

        # Widget de configuración
        self.notifications_switch = ft.Switch(value=True, active_color=self.yellow_color)
        self.theme_dropdown = ft.Dropdown(
            label="Tema",
            options=[
                ft.dropdown.Option("Claro"),
                ft.dropdown.Option("Oscuro"),
                ft.dropdown.Option("Sistema"),
            ],
            value="Oscuro",
            width=200,
            border_color=self.purple_color
        )
        self.font_size_slider = ft.Slider(
            min=12,
            max=24,
            divisions=6,
            value=16,
            active_color=self.purple_color,
            inactive_color=self.grey_color,
            thumb_color=self.white_color,
        )
        self.content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=20,
            controls=[
                self._create_header(),
                self._create_setting_card(
                    icon=ft.Icon(ft.icons.NOTIFICATIONS, color=self.yellow_color),
                    title="Notificaciones",
                    subtitle="Activa/desactiva las notificaciones del sistema",
                    control=self.notifications_switch,
                ),
                self._create_setting_card(
                    icon=ft.Icon(ft.icons.COLOR_LENS, color=self.yellow_color),
                    title="Tema",
                    subtitle="Selecciona el tema de la aplicación",
                    control=self.theme_dropdown,
                ),
                self._create_setting_card(
                    icon=ft.Icon(ft.icons.TEXT_FIELDS, color=self.yellow_color),
                    title="Tamaño de fuente",
                    subtitle="Ajusta el tamaño de la fuente de la aplicación",
                    control=self.font_size_slider,
                ),
                self._create_advanced_settings(),
                self._create_save_button(),
            ]
        )
    
    def _create_header(self):
        return ft.Column(
            spacing=5,
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.SETTINGS, color=self.yellow_color, size=24),
                        ft.Text("Configuración", size=24, weight="bold", color=self.white_color),
                    ],
                    spacing=10
                ),
                ft.Text("Ajusta la configuración de la aplicación", size=14, color=ft.colors.with_opacity(0.4, self.white_color)),
                ft.Divider(height=10, color=ft.colors.with_opacity(0.2, self.white_color)),
            ]
        )
        
    def _create_setting_card(self, icon, title, subtitle, control):
        return ft.Card(
            elevation=5,
            color=ft.colors.with_opacity(0.1, self.white_color),
            content=ft.Container(
                padding=15,
                content=ft.Row(
                    controls=[
                        icon,
                        ft.Column(
                            expand=True,
                            spacing=5,
                            controls=[
                                ft.Text(title, size=16, weight="bold", color=self.white_color),
                                ft.Text(subtitle, size=12, color=self.white_color),
                            ]
                        ),
                        control
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            )
        )
        
    def _create_advanced_settings(self):
        return ft.Card(
            elevation=5,
            color=ft.colors.with_opacity(0.1, self.white_color),
            content=ft.Container(
                padding=15,
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.SETTINGS_APPLICATIONS, color=self.yellow_color),
                                ft.Text("Configuración avanzada", size=16, weight="bold", color=self.white_color),
                            ],
                            spacing=10
                        ),
                        ft.Divider(height=10, color=ft.colors.with_opacity(0.2, self.white_color)),
                        self._create_setting_card(
                            icon=ft.Icon(ft.icons.CLOUD, color=self.yellow_color),
                            title="Sincronización en la nube",
                            subtitle="Sincroniza tus datos con la nube",
                            control=ft.Switch(value=True, active_color=self.purple_color),
                        ),
                        self._create_setting_card(
                            icon=ft.Icon(ft.icons.SECURITY, color=self.yellow_color),
                            title="Autenticación biométrica",
                            subtitle="Habilita la autenticación biométrica",
                            control=ft.Switch(value=True, active_color=self.purple_color),
                        ),
                    ]
                )
            )
        )
        
    def _create_save_button(self):
        return ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.ElevatedButton(
                text="Guardar Cambios",
                bgcolor=self.purple_color,
                width=200,
                on_click=lambda e: self._save_settings(),
            ),
            alignment=ft.alignment.center,
        )
        
    def _save_settings(self):
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("Configuración guardada con éxito!", color=self.white_color),
            bgcolor=self.purple_color,
            action="OK",
        )
        self.page.snack_bar.open = True
        self.page.update()