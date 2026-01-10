import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path
from urllib.parse import urlparse

from platformdirs import user_pictures_dir

from qrcode_generator.url_validator import URLvalidator
from qrcode_generator.qr_generator import generate_qr


# Este módulo ha sido creado con vibe coding con el próposito de repasar lo aprendido sobre Tkinter

def run_gui():
    # Instancia el root
    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("400x200")
    root.resizable(False, False)

    # Instancia el frame
    main_frame = ttk.Frame(master=root, padding=20)
    main_frame.pack(fill="both", expand=True)

    # Etiqueta para el cuadro del input
    ttk.Label(main_frame, text="Introduce la URL:").pack(anchor="w")

    # Cuadro de texto para escribir el input/entry
    url_entry = ttk.Entry(main_frame, width=40)
    url_entry.pack(fill="x", pady=5)

    # Esta función se crea dentro de la función principal para dar funcionalidad al botón que vamos a crear
    def on_generate():
        # El get() la variable url_entry
        raw_url = url_entry.get().strip()

        try:
            validated_url = URLvalidator(raw_url)
        except ValueError as e:
            messagebox.showerror("URL inválida", str(e))
            return

        # Construye el nombre del archivo en base al dominio de la URL
        domain = urlparse(validated_url).netloc.replace(":","_")
        default_name = f"qrcode_{domain}.png"

        # Selección de la ruta
        file_path = filedialog.asksaveasfilename(
            title="Guardar código QR",
            initialdir=user_pictures_dir(),
            initialfile=default_name,
            defaultextension=".png",
            filetypes=[("PNG Image", "*,png")]
        )

        if not file_path:
            return # User habrá cancelado
        
        try:
            generate_qr(validated_url, Path(file_path))
        except Exception as e:
            messagebox.showerror("Error",
                                f"No se pudo generar el código QR:\n{e}"                                 )

        messagebox.showinfo("QR generado",
                            f"QR generado:\n{file_path}")

    # Botón para ejecutar
    ttk.Button(
        main_frame,
        text="Generar QR",
        command=on_generate
    ).pack(pady=20) # expand=True si queda un hueco extraño

    root.mainloop()

    

run_gui()
