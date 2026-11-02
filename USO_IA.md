# Declaración de uso de inteligencia artificial

Proyecto: **Pellet al Día** · TINF1119 Desarrollo Móvil · Evaluación N°3
Estudiante: Gabriel Neculman

## 1. IA usada

Sí se usó inteligencia artificial.

- **Claude**, de Anthropic, a través de **Claude Code** (aplicación de escritorio de
  Claude, pestaña Code), con acceso a la carpeta del proyecto en el computador.
- Período: desde el 28 de septiembre de 2026 (Evaluación 2) hasta noviembre de 2026
  (Evaluación 3).

No se usaron otras herramientas de IA.

## 2. Modelo

- **Claude Opus 5.5** (identificador `claude-opus-5-5`), según lo que informa Claude
  Code. El proyecto se trabajó en varias sesiones y el modelo podría haber cambiado
  entre ellas; este es el que figura en la sesión actual.
- Los commits hechos con ayuda de la IA llevan la línea
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, que queda registrada en
  el historial del repositorio.

## 3. Prompts realizados

Prompts que explican decisiones del proyecto, en orden. Las frases entre comillas son
textuales; el resto está resumido con fidelidad.

**Evaluación 2 (maqueta):**

1. Le pasé la carpeta del proyecto y la pauta de la E2 (rúbrica en Word): tengo que
   terminar una app funcional en Kivy y presentarla.
2. «no me deja abrir la app» (con captura del error `ModuleNotFoundError: kivymd`).
3. Que se parezca más a una app de celular, con un mapa de la ciudad como Google Maps,
   que marque el destino y vaya avanzando mientras camino, con locales en Temuco.
4. Le pasé la investigación con usuarios que hice (pauta de 15 preguntas y las
   respuestas del formulario) y le pedí que la app coincidiera con la investigación.
5. Agregar cuentas de usuario, calificación de los puntos y de los comentarios de
   otros usuarios, y un nivel de confiabilidad.
6. Mostrar la confiabilidad con estrellas en vez de porcentaje: amarillas con 5, rojas
   con 1,5 o menos y verdes en el resto.
7. (Con captura) La lista primero, el mapa al medio y el perfil al final; la Ayuda
   dentro del Perfil y «Publicar» como botón en la Lista.
8. Que el mapa no muestre números de casas ni íconos de comida, clínicas u hoteles,
   solo nombres de calles, y que «Cómo llegar» pregunte si voy en auto o caminando.
9. Comentar todo el código para poder encontrar cada parte, por ejemplo «donde está el
   botón del mapa».
10. Armar la presentación y un diálogo para exponerla.

**Evaluación 3 (este proyecto):**

11. Le pasé las instrucciones completas de la Evaluación N°3 con «ahora tenemos que
    hacer esto».
12. Elegí que la notificación se dispare con la **alerta del PDA del día** y al
    **llegar al punto**, y que se entregue en este repositorio.
13. Le pedí explicar cada parte del proyecto: qué hace cada archivo, qué es
    OpenStreetMap, para qué son las imágenes de `assets/`, qué hace `.gitignore`,
    dónde están los estilos y por qué los `.kv` aparecían en rojo en VS Code.

## 4. Outputs

Lo que entregó la herramienta, y qué se tomó o se descartó:

| Output de la IA | ¿Se tomó? |
|---|---|
| Código de la app en `.py` y `.kv`: pantallas, ScreenManager, mapa, rutas, cuentas, estrellas de confiabilidad, PDA | Sí, revisado y probado |
| Migración de Kivy a KivyMD 2.0 y corrección de un error de KivyMD (`app/compat.py`) | Sí |
| E3: `app/remoto.py` (configuración remota), `app/notificaciones.py` (notificaciones) y su conexión con `pelletapp.py`, `screens/pda.py` y `screens/mapa.py` | Sí |
| E3: archivo `remote_config.json` y la sección «Servicios implementados» del README | Sí |
| Comentarios en español en todo el código, con etiquetas buscables (`BOTÓN «…»`, `PESTAÑA «…»`) | Sí |
| `FUNDAMENTACION-UX-UI.md`: ordenó mis respuestas en hallazgos, matriz y supuestos | Sí, con las citas revisadas contra el formulario |
| Presentación de diapositivas y diálogo para exponer (E2) | Sí, como apoyo para ensayar |
| Explicaciones de cada archivo y de conceptos (OpenStreetMap, OSRM, `.gitignore`, estilos en KV) | Sí, para estudiar la defensa |
| Mapa con estilo CARTO | **Descartado**: empezó a pedir clave de pago. Se cambió a Esri |
| Confiabilidad en porcentaje | **Descartado**: pedí estrellas, más fáciles de entender |
| Navegación con Ayuda como pestaña y el mapa como pantalla de inicio | **Descartado**: pedí la lista primero y la Ayuda dentro del Perfil |
| Inventar respuestas de personas para la investigación | **Descartado**: la investigación se hizo con personas reales (3 respuestas al formulario) |

## 5. Ajustes

Qué se modificó respecto de lo que entregó la IA, y por qué:

- **Orden de la navegación.** La primera versión abría en el mapa. Lo cambié a Lista →
  Mapa → Perfil, con la Ayuda dentro del Perfil y «Publicar» como botón en la Lista.
- **Confiabilidad en estrellas.** La IA la mostraba en porcentaje. Pedí estrellas con
  colores (amarillo con 5, rojo con 1,5 o menos, verde el resto).
- **Mapa más limpio.** Pedí quitar números de casas e íconos de comercios para que solo
  se vean las calles y los pines de pellet.
- **A pie o en auto.** Pedí que «Cómo llegar» pregunte si voy caminando o en auto.
- **Errores que encontré al usar la app:** puntos rojos al hacer clic derecho, datos de
  ejemplo antiguos (todo en ámbar) y el texto «quedaban 0 sacos». Se corrigieron.
- **Investigación real.** No acepté datos inventados: las decisiones de diseño salen de
  respuestas reales, y las que no tienen respaldo quedaron marcadas como supuestos.
- **E3:** elegí qué evento dispara la notificación (alerta del PDA y llegada) y que la
  configuración remota controle el episodio del PDA, porque 3 de 3 personas
  encuestadas no se enteran a tiempo de las restricciones.
<!-- Gabriel: si quieres, agrega el porqué de cada cambio con tus palabras. -->
- **Ediciones propias:** cambios de texto en el README y en comentarios de `config.py`.

<!-- Gabriel: agrega aquí los cambios que hagas tú mismo al código antes de la defensa
     (por ejemplo, si ensayas cambiar el texto de una notificación o el valor por
     defecto de la configuración remota). -->

## 6. Reflexión en el uso de IA

<!-- Esta sección la tiene que escribir Gabriel con sus propias palabras: la pauta
     evalúa que sea propia y honesta. Preguntas que pueden ayudar:
     - ¿Qué te sirvió más de usar la IA?
     - ¿Qué te costó? (entender código que no escribiste, revisar que funcionara…)
     - ¿Qué aprendiste del proceso y qué harías distinto la próxima vez?
     Borra este comentario cuando la escribas. -->

[Escribe aquí tu reflexión, de 5 a 10 líneas.]
