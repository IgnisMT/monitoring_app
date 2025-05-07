import flet as ft
import random
from components.graph import create_graph

class TrackingView(ft.Container):
    def __init__(self, page: ft.Page, purple_color: str, white_color: str, yellow_color: str, grey_color: str):
        super().__init__(expand=True)
        self.page = page
        self.purple_color = purple_color
        self.white_color = white_color
        self.yellow_color = yellow_color
        self.grey_color = grey_color
        self.current_view = "days"
        
        horas = ["7 am", "8 am", "9 am", "10 am", "11 am", "12 pm", "1 pm", "2 pm", "3 pm", "4 pm", "5 pm", "6 pm"]
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        años = ["2020", "2021", "2022", "2023", "2024"]
        
        # Inicializa gráficas
        self.graph_days = create_graph(self.purple_color, self.white_color, self.yellow_color, self.grey_color, horas)
        self.graph_months = create_graph(self.purple_color, self.white_color, self.yellow_color, self.grey_color, meses)
        self.graph_years = create_graph(self.purple_color, self.white_color, self.yellow_color, self.grey_color, años)
        
        # Crea botones de periodo
        self.btn_days = ft.TextButton(
            text="Días",
            style=ft.ButtonStyle(color=self.yellow_color),
            on_click=lambda e: self.change_view("days"),
        )
        
        self.btn_months = ft.TextButton(
            text="Meses",
            style=ft.ButtonStyle(color=self.white_color),
            on_click=lambda e: self.change_view("months"),
        )
        
        self.btn_years = ft.TextButton(
            text="Años",
            style=ft.ButtonStyle(color=self.white_color),
            on_click=lambda e: self.change_view("years"),
        )
        
        # Current graph based on view
        self.current_graph = self.graph_days
        
        # Main content
        self.content = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=20,
            controls=[
                self._create_header(),
                self._create_period_selector(),
                ft.Container(
                    padding=20,
                    content=self.current_graph,
                    border_radius=15,
                    bgcolor=ft.colors.with_opacity(0.05, self.white_color),
                    expand=True,
                ),
                self._create_statistics(),
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
                            ft.Icon(ft.icons.TRACK_CHANGES, color=self.yellow_color),
                            ft.Text("Seguimiento de Datos", size=24, weight="bold", color=self.white_color),
                        ],
                        spacing=10
                    ),
                    ft.Text("Análisis detallado del rendimiento del sistema",
                            size=14, color=ft.colors.with_opacity(0.4, self.white_color)),
                    ft.Divider(height=10, color=self.grey_color),
                ]
            )
        )
    
    def _create_period_selector(self):
        return ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.btn_days,
                    self.btn_months,
                    self.btn_years,
                ]
            ),
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.with_opacity(0.1, self.grey_color),
        )
    
    def _create_statistics(self):
        return ft.Container(
            padding=20,
            content=ft.Column(
                spacing=15,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.icons.INSERT_CHART, color=self.yellow_color),
                            ft.Text("Estadísticas", size=20, weight="bold", color=self.white_color),
                        ],
                    ),
                    ft.Divider(height=10, color=self.grey_color),
                    ft.Row(
                        controls=[
                            self._create_stat_card("Promedio", "15.8 kWh", ft.icons.TRENDING_UP, "#4CAF50"),
                            self._create_stat_card("Máximo", "24.3 kWh", ft.icons.ARROW_UPWARD, "#F44336"),
                            self._create_stat_card("Mínimo", "7.2 kWh", ft.icons.ARROW_DOWNWARD, "#2196F3"),
                            self._create_stat_card("Total", "356.4 kWh", ft.icons.EQUALIZER, "#FF9800"),
                        ],
                        wrap=True,
                        spacing=10,
                    )
                ]
            ),
            border_radius=15,
            bgcolor=ft.colors.with_opacity(0.05, self.white_color),
        )
    
    def _create_stat_card(self, title, value, icon, color):
        return ft.Container(
            width=200,
            padding=15,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.Icon(icon, size=30, color=color),
                    ft.Text(title, size=14, color=self.white_color),
                    ft.Text(value, size=22, weight="bold", color=self.white_color),
                ],
            ),
            border_radius=10,
            bgcolor=ft.colors.with_opacity(0.1, self.grey_color),
        )
    
    def change_view(self, view_name):
        self.current_view = view_name
        
        # Reset button colors
        self.btn_days.style = ft.ButtonStyle(color=self.white_color)
        self.btn_months.style = ft.ButtonStyle(color=self.white_color)
        self.btn_years.style = ft.ButtonStyle(color=self.white_color)
        
        # Update current graph and highlight selected button
        if view_name == "days":
            self.current_graph = self.graph_days
            self.btn_days.style = ft.ButtonStyle(color=self.yellow_color)
        elif view_name == "months":
            self.current_graph = self.graph_months
            self.btn_months.style = ft.ButtonStyle(color=self.yellow_color)
        elif view_name == "years":
            self.current_graph = self.graph_years
            self.btn_years.style = ft.ButtonStyle(color=self.yellow_color)
        
        # Update the graph in the UI
        self.content.controls[2].content = self.current_graph
        self.page.update()