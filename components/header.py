import flet as ft

class Header(ft.Container):
    def __init__(self, page: ft.Page, purple_color: str, white_color: str, grey_color: str):
        super().__init__(height=60)
        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row([
                    ft.Text(
                        value="Monitoreo",
                        color=purple_color,
                        size=20,
                        weight="bold"
                    )
                ]),
                
                ft.Row(
                    controls=[
                        ft.TextField(
                            text_align=ft.TextAlign.CENTER, 
                            hint_text="Buscar actuadores",
                            border_width=0, 
                            hint_style=ft.TextStyle(color=ft.colors.with_opacity(0.4, white_color))
                        ),
                        ft.IconButton(
                            icon=ft.icons.SEARCH, 
                            icon_color=ft.colors.with_opacity(0.4, white_color)
                        )
                    ]
                ),
                
                ft.Row(
                    controls=[
                        ft.Column(
                            spacing=0,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                            controls=[
                                ft.Text(value="Jesus Daniel", weight="bold", size=20, color=white_color),
                                ft.Text(value="Admin", color=ft.colors.with_opacity(0.4, white_color))
                            ]
                        ),
                        ft.Container(
                            width=40,
                            height=40,
                            border_radius=20,
                            bgcolor=purple_color,
                            alignment=ft.alignment.center,
                            content=ft.Text("JD", color=white_color, weight="bold")
                        )
                    ]
                )
            ]
        )