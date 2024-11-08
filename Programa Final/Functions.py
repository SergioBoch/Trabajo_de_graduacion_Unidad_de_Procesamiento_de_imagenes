import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from ttkthemes import ThemedTk
import pyautogui
from PIL import ImageTk, Image
import PIL.Image
import time
import serial.tools.list_ports
import cv2
import numpy as np
import pytesseract
from pymycobot.mycobot import MyCobot
import serial
import struct
from PIL import ImageOps
import PIL.ImageOps
import pandas as pd
from tkinter import messagebox as MessageBox
import matlab.engine
import roboticstoolbox as rtb
from spatialmath import SE3
import matplotlib.pyplot as plt
import math

#####################################################################################
# Inicialización de variables
#####################################################################################
Captura = ""
JA1 = ""
JB1 = ""
JB2 = ""
JC1 = ""
COM_PORT = ""
imagencapturada = 0

#####################################################################################
# Función para esconder ventana
#####################################################################################
def HideWindow(window):
    window.withdraw()

#####################################################################################
# Función para reaparecer ventana
#####################################################################################

def ShowWindow(window):
    window.deiconify()

#####################################################################################
# Función para capturar la pantalla
#####################################################################################

def TakeScreenshot(window, image_label):
    x0 = 572 # Punto inicial para la coordenada X
    y0 = 190 # Punto incial para la coordenada Y
    ancho = x0 + 775 # Ancho total para la ventana (X)
    alto = y0 + 604 # Alto total para el largo (Y)

    global Captura
    global imagencapturada

    HideWindow(window)
    time.sleep(0.5)
    myscreen = pyautogui.screenshot()
    image = myscreen.crop((x0, y0, ancho, alto)) # Captura de pantalla
    
    # Convertir la imagen a escala de grises
    gray_image = PIL.ImageOps.grayscale(image)
    
    # Convertir la imagen a binaria usando umbralización
    bw_image = gray_image.point(lambda x: 0 if x < 128 else 255, '1')
    
    bw_image.save('myscreen_bw.png') # Guardar la pantalla capturada
    imagencapturada = bw_image
    time.sleep(0.5)
    ShowWindow(window)

    fp = open("myscreen_bw.png", "rb")
    image = PIL.Image.open(fp)

    Captura = "myscreen_bw.png"
    new_size = (800, 500)  # Especifica las dimensiones deseadas (ancho, alto)
    resized_image = image.resize(new_size)
    photo = ImageTk.PhotoImage(resized_image)
    image_label.configure(image=photo)
    image_label.image = photo

#####################################################################################
# Función para búsqueda de robots conectados
#####################################################################################

def find_mycobot_ports(description="USB-Enhanced-SERIAL CH9102"):
    ports = serial.tools.list_ports.comports()
    mycobot_ports = [port.device for port in ports if description in port.description]
    return mycobot_ports

#####################################################################################
# Función para advertencia de múltiples robots conectados
#####################################################################################

def select_mycobot(ports):
    root = tk.Tk()
    root.withdraw()
    
    selected_port = simpledialog.askstring(
        "Selección de myCobot", 
        "Se detectaron múltiples sistemas myCobot: \n" + 
        "\n".join(f"{i + 1}: {port}" for i, port in enumerate(ports)) + 
        "\n\nIngrese el número de myCobot al que desea enviar los datos:"
    )
    
    root.destroy()
    if selected_port is not None:
        try:
            selection = int(selected_port) - 1
            if 0 <= selection < len(ports):
                return ports[selection]
        except ValueError:
            pass
    return None 

#####################################################################################
# Función para advertencia de conexión con el robot
#####################################################################################

def connect_and_send_angles(port, baudrate=115200):
    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=1)
        time.sleep(2)
        ser.close()
        return port
    except serial.SerialException as e:
        print(f"Error al conectar al puerto {port}: {e}")
        return None

#####################################################################################
# Función para mandar datos al robot
#####################################################################################

def Mandar_Robot():

    global JB2_angular

    global COM_PORT

    port_description = "USB-Enhanced-SERIAL CH9102" # Descripción sobre puerto para buscar automáticamente
    ports = find_mycobot_ports(port_description)
    
    # Condición en caso de que se tengan dos puertos iguales, se pide seleccionar alguno
    if len(ports) == 1:
        port = ports[0]
    elif len(ports) > 1:
        port = select_mycobot(ports)
        if not port:
            MessageBox.showwarning("Selección inválida", "No se seleccionó un puerto válido.")
            return
    else:
        MessageBox.showwarning("Error", f"No se encontró ningún puerto con la descripción '{port_description}'.")
        return
    
    # Condición en caso de que no se pueda establecer conexión con el sistema robótico
    COM_PORT = connect_and_send_angles(port)
    if not COM_PORT:
        MessageBox.showwarning("Error", "No se pudo establecer la conexión con el puerto seleccionado.")
        return
    
    # Condición para envío de datos
    Cadena_datos = ""
    if (JA1 and JB1 and JB2 and JC1):
        try:
            LINEAR_TO_ANGULAR_RATIO = 1
            JB2_angular = JB2 * LINEAR_TO_ANGULAR_RATIO

            mc = MyCobot(COM_PORT, 115200)
            # Formato de envío de datos para el myCobot 280 M5
            mc.send_angles([float(JA1), 0, float(JB1), float(JB2_angular), float(JC1), 0], 90)
            
            Recibido = COM_PORT.readline().decode()
            TempA = (Recibido[Recibido.index("JA")+2:Recibido.index("JB")])
            TempB = (Recibido[Recibido.index("JB")+2:Recibido.index(",")])
            TempC = (Recibido[Recibido.index(",")+1:Recibido.index("JC")])
            TempD = (Recibido[Recibido.index("JC")+2:Recibido.index(";")])
            # Cierra la conexión
            mc.close()
            
            # Condición para la verificación de envío de datos
            if ((float(TempA) == float(JA1))and(float(TempB) == float(JB1))and(float(TempC) == float(JB2))and(float(TempD) == float(JC1))):
                print("Transmisión Exitosa")
                print("JA" + JA1 + "JB" + JB1 + "," + JB2 + "JC" + JC1 + ";")
            else:
                MessageBox.showwarning("Alerta", "Error en la transmisión de datos")

        except Exception as error:
            print(error)    
    # Advertencia en dado caso falte algún dato para el envío al robot
    else:
        MessageBox.showwarning("Alerta", "No se tienen los datos completos")

#####################################################################################
# Función para mandar el robot a su posición inicial
#####################################################################################

# El formato de validación y errores es igual a la sección anterior, simpelmente en este caso
# como se busca mandar el myCobot 280 M5 a su posición inicial, los valores que van en la 
# cadena de envío es un vector de ceros. 

def RobotHome():
    port_description = "USB-Enhanced-SERIAL CH9102"
    ports = find_mycobot_ports(port_description)

    if len(ports) == 1:
        port = ports[0]
    elif len(ports) > 1:
        port = select_mycobot(ports)
        if not port:
            MessageBox.showwarning("Selección inválida", "No se seleccionó un puerto válido.")
            return
    else: 
        MessageBox.showwarning("Error", f"No se encontró ningún puerto con la descripción '{port_description}'.")
        return

    selected_port = connect_and_send_angles(port)
    if not selected_port:
        MessageBox.showwarning("Error", f"Error al enviar los ángulos al puerto '{port}'.")
        return

    try:
        mc = MyCobot(selected_port, 115200)
        mc.send_angles([0, 0, 0, 0, 0, 0], 90) # Vector de ceros a enviar
        mc.close()
    except Exception as e:
        MessageBox.showwarning("Error", f"Error al enviar ángulos al MyCobot: {e}")

#####################################################################################
# Función para validación de captura de pantalla
#####################################################################################

def MandarCaptura(Label_Joint1_Value, Label_Joint2_Value, Label_Joint2_1_Value, Label_Joint3_Value):
    global JA1
    global JB1
    global JB2
    global JC1
    global Captura

    imagencapture = cv2.imread(Captura)

    # Primer recorte para reconocer el joint 
    AjuRecorJoint = [25, 35, 25+55, 35+302] # x, y, ancho, alto
    Recorte_Joint = imagencapture[AjuRecorJoint[0]:AjuRecorJoint[2], AjuRecorJoint[1]:AjuRecorJoint[3]]
    cv2.imwrite("Joint Recibido.jpg", Recorte_Joint)

    # Reconocer el Joint (La línea de abajo solo es en Windows)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    Texto_joint = pytesseract.image_to_string(Recorte_Joint, config='--psm 6')

    # Condiciones según la junta reconocida
    if 'Joint 1' in Texto_joint:
        AjuRecorAng = [263, 540, 263+35, 540+89] # x, y, ancho, alto
        Recorte_Ang = imagencapture[AjuRecorAng[0]:AjuRecorAng[2], AjuRecorAng[1]:AjuRecorAng[3]]
        Texto = Process_number(Recorte_Ang)
        cv2.imwrite('AnguloJoint1.jpg', Recorte_Ang)
        JA1 = str(Texto)
        Label_Joint1_Value['text'] = (JA1 + "°")

    elif 'Joint 2' in Texto_joint:
        AjuRecorAng = [140, 550, 140+35, 550+85] # x, y, ancho, alto
        Recorte_Ang = imagencapture[AjuRecorAng[0]:AjuRecorAng[2], AjuRecorAng[1]:AjuRecorAng[3]]
        Texto1 = Process_number(Recorte_Ang)
        cv2.imwrite('AnguloJoint2.jpg', Recorte_Ang)
        JB1 = str(Texto1)
        Label_Joint2_Value['text'] = (JB1 + "°")

        AjuRecorAng = [265, 550, 265+35, 550+85] # x, y, ancho, alto
        Recorte_Ang = imagencapture[AjuRecorAng[0]:AjuRecorAng[2], AjuRecorAng[1]:AjuRecorAng[3]]
        Texto2 = Process_number(Recorte_Ang)
        cv2.imwrite('DesplazamientoJoint2.jpg', Recorte_Ang)
        JB2 = str(Texto2)
        Label_Joint2_1_Value['text'] = (JB2 + "mm")

    elif 'Joint 3' in Texto_joint:
        AjuRecorAng = [265, 540, 265+35, 540+90] # x, y, ancho, alto
        Recorte_Ang = imagencapture[AjuRecorAng[0]:AjuRecorAng[2], AjuRecorAng[1]:AjuRecorAng[3]]
        cv2.imwrite("AnguloJoint3.jpg", Recorte_Ang)
        Texto = Process_number(Recorte_Ang)
        JC1 = str(Texto)
        Label_Joint3_Value['text'] = (JC1 + "°")
    
    else:
        MessageBox.showwarning("Alerta", "No se detecto ninguna junta. Reubique la imagen y capture la pantalla nuevamente.")

#####################################################################################
# Función para dibujar un eslabón de un robot para la simulación
#####################################################################################

def dibujar_eslabon(start, end, color, ax):
    """Dibuja un eslabón del robot desde el punto start al punto end con un color específico."""
    ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], color=color, linewidth=5)

#####################################################################################
# Función para ejectura la simulación 
#####################################################################################

def simulation():
    # Dimensiones del robot (en mm)
    d1 = 131.22; a1 = 0; alpha1 = np.pi/2; offset1 = 0
    d2 = 0; a2 = -110.4; alpha2 = 0; offset2 = -np.pi/2
    d3 = 0; a3 = -96; alpha3 = 0; offset3 = 0
    d4 = 63.4; a4 = 0; alpha4 = np.pi/2; offset4 = -np.pi/2
    d5 = 75.05; a5 = 0; alpha5 = -np.pi/2; offset5 = np.pi/2
    d6 = 45.6; a6 = 0; alpha6 = 0; offset6 = 0

    # Definición del robot como un objeto DHRobot
    L1 = rtb.RevoluteDH(d=d1, a=a1, alpha=alpha1, offset=offset1)
    L2 = rtb.RevoluteDH(d=d2, a=a2, alpha=alpha2, offset=offset2)
    L3 = rtb.RevoluteDH(d=d3, a=a3, alpha=alpha3, offset=offset3)
    L4 = rtb.RevoluteDH(d=d4, a=a4, alpha=alpha4, offset=offset4)
    L5 = rtb.RevoluteDH(d=d5, a=a5, alpha=alpha5, offset=offset5)
    L6 = rtb.RevoluteDH(d=d6, a=a6, alpha=alpha6, offset=offset6)

    myCobot = rtb.DHRobot([L1, L2, L3, L4, L5, L6], name='myCobot')

    # Definir el vector de ángulos de las articulaciones (en radianes)
    q0 = np.array([math.radians(float(JA1)), math.radians(0.0), math.radians(float(JB1)), math.radians(float(JB2)), math.radians(float(JC1)), math.radians(0.0)])

    # Obtener las posiciones de cada eslabón usando cinemática directa (forward kinematics)
    T = myCobot.fkine_all(q0)  # Calcula las transformaciones de todos los eslabones

    # Recoger las posiciones de los eslabones (solo las posiciones traslacionales, los 3 primeros valores de cada matriz de transformación)
    posiciones = [T[i].t for i in range(len(T))]  # T[i].t obtiene la parte traslacional de la transformación

    # Crear una nueva visualización con Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Definir el color de cada eslabón
    colores_eslabones = ['red', 'green', 'blue', 'orange', 'purple', 'cyan']

    # Dibujar cada eslabón del robot con el color asignado
    for i in range(len(posiciones) - 1):
        start = posiciones[i]
        end = posiciones[i + 1]
        color = colores_eslabones[i]
        dibujar_eslabon(start, end, color, ax)

    # Configurar límites de la gráfica
    ax.set_xlim([-300, 300])  # Ajusta el rango en función de la escala del robot
    ax.set_ylim([-300, 300])
    ax.set_zlim([0, 400])

    # Etiquetas de los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Mostrar la gráfica
    plt.show()

#####################################################################################
# Funciones tic y toc para medir tiempo de ejecución
#####################################################################################

def tic():
    global start_time
    start_time = time.time()

def toc():
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time:.6f} segundos")

#####################################################################################
# Función para el procesado de la imagen y reconocimiento de caracteres
#####################################################################################

def Process_number(image):
    scale_percent = 200     # Escala de aumento
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)   
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC) # Redimensionamiento con interpolación cúbica
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    
    # Aumentar el contraste
    gray_image = cv2.equalizeHist(gray_image)
    
    # Aplicar umbralización
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Aplicar GaussianBlur para reducir el ruido
    blurred_image = cv2.GaussianBlur(threshold_image, (5, 5), 0)
    
    cv2.imwrite("AnguloJoint1.jpg", blurred_image)
    
    tic()
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    whitelist = '0123456789.°-+'       # Listado de caracterers para reconocer
    Texto_joint = pytesseract.image_to_string(blurred_image, config=f'--psm 6 -c tessedit_char_whitelist={whitelist}')
    toc()

    # Tratar de convertir el texto a float, manejar excepciones
    try:
        Texto_joint = float(Texto_joint)
    except ValueError:
        Texto_joint = 0.0
    
    return Texto_joint

# Inicializa los valores de las juntas como variables globales para almacenar sus valores
JA1, JB1, JB2_angular, JC1 = None, None, None, None

#####################################################################################
# Función del envío de datos al robot para el proceso completo
#####################################################################################

def Mandar_Robot_2():
    global JA1, JB1, JB2_angular, JC1
    global COM_PORT

    port_description = "USB-Enhanced-SERIAL CH9102"
    ports = find_mycobot_ports(port_description)
    
    if len(ports) == 1:
        port = ports[0]
    elif len(ports) > 1:
        port = select_mycobot(ports)
        if not port:
            MessageBox.showwarning("Selección inválida", "No se seleccionó un puerto válido.")
            return
    else:
        MessageBox.showwarning("Error", f"No se encontró ningún puerto con la descripción '{port_description}'.")
        return
    
    COM_PORT = connect_and_send_angles(port)
    if not COM_PORT:
        MessageBox.showwarning("Error", "No se pudo establecer la conexión con el puerto seleccionado.")
        return

    try:
        # Enviar los datos que estén disponibles
        mc = MyCobot(COM_PORT, 115200)
        
        # Valores iniciales de las juntas (mantiene los anteriores si no hay nuevos)
        angles = [0, 0, 0, 0, 0, 0]  # Asumiendo 6 juntas en total

        if JA1 is not None:
            angles[0] = float(JA1)  # Actualizar el valor de la primera junta
        if JB1 is not None:
            angles[2] = float(JB1)  # Actualizar el valor de la tercera junta
        if JB2_angular is not None:
            angles[3] = float(JB2_angular)  # Actualizar el valor de la cuarta junta
        if JC1 is not None:
            angles[4] = float(JC1)  # Actualizar el valor de la quinta junta

        # Enviar los ángulos al robot
        mc.send_angles(angles, 90)

        # Recibir la respuesta del robot para confirmar los datos enviados
        Recibido = COM_PORT.readline().decode()
        TempA = (Recibido[Recibido.index("JA") + 2:Recibido.index("JB")])
        TempB = (Recibido[Recibido.index("JB") + 2:Recibido.index(",")])
        TempC = (Recibido[Recibido.index(",") + 1:Recibido.index("JC")])
        TempD = (Recibido[Recibido.index("JC") + 2:Recibido.index(";")])

        # Cierra la conexión
        mc.close()

        # Verificar si los datos se enviaron correctamente
        if (
            (JA1 is None or float(TempA) == float(JA1)) and
            (JB1 is None or float(TempB) == float(JB1)) and
            (JB2_angular is None or float(TempC) == float(JB2_angular)) and
            (JC1 is None or float(TempD) == float(JC1))
        ):
            print("Transmisión Exitosa")
        else:
            MessageBox.showwarning("Alerta", "Error en la transmisión de datos")

    except Exception as error:
        print(error)

#####################################################################################
# Función de proceso completo
#####################################################################################

def proceso_completo(window, image_label, Label_Joint1_Value, Label_Joint2_Value, Label_Joint2_1_Value, Label_Joint3_Value):
    # Paso 1: Capturar la pantalla
    TakeScreenshot(window, image_label)
    
    # Paso 2: Procesar la captura para extraer datos
    MandarCaptura(Label_Joint1_Value, Label_Joint2_Value, Label_Joint2_1_Value, Label_Joint3_Value)
    
    # Paso 3: Mandar los datos al robot
    Mandar_Robot_2()

