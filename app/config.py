# -*- coding: utf-8 -*-
"""Constantes de configuración: sectores de Temuco, mapa, colores y ventana."""

# Sectores de Temuco (y Padre Las Casas, al otro lado del río Cautín).
SECTORES = [
    "Centro", "Av. Alemania", "Pueblo Nuevo", "Amanecer", "Santa Rosa",
    "Pedro de Valdivia", "Fundo El Carmen", "Labranza", "Padre Las Casas",
]

HORAS_PARA_DUDAR = 6  # después de esto, un "hay pellet" deja de ser confiable

# Qué vende cada punto (la investigación habla de pellet y de leña seca)
COMBUSTIBLES = {
    "pellet": "Pellet",
    "lena": "Leña seca",
    "ambos": "Pellet y leña seca",
}

# ---- configuración remota (ver remoto.py)
# Archivo JSON publicado en el repositorio de GitHub. Si se edita en GitHub,
# la app muestra el valor nuevo la próxima vez que se abre (sin cambiar el código).
REMOTO_URL = ("https://raw.githubusercontent.com/vermeld/"
              "Evaluaci-n-N-3-Proyecto-Pr-ctico-N-2-Dise-o-y-estructura-app-Kivy/"
              "main/remote_config.json")
REMOTO_ESPERA = 8  # segundos máximos esperando la respuesta
# VALORES POR DEFECTO: se usan si no hay internet y nunca se descargó la configuración.
REMOTO_POR_DEFECTO = {
    "episodio_pda": "alerta",  # bueno, alerta, preemergencia o emergencia
    "mensaje": "",             # aviso corto que se muestra bajo el PDA en la Lista
}

# ---- notificaciones (ver notificaciones.py)
NOTIF_SEGUNDOS = 10  # cuánto dura la notificación en pantalla (escritorio)
NOTIF_LLEGADA = "Estás en %s. ¿Había stock? Abre la app y cuéntale a tus vecinos."

# ---- mapa
CENTRO_TEMUCO = (-38.7390, -72.5985)
ZOOM_INICIAL = 14
# Sin GPS (escritorio) partimos en la Plaza Aníbal Pinto.
UBICACION_SIMULADA = (-38.73905, -72.59040)
# Estilo de mapa limpio (Esri World Street Map): solo calles y sus nombres,
# sin números de casas ni íconos de comercios.
TILES_URL = ("https://server.arcgisonline.com/ArcGIS/rest/services/"
             "World_Street_Map/MapServer/tile/{z}/{y}/{x}")
TILES_EXT = "jpg"
TILES_CACHE = "esri_calles"
TILES_ATRIBUCION = "Esri · © OpenStreetMap"
# Los servicios de mapas piden identificar la app que hace las consultas.
USER_AGENT = "PelletAlDia/1.0 (proyecto academico UC Temuco)"

# Servidores OSRM (OpenStreetMap): a pie usa veredas y pasajes; en auto respeta
# el sentido de las calles.
RUTAS_URL = {
    "pie": ("https://routing.openstreetmap.de/routed-foot/route/v1/foot/"
            "{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson"),
    "auto": ("https://routing.openstreetmap.de/routed-car/route/v1/driving/"
             "{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson"),
}
MODOS = {
    # velocidad: m/s de respaldo si el servidor no da la duración
    # simulada: m/s de la demo en escritorio · llegada: metros para "¡Llegaste!"
    "pie": {"velocidad": 1.3, "simulada": 25.0, "llegada": 20,
            "texto": "a pie", "icono": "walk", "nombre": "Caminando"},
    "auto": {"velocidad": 7.0, "simulada": 60.0, "llegada": 35,
             "texto": "en auto", "icono": "car", "nombre": "En auto"},
}
VELOCIDAD_CAMINANDO = MODOS["pie"]["velocidad"]

# En escritorio simulamos una pantalla de celular. En Android se ignora.
VENTANA_ANCHO = 400
VENTANA_ALTO = 800

# Paleta Material (KivyMD) para superficies, botones y barras.
PALETA = "Green"

# Semáforo de stock: se usan siempre junto a un texto e ícono, nunca solo por color.
C_HAY = (0.106, 0.478, 0.263, 1)    # verde: hay stock
C_NOHAY = (0.729, 0.176, 0.145, 1)  # rojo: sin stock
C_DUDA = (0.604, 0.388, 0.0, 1)     # ámbar oscuro: dato viejo
C_RUTA = (0.102, 0.451, 0.910, 1)   # azul de la ruta y de "tú"
C_ORO = (0.961, 0.722, 0.0, 1)      # amarillo: confiabilidad de 5 estrellas
C_ORO_TEXTO = (0.620, 0.431, 0.0, 1)  # el mismo tono más oscuro, para texto legible
