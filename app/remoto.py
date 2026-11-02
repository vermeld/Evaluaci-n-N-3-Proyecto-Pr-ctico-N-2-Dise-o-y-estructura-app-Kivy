# -*- coding: utf-8 -*-
"""Configuración remota: valores que se leen desde internet al abrir la app.

La fuente es el archivo remote_config.json del repositorio en GitHub
(config.REMOTO_URL). Así se puede cambiar el episodio del PDA del día o un
mensaje para todos los usuarios sin publicar una versión nueva de la app.

Orden de prioridad (de dónde sale cada valor):
  1. «remota»:    lo que respondió GitHub ahora.
  2. «guardada»:  la última configuración que se descargó (sirve sin internet).
  3. «por defecto»: config.REMOTO_POR_DEFECTO, escrita en el código.
"""

import json
import os
import time

from kivy.network.urlrequest import UrlRequest

from . import config, pda

ARCHIVO_CACHE = "config_remota.json"


# Revisa que lo que llegó tenga sentido. Devuelve solo las claves válidas.
def validar(datos):
    if not isinstance(datos, dict):
        return {}
    limpio = {}
    if datos.get("episodio_pda") in pda.ORDEN:
        limpio["episodio_pda"] = datos["episodio_pda"]
    if isinstance(datos.get("mensaje"), str):
        limpio["mensaje"] = datos["mensaje"].strip()[:140]
    return limpio


class ConfigRemota:
    """Guarda los valores actuales y de dónde salieron (origen)."""

    def __init__(self, carpeta):
        self.cache = os.path.join(carpeta, ARCHIVO_CACHE)
        self.valores = dict(config.REMOTO_POR_DEFECTO)
        self.origen = "por defecto"
        guardada = self._leer_cache()
        if guardada:
            self.valores.update(guardada)
            self.origen = "guardada"

    # Valor de una clave, ej. remoto.get("episodio_pda").
    def get(self, clave):
        return self.valores.get(clave, config.REMOTO_POR_DEFECTO.get(clave))

    # PIDE LA CONFIGURACIÓN A GITHUB. No bloquea la app: cuando llega la respuesta
    # (o falla) se llama a al_terminar(cambio), donde cambio=True si llegó algo nuevo.
    def descargar(self, al_terminar):
        def ok(req, datos):
            if isinstance(datos, (str, bytes)):  # GitHub raw responde text/plain
                try:
                    datos = json.loads(datos)
                except ValueError:
                    datos = None
            limpio = validar(datos)
            if not limpio:
                return fallo(req, None)
            self.valores.update(limpio)
            self.origen = "remota"
            self._guardar_cache(limpio)
            al_terminar(True)

        def fallo(req, error):
            al_terminar(False)  # sin internet: se quedan los valores guardados o por defecto

        # «?t=» evita que GitHub entregue una copia vieja guardada en su caché.
        UrlRequest("%s?t=%d" % (config.REMOTO_URL, time.time()),
                   on_success=ok, on_failure=fallo, on_error=fallo,
                   timeout=config.REMOTO_ESPERA,
                   req_headers={"User-Agent": config.USER_AGENT})

    def _leer_cache(self):
        try:
            with open(self.cache, "r", encoding="utf-8") as f:
                return validar(json.load(f))
        except (OSError, ValueError):
            return {}

    def _guardar_cache(self, datos):
        try:
            with open(self.cache, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)
        except OSError:
            pass
