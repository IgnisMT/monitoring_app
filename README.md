# Sistema de Monitoreo

Aplicación de escritorio para el monitoreo de datos en tiempo real, construida con Flet. Permite visualizar información de diversos sensores, rastrear eventos y configurar alertas.

## Características Detalladas

*   **Vista de Sensores (`SensorsView`)**: 
    *   Muestra tarjetas individuales para cada sensor (ej. Temperatura, Nivel de pH, Humedad, Oxígeno).
    *   Visualiza el valor actual, unidad, icono representativo y estado del sensor.
    *   Incluye un gráfico para visualizar tendencias de los datos de los sensores.
    *   Proporciona acciones rápidas como calibrar sensores, exportar datos y configurar alertas.
*   **Vista de Línea de Tiempo (`TimelineView`)**: (Descripción basada en el nombre)
    *   Presenta eventos relevantes y datos históricos en una secuencia cronológica.
*   **Vista de Rastreo (`TrackingView`)**: (Descripción basada en el nombre)
    *   Permite el seguimiento activo de elementos o procesos específicos.
*   **Vista de Monitor (`MonitorView`)**: (Descripción basada en el nombre)
    *   Ofrece un panel general con los indicadores clave y el estado general del sistema.
*   **Vista de Configuración (`SettingsView`)**: (Descripción basada en el nombre)
    *   Permite al usuario ajustar las preferencias y configuraciones de la aplicación.

## Componentes Principales

*   **`Header`**: Ubicado en la parte superior de la aplicación, muestra el título "Monitoreo", una barra de búsqueda para "actuadores" y la información del usuario ("Jesus Daniel", "Admin").
*   **`Menu`**: Barra lateral de navegación con iconos para acceder a las diferentes vistas: Sensores, Línea de Tiempo, Rastreo, Monitor y Configuración. El icono de la vista activa se resalta.

## Tecnologías Utilizadas

*   Python 3
*   Flet (Framework para interfaces gráficas de usuario)

## Estructura del Proyecto

```
main.py               # Punto de entrada principal de la aplicación
README.md             # Este archivo
assets/
	MT9.png             # Recursos gráficos (ej. logo)
components/
	__init__.py
	graph.py            # Lógica para crear gráficos (usado en SensorsView)
	header.py           # Define el componente Header
	menu.py             # Define el componente Menu
views/
	__init__.py
	monitor.py          # Lógica para la vista Monitor
	sensors.py          # Lógica para la vista Sensores
	settings.py         # Lógica para la vista Configuración
	timeline.py         # Lógica para la vista Línea de Tiempo
	tracking.py         # Lógica para la vista Rastreo
```

## Instalación y Ejecución

1.  **Clonar el repositorio (si aplica):**
    ```bash
    git clone <url-del-repositorio>
    cd <nombre-del-directorio-del-proyecto>
    ```
2.  **Asegúrate de tener Python instalado** (versión 3.x recomendada).
3.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
4.  **Instala las dependencias (principalmente Flet):**
    ```bash
    pip install flet
    ```
5.  **Ejecuta la aplicación:**
    ```bash
    python main.py
    ```

## Lógica Principal (`main.py`)

La aplicación se inicializa en `main.py` a través de la clase `MainApp`. Esta clase configura la ventana principal, los colores base, e instancia los componentes `Header` y `Menu`.

Define un diccionario `views` que mapea nombres de vistas a sus respectivas clases (ej. `"sensors": SensorsView(...)`).

La función `setup_menu_events` conecta los botones del `Menu` a la función `change_view`, la cual se encarga de cambiar la vista mostrada en el cuerpo principal de la aplicación y resaltar el icono del menú correspondiente.

La vista por defecto al iniciar la aplicación es `TrackingView`.

## Contribuir(Prueba no esta habilitado)

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1.  Haz un fork del repositorio.
2.  Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3.  Realiza tus cambios y haz commit (`git commit -am 'Añade nueva característica'`).
4.  Sube tus cambios a la rama (`git push origin feature/nueva-caracteristica`).
5.  Crea un nuevo Pull Request.

## Licencia

(Especifica aquí la licencia de tu proyecto, ej: MIT, GPL, etc. Si no tienes una, considera añadirla.)

