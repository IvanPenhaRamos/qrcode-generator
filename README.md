# QR Code Generator

## 1. Descripción

Aplicación desarrollada en Python con la finalidad de generar códigos QR a partir de URLs. Disponible en **versión escritorio** con soporte multiplataforma (Linux, Windows y macOS) y **versión web**.

Este proyecto nace de dos necesidades concretas:

**1. Una necesidad práctica**
Muchos generadores de códigos QR disponibles en la web generan enlaces que **caducan** o dependen de servicios externos. Esta aplicación genera códigos QR **locales y permanentes**, libre y sin intermediarios.

**2. Una necesidad de aprendizaje y refuerzo**
El proyecto sirve como ejercicio práctico para refrescar y mejorar habilidades en Python, aplicando buenas prácticas de desarrollo y estructura de proyectos reales.

Durante el desarrollo se han trabajado y reforzado los siguientes conceptos:

- Sustituir `print()` en consola por manejo de errores con excepciones y comunicación mediante la GUI

- Pasar de archivos `.py` sueltos a una estructura de proyecto organizada

- Sustituir rutas basadas en `strings` por el uso del módulo `pathlib.Path`

- Uso de **Tkinter** para crear una interfaz gráfica sencilla y una iniciación en **HTML** y **CSS**

- Separación clara entre interfaz gráfica y lógica

- Mejora del sistema de **importaciones** y ejecución mediante **entrypoints**

## 2. Arquitectura

- **Domain**: lógica de validación y generación de QR (compartida)

- **Desktop**: interfaz gráfica con Tkinter

- **Web**: aplicación Flask con HTML y CSS

- **Tests**: validación automática del dominio

## 3. Versión de escritorio

Genera los códigos y permite al usuario elegir dónde guardarlos.

```bash
python -m qrcode_generator.desktop.gui
```
## 4. Versión web (Flask)

Interfaz web sencilla para validar una URL, mostrar una previsualización del QR y descargarlo.

```bash
flask --app qrcode_generator.web.app run
```

## 5. Test

```bash
pytest
```
## 6. 🐳 Docker (opcional)

El proyecto incluye los archivos necesarios para ejecutarse en Docker (Dockerfile y docker-compose.yml).

## 7. Requisitos

- Python ≥ 3.10
- pip
- Uso de un entorno virtual (recomendado)

## Notas finales

Este proyecto tiene un enfoque educativo y práctico, priorizando la claridad del código, la separación de responsabilidades y el uso de estándares modernos en Python.