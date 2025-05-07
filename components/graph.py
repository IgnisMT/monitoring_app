import flet as ft
import random

def create_graph(purple_color: str, white_color: str, yellow_color: str, grey_color: str, data):
    # En versiones antiguas de Flet, no existe LineChart, así que crearemos una visualización alternativa
    # Crea un gráfico simulado usando Container
    
    chart_height = 300
    chart_width = 600
    
    # Valores aleatorios para visualización
    valores = [random.randint(5, 20) for _ in range(len(data))]
    
    # Crea contenedores para representar barras
    bars = []
    for i in range(len(data)):
        # Altura basada en el valor aleatorio
        height = valores[i] * 10
        
        # Crea una barra
        bar = ft.Container(
            width=30,
            height=height,
            bgcolor=purple_color,
            border_radius=ft.border_radius.only(top_left=5, top_right=5),
            tooltip=f"Valor: {valores[i]}",
            margin=ft.margin.only(right=10),
        )
        
        # Crea un contenedor para la etiqueta
        label = ft.Container(
            content=ft.Text(str(data[i]), color=white_color, size=10),
            margin=ft.margin.only(top=5),
            alignment=ft.alignment.center,
            width=30,
        )
        
        # Agrega la barra y etiqueta a una columna
        column = ft.Column(
            controls=[
                bar,
                label
            ],
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        bars.append(column)
    
    # Crea una fila con todas las barras
    chart = ft.Container(
        content=ft.Row(
            controls=bars,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        height=chart_height,
        width=chart_width,
        padding=20,
        alignment=ft.alignment.bottom_center,
    )
    
    # Agrega decoración
    decorated_chart = ft.Container(
        content=chart,
        border=ft.border.all(1, color=ft.colors.with_opacity(0.2, white_color)),
        border_radius=10,
        padding=10,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[
                ft.colors.with_opacity(0.05, purple_color),
                ft.colors.with_opacity(0.0, purple_color),
            ],
        ),
    )
    
    return decorated_chart

# Función simplificada para las vistas de sensores
def create_graph_sensors(purple_color: str, white_color: str, yellow_color: str, grey_color: str, data):
    return create_graph(purple_color, white_color, yellow_color, grey_color, data)