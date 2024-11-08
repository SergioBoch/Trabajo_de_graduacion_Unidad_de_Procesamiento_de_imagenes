import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
import PIL.Image
from pymycobot.mycobot import MyCobot
from Fuctions import *

# Función para enviar ángulos al robot
def send_angles(joint1, joint2, joint3):
    try:
        angles = [float(joint1.get()), float(joint2.get()), float(joint3.get()), 0, 0, 0]
        mc = MyCobot('COM14', 115200)
        mc.send_angles(angles, 50)
        mc.close()
        tk.messagebox.showinfo("Éxito", "Comandos enviados al robot con éxito")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error al enviar comandos al robot: {str(e)}")

# Función para crear la interfaz gráfica
def Crear_Interfaz():
    window = ThemedTk(theme="breeze")
    window.geometry("1000x500")
    window.maxsize(1000, 500)
    window.minsize(1000, 500)
    window.title("Ángulo Configuración")

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=10)
    style.configure("TLabel", font=("Helvetica", 16))
    style.configure("TCombobox", font=("Helvetica", 14))

    # Título principal
    Titulo = ttk.Label(window, text="Ángulo Configuración", font=('Helvetica', 30, 'bold'))
    Titulo.pack(pady=20)

    # Sección de puertos
    port_frame = ttk.Frame(window)
    port_frame.pack(pady=10)

    Boton_Buscar_Puertos = ttk.Button(port_frame, text="Buscar Puertos", command=lambda: Search_COMPorts(Combo_ports))
    Boton_Buscar_Puertos.grid(row=0, column=0, padx=10)

    Combo_ports = ttk.Combobox(port_frame, width=15, font=("Helvetica", 14))
    Combo_ports.grid(row=0, column=1, padx=10)

    # Imagen
    image_frame = ttk.Frame(window)
    image_frame.pack(pady=20)

    fp = open("WhiteScreen.jpg", "rb")
    image = PIL.Image.open(fp)
    new_size = (300, 200)
    resized_image = image.resize(new_size)
    photo = ImageTk.PhotoImage(resized_image)
    image_label = ttk.Label(image_frame, image=photo)
    image_label.grid(row=0, column=0, columnspan=2)

    # Botones para la imagen
    image_buttons_frame = ttk.Frame(window)
    image_buttons_frame.pack(pady=10)

    Boton_HacerScreen = ttk.Button(image_buttons_frame, text="Hacer Screen", command=lambda: TakeScreenshot(window, image_label))
    Boton_HacerScreen.grid(row=0, column=0, padx=10)

    Boton_Procesar = ttk.Button(image_buttons_frame, text="Procesar Imagen", command=lambda: MandarCaptura(Label_Joint1_Value, Label_Joint2_Value, Label_Joint2_1_Value, Label_Joint3_Value))
    Boton_Procesar.grid(row=0, column=1, padx=10)

    # Sección de ángulos de configuración
    angles_frame = ttk.LabelFrame(window, text="Ángulos de Configuración", padding=20)
    angles_frame.pack(pady=20)

    Label_Joint1 = ttk.Label(angles_frame, text="Joint 1= ")
    Label_Joint1.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    Label_Joint1_Value = ttk.Entry(angles_frame, font=('Helvetica', 16), width=10)
    Label_Joint1_Value.grid(row=0, column=1, padx=10, pady=10)

    Label_Joint2 = ttk.Label(angles_frame, text="Joint 2= ")
    Label_Joint2.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Label_Joint2_Value = ttk.Entry(angles_frame, font=('Helvetica', 16), width=10)
    Label_Joint2_Value.grid(row=1, column=1, padx=10, pady=10)

    Label_Joint3 = ttk.Label(angles_frame, text="Joint 3= ")
    Label_Joint3.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Label_Joint3_Value = ttk.Entry(angles_frame, font=('Helvetica', 16), width=10)
    Label_Joint3_Value.grid(row=2, column=1, padx=10, pady=10)

    # Botones para el robot
    robot_buttons_frame = ttk.Frame(window)
    robot_buttons_frame.pack(pady=20)

    Boton_ConectarRobot = ttk.Button(robot_buttons_frame, text="Conectar Robot", command=lambda: Conectar_COM(Combo_ports.get()))
    Boton_ConectarRobot.grid(row=0, column=0, padx=10)

    Boton_MandarRobot = ttk.Button(robot_buttons_frame, text="Mandar a Robot", command=lambda: send_angles(Label_Joint1_Value, Label_Joint2_Value, Label_Joint3_Value))
    Boton_MandarRobot.grid(row=0, column=1, padx=10)

    Boton_Salir = ttk.Button(robot_buttons_frame, text="Salir", command=window.quit)
    Boton_Salir.grid(row=0, column=2, padx=10)

    window.mainloop()

# Llama a la función para crear la interfaz
Crear_Interfaz()
