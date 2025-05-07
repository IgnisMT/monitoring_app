import flet as ft
import random
from components.menu import Menu
from components.header import Header
from views.sensors import SensorsView
from views.timeline import TimelineView
from views.tracking import TrackingView
from views.monitor import MonitorView
from views.settings import SettingsView

class MainApp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.title = "Sistema de Monitoreo"
        self.page.bgcolor = "#000000"
        self.page.padding = 20
        self.page.window_width = 1200
        self.page.window_height = 800
        self.page.window_min_width = 800
        self.page.window_min_height = 600

        # Colores
        self.black_color = "#000000"
        self.purple_color = "#9458cf"
        self.white_color = "#ffffff"
        self.yellow_color = "#f1c846"
        self.grey_color = "#191a15"

        # Componentes
        self.header = Header(self.page, self.purple_color, self.white_color, self.grey_color)
        self.menu = Menu(self.page, self.purple_color, self.white_color, self.grey_color)

        # Vistas
        self.views = {
            "sensors": SensorsView(self.page, self.purple_color, self.white_color, self.yellow_color, self.grey_color),
            "timeline": TimelineView(self.page, self.purple_color, self.white_color, self.yellow_color, self.grey_color),
            "tracking": TrackingView(self.page, self.purple_color, self.white_color, self.yellow_color, self.grey_color),
            "monitor": MonitorView(self.page, self.purple_color, self.white_color, self.yellow_color, self.grey_color),
            "settings": SettingsView(self.page, self.purple_color, self.white_color, self.yellow_color, self.grey_color),
        }

        # Configurar eventos del menú
        self.setup_menu_events()

        # Vista actual
        self.current_view = self.views["tracking"]

        # Cuerpo principal
        self.body = ft.Container(
            expand=True,
            content=ft.Row(
                controls=[
                    self.menu,
                    self.current_view
                ],
                spacing=20
            )
        )

        # Diseño principal
        self.content = ft.Column(
            expand=True,
            controls=[
                self.header,
                self.body,
            ],
            spacing=20
        )

    def setup_menu_events(self):
        # Configuración de eventos para los botones del menú
        self.menu.sensors_btn.on_click = lambda e: self.change_view("sensors")
        self.menu.timeline_btn.on_click = lambda e: self.change_view("timeline")
        self.menu.tracking_btn.on_click = lambda e: self.change_view("tracking")
        self.menu.monitor_btn.on_click = lambda e: self.change_view("monitor")
        self.menu.settings_btn.on_click = lambda e: self.change_view("settings")
        
    def change_view(self, view_name: str):
        self.body.content.controls[1] = self.views[view_name]
        
        # Reset all icons to white
        self.menu.sensors_btn.icon_color = self.white_color
        self.menu.timeline_btn.icon_color = self.white_color
        self.menu.tracking_btn.icon_color = self.white_color
        self.menu.monitor_btn.icon_color = self.white_color
        self.menu.settings_btn.icon_color = self.white_color
        
        # Highlight selected icon
        if view_name == "sensors":
            self.menu.sensors_btn.icon_color = self.yellow_color
        elif view_name == "timeline":
            self.menu.timeline_btn.icon_color = self.yellow_color
        elif view_name == "tracking":
            self.menu.tracking_btn.icon_color = self.yellow_color
        elif view_name == "monitor":
            self.menu.monitor_btn.icon_color = self.yellow_color
        elif view_name == "settings":
            self.menu.settings_btn.icon_color = self.yellow_color
            
        self.page.update()

def main(page: ft.Page):
    app = MainApp(page)
    page.add(app)

if __name__ == "__main__":
    ft.app(target=main)