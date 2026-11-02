# -*- coding: utf-8 -*-
"""Notificaciones del sistema (las que aparecen fuera de la app).

Usa plyer: en Windows sale el aviso en la esquina de la pantalla y en Android
en la barra de notificaciones. Si el sistema no las permite, se muestra el
mismo texto dentro de la app (Snackbar), para que el aviso nunca se pierda.

Eventos que disparan una notificación (ver pelletapp.py y screens/mapa.py):
  - Al abrir la app, si el PDA del día (configuración remota) tiene restricción.
  - Al cambiar el episodio con «Simular otro día (demo)».
  - Al llegar caminando o en auto al punto elegido.
"""

from . import config


# ENVÍA UNA NOTIFICACIÓN. Devuelve True si el sistema la aceptó.
def notificar(titulo, mensaje):
    try:
        from plyer import notification
        notification.notify(title=titulo, message=mensaje,
                            app_name="Pellet al Día",
                            timeout=config.NOTIF_SEGUNDOS)
        return True
    except Exception:  # plyer no instalado o el sistema no soporta notificaciones
        return False
