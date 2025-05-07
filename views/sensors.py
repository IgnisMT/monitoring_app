import flet as ft
from components.graph import create_graph_sensors
import random

class SensorsView(ft.Container):
    def __init__(self, page: ft.Page, purple_color: str, white_color: str, yellow_color: str, grey_color: str):
        super().__init__(expand=True)
        self.page = page
        self.purple_color = purple_color
        self.white_color = white_color
        self.yellow_color = yellow_color
        self.grey_color = grey_color

        data = ["Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4", "Sensor 5", "Sensor 6"]
        self.chart = create_graph_sensors(self.purple_color, self.white_color, self.yellow_color, self.grey_color, data)
        
        # Datos de ejemplo para sensores
        self.sensors = [
            {"name": "Temperatura", "value": 24.5, "unit": "℃", "icon": ft.icons.THERMOSTAT, "color": "#FF5252", "status": "Normal"},
            {"name": "Nivel de pH", "value": 7.2, "unit": "pH", "icon": ft.icons.WATER_DROP, "color": "#4285F4", "status": "Óptimo"},
            {"name": "Humedad", "value": 65, "unit": "%", "icon": ft.icons.WATER_DROP, "color": "#4285F4", "status": "Normal"},
            {"name": "Oxígeno", "value": 8.5, "unit": "mg/L", "icon": ft.icons.AIR, "color": "#4CAF50", "status": "Alto"},
        ]
        
        self.content = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=20,
            controls=[
                self._create_header(),
                ft.Row(
                    wrap=True,
                    spacing=20,
                    controls=[self._create_sensor_card(sensor) for sensor in self.sensors],
                ),
                ft.Container(
                    padding=20,
                    content=self.chart,
                    border_radius=15,
                    bgcolor=ft.colors.with_opacity(0.05, self.white_color)
                ),
                self._create_quick_actions(),
            ]
        )
        
    def _create_header(self):
        return ft.Container(
            padding=ft.padding.only(bottom=20),
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.icons.SENSORS, color=self.yellow_color),
                            ft.Text("Monitor de Sensores", size=24, weight="bold", color=self.white_color),
                        ],
                        spacing=10
                    ),
                    ft.Text("Datos en tiempo real de los sensores conectados",
                            size=14, color=ft.colors.with_opacity(0.4, self.white_color)),
                    ft.Divider(height=10, color=self.grey_color),
                ]
            )
        )
        
    def _create_sensor_card(self, sensor):
        return ft.Container(
            width=250,
            height=200,
            padding=15,
            border_radius=15,
            bgcolor=ft.colors.with_opacity(0.1, self.grey_color),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    ft.Icon(sensor["icon"], size=30, color=sensor["color"]),
                    ft.Text(sensor["name"], size=16, weight="bold", color=self.white_color),
                    ft.Text(
                        f"{sensor['value']} {sensor['unit']}",
                        size=24,
                        weight="bold",
                        color=self.white_color,
                    ),
                    ft.Text(
                        f"Estado: {sensor['status']}",
                        size=12,
                        color=ft.colors.with_opacity(0.7, self.white_color),
                    ),
                    ft.Container(
                        height=5,
                        border_radius=5,
                        bgcolor=ft.colors.with_opacity(0.2, self.white_color),
                        padding=0,
                        content=ft.Container(
                            width=random.randint(30, 200),
                            height=5,
                            border_radius=5,
                            bgcolor=sensor["color"],
                        )
                    )
                ]
            ),
        )
    
    def _create_quick_actions(self):
        return ft.Container(
            padding=20,
            border_radius=15,
            bgcolor=ft.colors.with_opacity(0.05, self.white_color),
            content=ft.Column(
                spacing=15,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.icons.SPEED, color=self.yellow_color),
                            ft.Text("Acciones Rápidas", size=18, weight="bold", color=self.white_color),
                        ],
                        spacing=10
                    ),
                    ft.Divider(height=1, color=ft.colors.with_opacity(0.2, self.white_color)),
                    ft.Row(
                        spacing=10,
                        controls=[
                            ft.ElevatedButton(
                                text="Calibrar Sensores",
                                icon=ft.icons.TUNE,
                                bgcolor=self.purple_color,
                            ),
                            ft.ElevatedButton(
                                text="Exportar Datos",
                                icon=ft.icons.DOWNLOAD,
                                bgcolor=ft.colors.with_opacity(0.2, self.grey_color),
                            ),
                            ft.ElevatedButton(
                                text="Configurar Alertas",
                                icon=ft.icons.NOTIFICATIONS,
                                bgcolor=ft.colors.with_opacity(0.2, self.grey_color),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ]
            )
        )
