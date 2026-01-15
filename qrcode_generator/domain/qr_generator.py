import qrcode # type: ignore
from pathlib import Path
from io import BytesIO
import base64

# General el QR para la app de escritorio
def generate_qr(url: str, file_path: Path) -> None:

    if not isinstance(file_path, Path):
        raise TypeError("file_path debe ser un objeto Path")
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(file_path)

# Genera el QR a descargar
def generate_qr_bytes(url: str) -> BytesIO:
    qr = qrcode.make(url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer

# Genera un string para mostrar el código en el HTML
def generate_qr_base64(data: str) -> str:
    qr = qrcode.make(data)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    encoded = base64.b64encode(buffer.read()).decode("utf-8")
    return encoded
