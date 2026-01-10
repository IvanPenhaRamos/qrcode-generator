from urllib.parse import urlparse

"""
Valida y normaliza una URL.
- Añade https:// si no hay esquema
- Comprueba que tenga esquema válido y dominio
- Lanza ValueError si la URL no es válida
"""

def URLvalidator(url: str) -> str:

    if not url or " " in url:
        raise ValueError("La URL está vacía o contiene espacios")

    parsed = urlparse(url)

    # Si no hay esquema, se asume https
    if not parsed.scheme:
        url = "https://" + url
        parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("El esquema de la URL debe ser http o https")

    if not parsed.netloc or not "." in parsed.netloc:
        raise ValueError("La URL no contiene un dominio válido")

    return url