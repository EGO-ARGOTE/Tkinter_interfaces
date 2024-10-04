import tkinter as tk
from tkinter import ttk

def convertir_temp():
  temp_celsius = float(caja_temp_celsius.get())
  temp_kelvin = temp_celsius + 273.15
  temp_farenheit = temp_celsius * 1.8 + 32
  etiqueta_temp_kelvin.config(text=f"Temperatura en °K: {temp_kelvin}")
  etiqueta_temp_farenheit.config(text=f"Temperatura en °F: {temp_farenheit}")
  
ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.configure(bg="lightblue")
ventana.config(width=400, height=300)

# Estilos para los botones
style = ttk.Style()
style.configure("TButton", background="lightblue", foreground="black")

# Crear el boton usando el estilo personalizado
boton_convertir = ttk.Button(text="Convertir", style="TButton", command=convertir_temp)

etiqueta_temp_celsius = ttk.Label(text="Temperatura en °C:")
etiqueta_temp_celsius.place(x=20, y=20)

caja_temp_celsius = ttk.Entry()
caja_temp_celsius.place(x=140, y=20, width=60)

boton_convertir = ttk.Button(text="Convertir", command=convertir_temp)
boton_convertir.place(x=20, y=60)

etiqueta_temp_kelvin = ttk.Label(text="Temperatura en °K: n/a")
etiqueta_temp_kelvin.place(x=20, y=120)

etiqueta_temp_farenheit = ttk.Label(text="Temperatura en °F: n/a")
etiqueta_temp_farenheit.place(x=20, y=160)

ventana.mainloop()