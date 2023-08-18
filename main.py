import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import os
import ocr
import sys
import subprocess


output_path = ""  # Variable global para guardar la ruta del archivo de salida

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_path_label.config(text=file_path)

def perform_ocr():
    global output_path
    pdf_path = pdf_path_label.cget("text")
    output_path = ocr.convert_pdf_to_text(pdf_path)
    output_label.config(text=f"Texto extraído y guardado en {output_path}")
    messagebox.showinfo("OCR Pro", "El escaneo OCR está listo.")
    open_result_button.config(state=tk.NORMAL)  # Habilitar el botón para abrir el resultado

def open_result():
    global output_path     
    if sys.platform.startswith('darwin'):        
         subprocess.run(['open', output_path])     
    elif sys.platform.startswith('linux'):         
         subprocess.run(['xdg-open', output_path])    
    elif sys.platform.startswith('win32'):        
         subprocess.run(['start', output_path], shell=True)

def open_policies():
    webbrowser.open("https://ruta/a/politicas_de_uso.pdf")  # Enlace a las políticas de uso

root = tk.Tk()
root.title("OCR Pro")

# Icono de la Aplicación
root.iconbitmap('icono.ico')  # Ajusta la ruta según sea necesario

# Logo (Redimensionado)
logo = tk.PhotoImage(file="logo.png")  # Ajusta la ruta según sea necesario
logo = logo.subsample(4, 4)  # Redimensionar; ajusta los valores según sea necesario
logo_label = tk.Label(root, image=logo)
logo_label.pack()

# Descripción
description_text = (
    "OCR Pro es una solución de reconocimiento óptico de caracteres\n"
    "diseñada para situaciones donde el OCR de Word falla. Convierte documentos\n"
    "escaneados y archivos PDF en texto editable con precisión."
)
description_label = tk.Label(root, text=description_text, justify="left")
description_label.pack()

# Seleccionar PDF
select_button = tk.Button(root, text="Seleccionar PDF", command=select_pdf)
select_button.pack()
pdf_path_label = tk.Label(root, text="")
pdf_path_label.pack()

# Realizar OCR
convert_button = tk.Button(root, text="Realizar OCR", command=perform_ocr)
convert_button.pack()
output_label = tk.Label(root, text="")
output_label.pack()

# Botón para abrir el resultado
open_result_button = tk.Button(root, text="Abrir Resultado", command=open_result, state=tk.DISABLED)
open_result_button.pack()

# Políticas de Uso
policies_label = tk.Label(root, text="Políticas de Uso", fg="blue", cursor="hand2")
policies_label.pack()
policies_label.bind("<Button-1>", lambda e: open_policies())

root.mainloop()
