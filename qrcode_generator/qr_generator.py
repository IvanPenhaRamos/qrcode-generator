import qrcode # type: ignore
from pathlib import Path

def generate_qr(url: str, file_path: Path) -> None:

    if not isinstance(file_path, Path):
        raise TypeError("file_path debe ser un objeto Path")
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(file_path)