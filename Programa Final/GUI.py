import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica
from tkinter import *  # Importa todo desde tkinter
from tkinter import ttk  # Importa ttk para usar estilos y widgets temáticos
from ttkthemes import ThemedTk  # Importa ThemedTk para usar temas en la interfaz gráfica
from PIL import ImageTk, Image  # Importa ImageTk e Image desde PIL para trabajar con imágenes
import PIL.Image  # Importa la clase Image desde PIL
from Fuctions import *  # Importa todo desde un módulo llamado Fuctions (asegúrate de tener este módulo)

#####################################################################################
# Función para crear la interfaz
#####################################################################################

def Crear_Interfaz():
    # Crea la ventana principal con un tema específico
    window = ThemedTk(theme="arc")
    window.geometry("1000x900") # Establece el tamaño de la ventana
    window.maxsize(1000, 900)  # Establece el tamaño máximo de la ventana
    window.minsize(1000, 900)  # Establece el tamaño mínimo de la ventana

    # Establece un estilo para los botones
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12), background='#4CAF50', foreground='black', padding=10)
    style.map('TButton', background=[('active', '#45a049')])

    # Etiqueta del título de la ventana
    Titulo = tk.Label(window, text="UNIDAD DE PROCESAMIENTO DE IMÁGENES", font=('Helvetica', 25, 'bold'), fg='#333')
    Titulo.pack(pady=10)  # Coloca el título en la ventana

    # Carga y muestra una imagen
    fp = open("WhiteScreen.jpg", "rb")  # Abre la imagen en modo binario
    image = PIL.Image.open(fp)  # Carga la imagen usando PIL
    new_size = (800, 500)  # Especifica el tamaño deseado (ancho, alto)
    resized_image = image.resize(new_size)  # Redimensiona la imagen
    photo = ImageTk.PhotoImage(resized_image)  # Convierte la imagen redimensionada a un formato que Tkinter pueda usar
    image_label = tk.Label(window, image=photo, borderwidth=2, relief="solid")  # Crea una etiqueta para mostrar la imagen con un borde
    image_label.place(x=100, y=70)  # Coloca la etiqueta de la imagen en la ventana

    boton_ancho_op1 = 20
    boton_ancho = 22


    # Botón para hacer un screenshot
    Boton_HacerScreen = ttk.Button(window, text="Realizar una captura", command=lambda: TakeScreenshot(window, image_label), width=boton_ancho_op1)
    Boton_HacerScreen.place(x=120, y=580)  # Coloca el botón en la ventana

    # Botón para procesar la imagen
    Boton_Procesar = ttk.Button(window, text="Procesar Imagen", command=lambda: MandarCaptura(Label_Joint1_Value, Label_Joint2_Value, Label_Joint2_1_Value, Label_Joint3_Value), width=boton_ancho_op1)
    Boton_Procesar.place(x=372, y=580)  # Coloca el botón en la ventana

    # Botón proceso completo
    Boton_Proceso_Completo = ttk.Button(window, text="Proceso completo", command=lambda: proceso_completo(window, image_label, Label_Joint1_Value, Label_Joint2_Value, Label_Joint2_1_Value, Label_Joint3_Value), width=boton_ancho_op1)
    Boton_Proceso_Completo.place(x=625, y=580)  # Coloca el botón en la ventana

    # Etiqueta para la sección de ángulos de configuración
    Label_AngulosConf = tk.Label(window, text="Ángulos de Configuración", font=('Helvetica', 22, 'bold'), fg='#333')
    Label_AngulosConf.place(x=30, y=640)  # Coloca la etiqueta en la ventana

    # Etiquetas para cada articulación (joint)
    Label_Joint1 = tk.Label(window, text="Joint 1 = ", font=('Helvetica', 20), fg='#333')
    Label_Joint1.place(x=30, y=690)  # Coloca la etiqueta en la ventana

    Label_Joint2 = tk.Label(window, text="Joint 2 = ", font=('Helvetica', 20), fg='#333')
    Label_Joint2.place(x=30, y=740)  # Coloca la etiqueta en la ventana

    Label_Joint3 = tk.Label(window, text="Joint 3 = ", font=('Helvetica', 20), fg='#333')
    Label_Joint3.place(x=30, y=790)  # Coloca la etiqueta en la ventana

    # Etiquetas para mostrar los valores de cada articulación (joint)
    Label_Joint1_Value = tk.Label(window, text="", font=('Helvetica', 20), fg='#333')
    Label_Joint1_Value.place(x=160, y=690)  # Coloca la etiqueta en la ventana

    Label_Joint2_Value = tk.Label(window, text="", font=('Helvetica', 20), fg='#333')
    Label_Joint2_Value.place(x=160, y=740)  # Coloca la etiqueta en la ventana

    Label_Joint2_1_Value = tk.Label(window, text="", font=('Helvetica', 20), fg='#333')
    Label_Joint2_1_Value.place(x=280, y=740)  # Coloca la etiqueta en la ventana

    Label_Joint3_Value = tk.Label(window, text="", font=('Helvetica', 20), fg='#333')
    Label_Joint3_Value.place(x=160, y=790)  # Coloca la etiqueta en la ventana

    # Botón para mandar comandos al robot
    Boton_MandarRobot = ttk.Button(window, text="Envío de comandos al robot", command=Mandar_Robot, width=boton_ancho)
    Boton_MandarRobot.place(x=600, y=770)  # Coloca el botón en la ventana

    # Botón para mandar el robot a su posición inicial
    Boton_RobotHome = ttk.Button(window, text="Posición inicial del robot", command=RobotHome, width=boton_ancho)
    Boton_RobotHome.place(x=600, y=670) # Coloca el botón en la ventana

    # Botón para ver la simulación en MATLAB
    Boton_simulacion = ttk.Button(window, text="Ver simulación", command=simulation, width=boton_ancho)
    Boton_simulacion.place(x=600, y=720) # Coloca el botón en la ventana
    
    
    # Botón para salir de la aplicación
    Boton_Salir = ttk.Button(window, text="Salir", command=window.quit, width=boton_ancho)
    Boton_Salir.place(x=600, y=820)  # Coloca el botón en la ventana5

    # Ejecuta el bucle principal de la interfaz gráfica
    window.mainloop()

# Llama a la función para crear la interfaz
Crear_Interfaz()
