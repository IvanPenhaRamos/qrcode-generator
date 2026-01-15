FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY qrcode_generator ./qrcode_generator

RUN pip install --no-chache-dir .

EXPOSE 5000

CMD ["flask", "--app", "qrcode_generator.web.app", "run", "--host=0.0.0.0"]