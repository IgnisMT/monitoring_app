import flet as ft

class Menu(ft.Container):
    def __init__(self, page: ft.Page, purple_color: str, white_color: str, grey_color: str):
        super().__init__(width=60, border_radius=10, padding=5)
        self.bgcolor = grey_color
        
        # Guarda los iconos como atributos para acceder luego
        self.sensors_btn = ft.IconButton(icon=ft.icons.SENSORS, icon_color=white_color)
        self.timeline_btn = ft.IconButton(icon=ft.icons.TIMELINE, icon_color=white_color)
        self.tracking_btn = ft.IconButton(icon=ft.icons.TRACK_CHANGES, icon_color=white_color)
        self.monitor_btn = ft.IconButton(icon=ft.icons.MONITOR_HEART, icon_color=white_color)
        self.settings_btn = ft.IconButton(icon=ft.icons.SETTINGS, icon_color=white_color)

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            controls=[
                ft.Column([
                    self.sensors_btn,
                    self.timeline_btn, 
                    self.tracking_btn, 
                    self.monitor_btn
                ]),
                ft.Column([
                    self.settings_btn
                ])
            ]
        )
