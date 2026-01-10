# QR Code Generator

## 1. Descripción

Aplicación de escritorio desarrollada en Python para generar códigos QR a partir de URLs, con interfaz gráfica y soporte multiplataforma (Linux, Windows y macOS).

Este proyecto nace de dos necesidades concretas:

**1. Una necesidad práctica**
Muchos generadores de códigos QR disponibles en la web generan enlaces que **caducan** o dependen de servicios externos. Esta aplicación genera códigos QR **locales y permanentes**, libre y sin intermediarios.

**2. Una necesidad de aprendizaje y refuerzo**
El proyecto sirve como ejercicio práctico para refrescar y mejorar habilidades en Python, aplicando buenas prácticas de desarrollo y estructura de proyectos reales.

Durante el desarrollo se han trabajado y reforzado los siguientes conceptos:

- Sustituir `print()` en consola por manejo de errores con excepciones y comunicación mediante la GUI

- Pasar de archivos `.py` sueltos a una estructura de proyecto organizada

- Sustituir rutas basadas en `strings` por el uso del módulo `pathlib.Path`

- Uso de **Tkinter** para crear una interfaz gráfica sencilla

- Separación clara entre interfaz gráfica y lógica

- Mejora del sistema de **importaciones** y ejecución mediante **entrypoints**

## 2. Requisitos

- Python ≥ 3.10
- pip
- Uso de un entorno virtual (recomendado)

## 3. Instalación

Clona el repositorio y ejecuta los siguientes comandos desde la raíz del proyecto:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
pip install -e .
```

## 4. Ejecución

Una vez instalado el proyecto, la aplicación puede ejecutarse mediante el comando:

```bash
qrcode-generator
```

Esto abrirá la interfaz gráfica del generador de códigos QR.

## Notas finales

Este proyecto tiene un enfoque educativo y práctico, priorizando la claridad del código, la separación de responsabilidades y el uso de estándares modernos en Python.