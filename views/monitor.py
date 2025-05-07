import flet as ft
import random
from components.graph import create_graph

class MonitorView(ft.Container):
    def __init__(self, page: ft.Page, purple_color: str, white_color: str, yellow_color: str, grey_color: str):
        super().__init__(expand=True)
        self.page = page
        self.purple_color = purple_color
        self.white_color = white_color
        self.yellow_color = yellow_color
        self.grey_color = grey_color

        # Datos de ejemplo para sensores
        self.sensors = {
            "Temperatura": {"value": 24.5, "unit": "C", "icon": ft.icons.THERMOSTAT, "color": "#FF5252"},
            "Humedad": {"value": 65, "unit": "%", "icon": ft.icons.WATER_DROP, "color": "#4285F4"},
            "Presión": {"value": 1013, "unit": "hPa", "icon": ft.icons.SPEED, "color": "#9C27B0"},
            "Calidad Aire": {"value": 85, "unit": "AQI", "icon": ft.icons.AIR, "color": "#4CAF50"},
        }
        
        data = ["1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "10h", "11h", "12h"]
        self.chart = create_graph(self.purple_color, self.white_color, self.yellow_color, self.grey_color, data)
        
        self.content = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                self._create_header(),
                self._create_sensor_cards(),
                ft.Container(
                    padding=20,
                    content=self.chart,
                    margin=ft.margin.only(top=20),
                    border_radius=15,
                    bgcolor=ft.colors.with_opacity(0.05, self.white_color)
                ),
                self._create_alert_panel()
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
                            ft.Icon(ft.icons.MONITOR_HEART, color=self.yellow_color),
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
        
    def _create_sensor_cards(self):
        cards_row = ft.Row(
            wrap=True,
            spacing=15,
        )
        
        for name, data in self.sensors.items():
            cards_row.controls.append(
                ft.Container(
                    width=250,
                    padding=15,
                    border_radius=12,
                    bgcolor=ft.colors.with_opacity(0.1, self.white_color),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(data["icon"], size=30, color=data["color"]),
                            ft.Text(name, size=16, weight="bold", color=self.white_color),
                            ft.Text(f"{data['value']} {data['unit']}", size=28, weight="bold", color=data["color"]),
                            ft.Container(
                                height=5,
                                border_radius=5,
                                bgcolor=ft.colors.with_opacity(0.2, data["color"]),
                                width=100,
                                content=ft.Container(
                                    width=random.randint(30, 100),
                                    height=5,
                                    border_radius=5,
                                    bgcolor=data["color"],
                                )
                            )
                        ]
                    )
                )
            )
        
        return cards_row
                    
    def _create_alert_panel(self):
        return ft.Container(
            margin=ft.margin.only(top=20),
            padding=15,
            border_radius=12,
            bgcolor=ft.colors.with_opacity(0.1, self.white_color),
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.icons.WARNING, color=self.yellow_color),
                            ft.Text("Alertas Recientes", size=18, weight="bold", color=self.white_color),
                        ],
                        spacing=10
                    ),
                    ft.Divider(height=10, color=self.grey_color),
                    ft.Column(
                        controls=[
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.INFO, color=self.yellow_color),
                                title=ft.Text("Temperatura alta detectada!", color=self.white_color),
                                subtitle=ft.Text("Hace 2 minutos", color=self.purple_color),
                                trailing=ft.Text("25.6℃", color="#FF5252", weight="bold"),
                            ),
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.INFO, color=self.yellow_color),
                                title=ft.Text("Humedad estable", color=self.white_color),
                                subtitle=ft.Text("Hace 5 minutos", color=self.purple_color),
                                trailing=ft.Text("65%", color="#4285F4", weight="bold"),
                            ),
                        ]
                    )
                ]
            )
        )
