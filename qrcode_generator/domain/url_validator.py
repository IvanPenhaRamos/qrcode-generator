import re
from urllib.parse import urlparse

def sanitize_filename(name:str) -> str:
    '''
    Reemplaza caracteres no válidos para un filename
    return:
    - Devuelve el nombre apto para archivos
    - En caso de una cadena vacía o algún error, devuelve un genérico
    '''
    name = name.strip()
    name = re.sub(r"[^a-zA-Z0-9._-]", "_", name)
    return name or "qrcode"


def URL_validator(url: str) -> tuple[str, str]:
    """
    Valida y normaliza una URL.
    - Añade https:// si no hay esquema
    - Comprueba que tenga esquema válido y dominio
    - Lanza ValueError si la URL no es válida
    
    return:
    - url normalizada
    - propuesta de nombre para el archivo a descargar
    """

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
    
    recommended_name = sanitize_filename(parsed.netloc)

    return url, recommended_name