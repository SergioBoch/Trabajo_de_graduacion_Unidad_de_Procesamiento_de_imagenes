import roboticstoolbox as rtb
import numpy as np
import math
import matplotlib.pyplot as plt

# Función para dibujar un eslabón de un robot
def dibujar_eslabon(start, end, color, ax):
    """Dibuja un eslabón del robot desde el punto start al punto end con un color específico."""
    ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], color=color, linewidth=5)

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
    q0 = np.array([math.radians(30), math.radians(0.0), math.radians(45), math.radians(10), math.radians(20), math.radians(0.0)])

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

# Ejecutar la simulación
simulation()
