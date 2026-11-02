# Pellet al Día

Dónde hay pellet o leña seca, y alertas del PDA, en Temuco y Padre Las Casas.
App para **TINF1119 Desarrollo Móvil**, Evaluación N°3 (Proyecto Práctico N°2:
diseño y estructura app Kivy), hecha con **Kivy + KivyMD**. Proyecto individual de
Gabriel Neculman.

**Servicios integrados:** autenticación (registro y login) · persistencia en JSON ·
notificaciones · configuración remota. Detalle y ubicación en el código en
[Servicios implementados](#servicios-implementados).

## Problema que resuelve

En invierno cuesta encontrar pellet y la información está dispersa. En la
investigación, una persona necesitó «unos 7 viajes» en auto y otra no encontró
pellet en el supermercado. Además, ninguna de las personas consultadas se entera
a tiempo de las restricciones del Plan de Descontaminación Atmosférica (PDA).

**Pellet al Día** es una app colaborativa con **lista y mapa**:
- Los vecinos reportan dónde vieron **pellet o leña seca** (o si se acabó), con precio, sacos y horario.
- Cada dato muestra su **confiabilidad en estrellas**.
- La app te **lleva a pie o en auto** hasta el punto.
- Arriba de la lista se ve el **episodio del PDA del día** y qué hacer.

## Usuario objetivo

Familias de Temuco y Padre Las Casas que calefaccionan con pellet o leña,
especialmente las que tienen niños, adultos mayores o personas con problemas
respiratorios. Las personas consultadas tienen entre 18 y más de 60 años, y la
de más edad es la que más esfuerzo invierte en conseguir combustible. El
resumen de la investigación está en
[FUNDAMENTACION-UX-UI.md](FUNDAMENTACION-UX-UI.md) y la evidencia (pauta de entrevista, respuestas y plantilla de investigación)
se entrega aparte.

## Requisitos e instalación

- **Python 3.10, 3.11 o 3.12** (probado con Python 3.12 en Windows 11).
- **Git** para clonar el repositorio.
- **Internet** para el mapa, las rutas y la configuración remota. Sin internet la app
  igual abre: usa la última configuración guardada y rutas en línea recta.

Paso a paso (en una terminal; en Windows, PowerShell o CMD):

```bash
# 1. Clonar el repositorio y entrar a la carpeta
git clone https://github.com/vermeld/Evaluaci-n-N-3-Proyecto-Pr-ctico-N-2-Dise-o-y-estructura-app-Kivy.git
cd Evaluaci-n-N-3-Proyecto-Pr-ctico-N-2-Dise-o-y-estructura-app-Kivy

# 2. (Recomendado) crear un entorno virtual
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# 3. Instalar las dependencias
python -m pip install -r requirements.txt
```

Dependencias (`requirements.txt`): `kivy` 2.3, `kivymd` 2.0.0, `mapview` (mapa)
y `plyer` (GPS en Android y notificaciones).

## Cómo ejecutarla

```bash
python main.py
```

1. Se abre una ventana con forma de celular (400×800).
2. Toca **«Crear una cuenta»** y regístrate (las cuentas de ejemplo no tienen contraseña).
3. Entras a la **Lista**. Arriba está el aviso del PDA, que llega por **configuración
   remota**, y al abrir sale una **notificación** de Windows si hay restricción.
4. Cierra la app y vuelve a abrirla: la sesión, los puntos, reportes y opiniones
   siguen ahí porque se guardan en **JSON**.

En escritorio no hay GPS: tu ubicación parte en la Plaza Aníbal Pinto. Con
**doble toque** en el mapa la mueves, y durante una ruta el botón **«Simular
caminata»** hace avanzar tu punto. En Android la app usa el GPS real (`plyer`).

Para la demo hay dos botones de apoyo: **«Simular otro día (demo)»** en la pantalla
del PDA y **«Restaurar datos de ejemplo»** en Perfil › Ayuda.

## Servicios implementados

| Servicio | Qué hace | Dónde está |
|---|---|---|
| **Autenticación** | Registro e inicio de sesión. La contraseña se valida (6 caracteres o más, repetida igual) y se guarda como hash **PBKDF2-SHA256 con sal**, nunca en texto plano. El login compara con `hmac.compare_digest`. La sesión queda abierta al reabrir. | Validación: `validar_registro()` en `app/cuentas.py`. Hash: `_hash()`. Registro y login: `Cuentas.registrar()` y `Cuentas.entrar()`. Pantallas: `app/screens/registro.py` (`crear()`) y `app/screens/entrar.py` (`entrar()`) |
| **Persistencia JSON** | Los puntos, reportes, opiniones y votos se guardan en `puntos_temuco_v2.json`. Las cuentas y la sesión, en `usuarios.json`. Al reabrir la app se leen de nuevo. | `PelletApp.cargar()` y `PelletApp.guardar()` en `app/pelletapp.py`. Cuentas: `Cuentas.guardar()` en `app/cuentas.py`. Los archivos quedan en `App.user_data_dir` (en Windows, `%APPDATA%\pellet\`) |
| **Notificaciones** | Notificación del sistema (plyer) disparada por eventos de la app: **(1)** al abrir, si el PDA del día tiene alerta, preemergencia o emergencia; **(2)** al cambiar de episodio con «Simular otro día»; **(3)** al **llegar** al punto durante la navegación. También se muestra dentro de la app (Snackbar). | `notificar()` en `app/notificaciones.py`. Eventos: `al_recibir_config()` y `notificar_pda()` en `app/pelletapp.py`; `_llegar()` en `app/screens/mapa.py`; `simular_otro_dia()` en `app/screens/pda.py`. Texto y duración: `NOTIF_LLEGADA` y `NOTIF_SEGUNDOS` en `app/config.py` |
| **Configuración remota** | Al abrir, la app descarga [`remote_config.json`](remote_config.json) desde este repositorio en GitHub. Trae el **episodio del PDA del día** y un **mensaje** para todos. Si cambias el archivo en GitHub, la app lo muestra al volver a abrirse, sin tocar el código. Sin internet usa la última configuración guardada (`config_remota.json`) o los valores por defecto. La pantalla del PDA dice de dónde salió el dato. | `ConfigRemota` en `app/remoto.py` (`descargar()`, `validar()`). URL y valores por defecto: `REMOTO_URL` y `REMOTO_POR_DEFECTO` en `app/config.py`. Se pide en `PelletApp.on_start()` y se aplica en `aplicar_config_remota()` |

Ejemplo de `remote_config.json`:

```json
{
  "episodio_pda": "preemergencia",
  "mensaje": "Recuerda: con preemergencia no se puede usar leña. Revisa dónde hay pellet."
}
```

`episodio_pda` acepta `bueno`, `alerta`, `preemergencia` o `emergencia`. Si llega un
valor inválido se ignora y se mantiene el anterior. GitHub puede tardar unos
minutos en entregar la versión nueva del archivo.

### Quién llama a quién

```
main.py ─▶ app/pelletapp.py (PelletApp)
             ├─ carga los .kv de app/kv/ y crea las pantallas de app/screens/
             ├─ cargar() / guardar() ─▶ puntos_temuco_v2.json
             ├─ cuentas.py ─▶ usuarios.json            (registro, login, reputación)
             ├─ remoto.py  ─▶ remote_config.json en GitHub ─▶ config_remota.json (caché)
             ├─ notificaciones.py ─▶ plyer.notification
             └─ confianza.py, pda.py, ubicacion.py
           app/screens/mapa.py ─▶ rutas.py (OSRM) ─▶ geo.py ─▶ notificación «¡Llegaste!»
```

## Cuentas, opiniones y confiabilidad

- **Cuentas:** registro e inicio de sesión. La contraseña se guarda como hash
  PBKDF2-SHA256 con sal aleatoria, nunca en texto plano (`app/cuentas.py`). Si
  el usuario o la contraseña están mal, el mensaje es el mismo en ambos casos,
  para no revelar qué usuarios existen. Se puede **seguir sin cuenta** (solo
  mirar). Para publicar, reportar stock, opinar o votar hay que entrar.
- **Opiniones:** cada usuario califica un punto con 1 a 5 estrellas y un
  comentario (una opinión por punto, editable). Puede marcar además si había
  pellet, y eso suma un reporte.
- **Calificar opiniones:** los demás marcan cada opinión como **Útil** o **No útil**.
  Nadie puede votar su propia opinión.
- **Reputación y niveles:** +2 por cada voto útil recibido (−2 por cada no útil),
  +2 por publicar un punto y +1 por cada reporte u opinión. Niveles: **Nuevo** (0),
  **Confiable** (6) y **Experto** (15).
- **Confiabilidad del dato: de 0 a 5 estrellas, con medias estrellas** (`app/confianza.py`):
  `estrellas = 5 × (0,4 × frescura + 0,4 × respaldo + 0,2 × reputación)`, redondeado a la media estrella más cercana.
  - Frescura: qué tan reciente es el último reporte (llega a 0 a las 12 h).
  - Respaldo: reportes de 24 h que coinciden con el estado actual. Cada uno pesa según el nivel de su autor y se divide por el total, como mínimo por 2 (un solo reporte nunca basta).
  - Reputación: el nivel de quien hizo el último reporte.
  - Color: **amarillo** con 5 estrellas (excelente), **rojo** con 1½ o menos (poco confiable) y **verde** entre 2 y 4½. En los extremos se agrega la palabra, para no depender solo del color.
  - Las estrellas de confiabilidad son distintas de las **opiniones** (el promedio de 1 a 5 que ponen los usuarios), que se muestran con un ícono de comentario.

Las cuentas y los datos se guardan en el dispositivo (`usuarios.json` y
`puntos_temuco_v2.json`, dentro de `App.user_data_dir`). Las cuentas de ejemplo
(los vecinos que aparecen en las opiniones) no tienen contraseña. **Para probar,
crea tu propia cuenta** en «Crear una cuenta».

## Pantallas y navegación

Hay una barra inferior (`MDNavigationBar`) con 3 pestañas, **Lista · Mapa · Perfil**,
más 6 pantallas secundarias. Todas están en un `MDScreenManager`.

| # | Pantalla | .py | .kv | Qué se hace |
|---|----------|-----|-----|-------------|
| 1 | **Lista** (inicio) | `screens/lista.py` | `kv/lista.kv` | Puntos ordenados por cercanía, con confiabilidad en estrellas, filtros por stock y sector, y el botón **Publicar un punto** |
| 2 | **Mapa** | `screens/mapa.py` | `kv/mapa.kv` | Pines de colores según el stock, tarjeta del punto, **Cómo llegar** y navegación a pie con avance en vivo |
| 3 | **Perfil** | `screens/perfil.py` | `kv/perfil.kv` | Nivel, reputación, aportes, acceso a **Ayuda** y Cerrar sesión |
| 4 | Entrar / Crear cuenta | `screens/entrar.py`, `screens/registro.py` | `kv/entrar.kv`, `kv/registro.kv` | Inicio de sesión, registro con validación o «solo mirar» |
| 5 | Detalle | `screens/detalle.py` | `kv/detalle.kv` | Estado, confiabilidad, dirección, distancia a pie, horario, Cómo llegar, Sigue habiendo / Ya no hay, y opiniones con votos Útil / No útil |
| 6 | Publicar | `screens/formulario.py` | `kv/formulario.kv` | Formulario con validación (se abre desde la Lista) |
| 7 | Elegir ubicación | `screens/elegir.py` | `kv/elegir.kv` | Se mueve el mapa bajo un pin fijo para marcar el punto nuevo |
| 8 | Ayuda | `screens/ayuda.py` | `kv/ayuda.kv` | Colores, estrellas, cómo usar la app (se abre desde el Perfil) |
| 9 | Calidad del aire hoy | `screens/pda.py` | `kv/pda.kv` | Episodio del PDA (Alerta, Preemergencia, Emergencia), qué hacer y enlace al pronóstico oficial. Se abre desde el aviso de la Lista |

```
[Entrar] ─ Crear cuenta / Solo mirar ─▶ Lista
[Lista] ─ toca tarjeta ─▶ Detalle ─▶ confirmar / opinar / votar
   └─ Publicar un punto ─▶ Formulario ─ Ubicación ─▶ Elegir en mapa ─▶ Publicar ─▶ Mapa con el punto nuevo
[Mapa] ─ toca pin ─▶ tarjeta ─ Cómo llegar ─▶ ¿Caminando o en auto? ─▶ ruta + tu punto avanza ─▶ «¡Llegaste! ¿Había pellet?»
[Perfil] ─ ¿Tienes dudas? ─▶ Ayuda
   └─ Cerrar sesión ─▶ Entrar
```

## Cómo funciona el mapa

- **Estilo del mapa:** se usa Esri *World Street Map* a través de `kivy_garden.mapview` (`app/mapa.py`). Muestra solo calles y sus nombres, sin números de casas ni íconos de comercios, para que se lea fácil. Las teselas quedan en caché en la carpeta de datos de la app.
- **Cómo llegar:** la app pregunta **«¿Cómo vas a ir?»**:
  - **Caminando:** ruta por veredas y pasajes (servidor OSRM peatonal).
  - **En auto:** ruta que respeta el sentido de las calles (servidor OSRM de autos).

  Los minutos que faltan se calculan con la velocidad media que entrega el servidor para esa ruta (`app/rutas.py`). Si no hay internet, se usa una línea recta como respaldo.
- **Avance:** cada vez que cambia tu posición (GPS o simulada, `app/ubicacion.py`), se calcula el tramo más cercano de la ruta. La parte ya recorrida se pinta en gris y se actualizan los metros y minutos que faltan (`app/geo.py`, fórmula de Haversine). La app avisa que llegaste a menos de 20 m a pie o 35 m en auto.

## Componentes KivyMD usados

`MDNavigationBar`, `MDTopAppBar`, `MDButton` (filled, outlined, tonal, text),
`MDIconButton`, `MDTextField` (outlined, con ícono, hint y helper text), `MDCard`,
`MDDialog`, `MDDropdownMenu`, `MDSnackbar`, `MDLinearProgressIndicator`, `MDGridLayout`, `MDLabel`
(escala tipográfica Material 3), `MDIcon`, `MDScrollView` y `MDScreenManager`.

## Validaciones

- Registro: nombre de 2 caracteres o más; usuario de 3 a 20 caracteres (letras, números, `.` o `_`) que no esté repetido; contraseña de 6 caracteres o más, repetida igual.
- Opinión: de 1 a 5 estrellas y un texto de 5 a 280 caracteres.
- Nombre, dirección y ubicación en el mapa son obligatorios. El campo que falta se marca en rojo y recibe el foco.
- Si había pellet, se piden los sacos y el precio. Solo se aceptan números, y un precio menor a $500 se rechaza.
- Las horas se validan con formato `HH:MM`.
- Antes de publicar o de cambiar el estado de un punto, la app muestra un diálogo de confirmación.

## Estructura del proyecto

```
pellet/
├── main.py                     # punto de entrada
├── requirements.txt
├── README.md
├── USO_IA.md                   # declaración de uso de inteligencia artificial
├── remote_config.json          # configuración remota que lee la app desde GitHub
├── FUNDAMENTACION-UX-UI.md     # fundamentación del diseño con evidencia de usuarios
├── assets/                     # íconos del mapa (pines, "tú")
├── tools/generar_iconos.py     # genera los PNG de assets/
├── docs/capturas/              # capturas de pantalla
└── app/
    ├── pelletapp.py            # MDApp: build(), ScreenManager, barra inferior, datos, acciones
    ├── cuentas.py              # registro, login (hash PBKDF2), reputación y niveles
    ├── confianza.py            # estrellas de confiabilidad de cada punto
    ├── config.py               # sectores, mapa, colores, URL remota, textos de notificación
    ├── remoto.py               # configuración remota (descarga, validación y caché)
    ├── notificaciones.py       # notificaciones del sistema (plyer)
    ├── pda.py                  # niveles del PDA y qué hacer en cada uno
    ├── data.py                 # puntos, vecinos, reportes y opiniones de ejemplo (ficticios)
    ├── mapa.py                 # MapView, pines, capa de la ruta
    ├── rutas.py                # ruta a pie o en auto (OSRM)
    ├── ubicacion.py            # GPS (Android) o ubicación simulada
    ├── geo.py                  # distancias y avance sobre la ruta
    ├── utils.py                # formato de fecha, dinero y textos de un punto
    ├── widgets.py              # PuntoCard, OpinionCard, ItemNav, Raiz
    ├── compat.py               # parche de un bug de KivyMD 2.0.0 (ripple con alto 0)
    ├── kv/                     # interfaz declarativa (KV Language), un .kv por pantalla
    └── screens/                # lógica de cada pantalla
```

La **interfaz** está en los `.kv` y la **lógica** (filtros, validación, rutas,
eventos) en los `.py`. Cada pantalla tiene su clase en `app/screens/` y su
interfaz en `app/kv/`.

## Calidad del aire (PDA)

Arriba de la Lista aparece un aviso con el episodio del día (por ejemplo, **«Hoy:
Alerta ambiental»**). Al tocarlo se abre una pantalla con qué hacer, los niveles
del PDA, la aclaración de que rige en todo Temuco y Padre Las Casas, y un botón
al pronóstico oficial (airechile.mma.gob.cl).

El episodio del día llega por **configuración remota** (`remote_config.json` en
GitHub) y, si hay restricción, la app envía una **notificación**. Para la demo, el
botón «Simular otro día (demo)» cambia el episodio y vuelve a notificar. En una
versión real, el archivo remoto se actualizaría cada día con el pronóstico oficial.

## Guía para leer el código

Cada botón, pestaña, campo y pantalla tiene un comentario con una etiqueta que
se puede buscar en VS Code con **Ctrl+Shift+F**, por ejemplo `BOTÓN «Cómo llegar»`
o `PESTAÑA «Mapa»`.

## Capturas

| Mapa | Navegando | Llegada |
|---|---|---|
| ![](docs/capturas/1_mapa.png) | ![](docs/capturas/2_navegacion.png) | ![](docs/capturas/3_llegada.png) |

| Lista | Detalle | Publicar | Marcar ubicación | Ayuda |
|---|---|---|---|---|
| ![](docs/capturas/4_lista.png) | ![](docs/capturas/5_detalle.png) | ![](docs/capturas/6_formulario.png) | ![](docs/capturas/7_elegir_ubicacion.png) | ![](docs/capturas/8_ayuda.png) |

| Calidad del aire (PDA) | Preemergencia | Qué vende |
|---|---|---|
| ![](docs/capturas/17_pda.png) | ![](docs/capturas/18_pda_preemergencia.png) | ![](docs/capturas/19_que_vende.png) |

| Entrar | Crear cuenta | Opiniones | Perfil | Cómo se calcula | Confiabilidad baja |
|---|---|---|---|---|---|
| ![](docs/capturas/9_entrar.png) | ![](docs/capturas/10_crear_cuenta.png) | ![](docs/capturas/11_opiniones.png) | ![](docs/capturas/12_perfil.png) | ![](docs/capturas/13_confiabilidad.png) | ![](docs/capturas/14_confiabilidad_baja.png) |

## Dificultades y cómo se resolvieron

| Dificultad | Solución |
|---|---|
| Con KivyMD 2.0.0 la app se caía al abrir en algunas tarjetas de video («FBO Initialization failed: Incomplete attachment»), porque el efecto *ripple* se crea con alto 0. | Parche en `app/compat.py` que fuerza un tamaño mínimo de 1×1. Se aplica al inicio de `pelletapp.py`. |
| VS Code usaba otro Python, sin KivyMD instalado (`ModuleNotFoundError: kivymd`). | Elegir el intérprete correcto en VS Code e instalar `requirements.txt` en ese Python. |
| Las teselas del mapa de CARTO empezaron a pedir una clave de pago. | Cambio a Esri *World Street Map*, que además muestra solo calles (sin números ni íconos de comercios). |
| La caché del mapa se guardaba en una carpeta relativa y fallaba según desde dónde se abría la app. | Se pasa `cache_dir` dentro de `user_data_dir`. |
| Clic derecho dejaba puntos rojos en la pantalla (Kivy simula multitáctil). | `Config.set("input", "mouse", "mouse,multitouch_on_demand")` en `main.py`, antes de crear la ventana. |
| El símbolo ★ no existe en la fuente Roboto y salía como un cuadro. | Se usan íconos de Material Design (`star`, `star-half-full`). |
| Los datos de ejemplo quedaban «viejos» (todo en ámbar) días después. | Botón «Restaurar datos de ejemplo» que vuelve a crear los puntos con horas recientes. |
| GitHub *raw* responde el JSON como texto plano y además lo guarda en caché. | `remoto.py` convierte el texto con `json.loads` y agrega `?t=<hora>` a la URL para pedir la versión nueva. |
| Sin internet, la configuración remota no llega. | Se guarda la última recibida en `config_remota.json` y, si nunca llegó, se usan los valores de `REMOTO_POR_DEFECTO`. |
| La extensión de Kivy de VS Code marcaba error en los `.kv` («Kivy files require #:kivy»). | Se agregó la cabecera `#:kivy 2.3.0` en cada `.kv`. |

## Créditos

- Mapa: Esri World Street Map (fuentes: Esri, HERE, Garmin y colaboradores de [OpenStreetMap](https://www.openstreetmap.org/copyright)).
- Rutas: [OSRM](https://project-osrm.org/) (servidores de routing.openstreetmap.de, perfiles peatonal y de auto).

## Uso de inteligencia artificial

La declaración completa (herramienta, modelo, prompts, outputs, ajustes y
reflexión) está en [USO_IA.md](USO_IA.md).
