from flask import Flask, render_template, request, send_file

from qrcode_generator.domain.url_validator import URL_validator
from qrcode_generator.domain.qr_generator import generate_qr_bytes, generate_qr_base64

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    validated_url = ""
    qr_preview = ""
    error = None

    if request.method == "POST":
        url_input = request.form.get("url", "").strip()

        try:
            validated_url, _ = URL_validator(url_input) # Para validar la URL y hacer preview no necesitamos nombre de archivo
            qr_preview = generate_qr_base64(validated_url)
        except ValueError as e:
            error = str(e)

    return render_template(
        "index.html",
        validated_url=validated_url,
        qr_preview=qr_preview,
        error=error
    )


@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url", "").strip()

    try:
        validated_url, filename = URL_validator(url)
    except ValueError as e:
        return str(e), 400

    buffer = generate_qr_bytes(validated_url)


    return send_file(
        buffer,
        mimetype="image/png",
        as_attachment=True,
        download_name=filename
    )
