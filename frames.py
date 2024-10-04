import tkinter as tk # Importa la biblioteca tkinter y la renombra como tk para facilitar su uso.

ventana = tk.Tk() # Crea una ventana principal de la aplicación.
ventana.title("Mi ventana") # Establece el título de la ventana como "Mi ventana".
ventana.geometry("600x400") # Define el tanaño de la ventana a 600 píxeles de ancho y 400 píxeles de alto.
ventana.configure(bg="lightblue") # Canbia el color de fondo de la ventana a azul claro.

labelframe = tk.LabelFrame(ventana, text="Grupo de Widget", bg="yellow", padx=10, pady=10)
labelframe.configure(width=300, height=200)
labelframe.pack()

ventana.mainloop() # Inicia el bucle principal que mantiene la ventana abierta y responde a eventos.

# frane1 = tk.Frame(ventana) # Crea un marco (frane) dentro de la ventana principal.
# frane1.configure(width=300, height=200, bg="red", bd=5) # Establece el taraño, color de fondo y borde del marco.
# frane1.pack() # Coloca el marco en la ventana principal, utilizando el método pack para organizarlo.

# frane2 = tk.Frame(frane1)
# frane2.configure(width=100, height=100, bg="blue", bd=5)

# boton =tk.Button(frane1, text="EGO")
# boton.pack()
# frane2.pack()
