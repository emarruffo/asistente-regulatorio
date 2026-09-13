"""Utilidades de normalización de texto para el asistente regulatorio."""

import re

_SALTOS_MULTIPLES = re.compile(r"\n{2,}")
_ESPACIOS_MULTIPLES = re.compile(r"[ \t]+")


def limpiar_texto(texto: str) -> str:
    """Normaliza texto crudo extraído de un PDF.

    Colapsa saltos de línea dobles en uno solo y secuencias de espacios
    o tabulaciones en un único espacio.

    Args:
        texto: Texto tal como sale del extractor de PDF.

    Returns:
        El texto normalizado, sin espacios al inicio ni al final.
        Cadena vacía si la entrada es vacía.
    """
    if not texto:
        return ""
    sin_saltos = _SALTOS_MULTIPLES.sub("\n", texto)
    sin_espacios = _ESPACIOS_MULTIPLES.sub(" ", sin_saltos)
    return sin_espacios.strip()