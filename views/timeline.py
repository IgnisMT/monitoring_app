import flet as ft
import random

class TimelineView(ft.Container):
    def __init__(self, page: ft.Page, purple_color: str, white_color: str, yellow_color: str, grey_color: str):
        super().__init__(expand=True)
        self.page = page
        self.purple_color = purple_color
        self.white_color = white_color
        self.yellow_color = yellow_color
        self.grey_color = grey_color
        
        self.actuators = [
            {"name": "Actuador 1", "value": 65, "status": "Funcionando ahora", "icon": ft.icons.MOTION_PHOTOS_AUTO, "active": True},
            {"name": "Actuador 2", "value": 35, "status": "Activo hace 11h 1min", "icon": ft.icons.ELECTRIC_BOLT, "active": False},
            {"name": "Actuador 3", "value": 90, "status": "Funcionando ahora", "icon": ft.icons.SETTINGS, "active": True},
            {"name": "Actuador 4", "value": 20, "status": "En espera", "icon": ft.icons.POWER_SETTINGS_NEW, "active": False},
        ]

        # Contenido de la vista de línea de tiempo
        self.content = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=20,
            controls=[
                self._create_header(),
                *[self._create_actuator_card(actuator) for actuator in self.actuators],
                self._create_actions_row(),
            ]
        )
        
    def _create_header(self):
        return ft.Column(
            spacing=5,
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.TIMELAPSE, color=self.yellow_color, size=24),
                        ft.Text("Línea de Tiempo de Actuadores", size=24, weight="bold", color=self.white_color),
                    ],
                    spacing=10
                ),
                ft.Text("Estado y actividad de los actuadores del sistema", size=14, color=self.white_color),
                ft.Divider(height=10, color=ft.colors.with_opacity(0.2, self.white_color))
            ]
        )   
        
    def _create_actuator_card(self, actuator):
        return ft.Card(
            elevation=5,
            color=ft.colors.with_opacity(0.1, self.white_color),
            content=ft.Container(
                padding=15,
                content=ft.Column(
                    spacing=10,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(actuator["icon"], color=self.yellow_color if actuator["active"] else self.grey_color),
                                ft.Text(actuator["name"], size=16, weight="bold", color=self.white_color),
                                ft.Container(
                                    content=ft.Text(
                                        "ACTIVO" if actuator["active"] else "INACTIVO",
                                        color=self.white_color,
                                        size=12,
                                        weight="bold",
                                    ),
                                    bgcolor=self.purple_color if actuator["active"] else ft.colors.with_opacity(0.5, self.grey_color),
                                    padding=ft.padding.symmetric(horizontal=10, vertical=5),
                                    border_radius=20,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Row(
                            controls=[
                                ft.Slider(
                                    min=0,
                                    max=100,
                                    value=actuator["value"],
                                    active_color=self.purple_color,
                                    inactive_color=ft.colors.with_opacity(0.1, self.white_color),
                                    label=f"{actuator['value']}%",
                                    expand=True
                                ),
                                ft.Container(
                                    width=80,
                                    content=ft.Text(f"{actuator['value']}%", 
                                                 size=18, 
                                                 weight="bold", 
                                                 color=self.white_color if actuator["active"] else self.grey_color),
                                )
                            ],                    
                        ),
                        ft.Text(actuator["status"], size=12, color=ft.colors.with_opacity(0.4, self.white_color)),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    text="Histórico",
                                    icon=ft.icons.HISTORY,
                                    bgcolor=ft.colors.with_opacity(0.2, self.purple_color),
                                ),
                                ft.ElevatedButton(
                                    text="Configuración",
                                    icon=ft.icons.SETTINGS,
                                    bgcolor=ft.colors.with_opacity(0.2, self.purple_color),
                                ),
                                ft.Switch(
                                    value=actuator["active"],
                                    active_color=self.purple_color,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    ],
                ),
            ),
        )
        
    def _create_actions_row(self):
        return ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Exportar Datos",
                    icon=ft.icons.DOWNLOAD,
                    bgcolor=ft.colors.with_opacity(0.2, self.grey_color),
                ),
                ft.ElevatedButton(
                    text="Programar Tareas",
                    icon=ft.icons.SCHEDULE,
                    bgcolor=ft.colors.with_opacity(0.2, self.grey_color),
                ),
                ft.ElevatedButton(
                    text="Ajustes Avanzados",
                    icon=ft.icons.TUNE,
                    bgcolor=ft.colors.with_opacity(0.2, self.grey_color),
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )