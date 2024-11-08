from pymycobot.mycobot import MyCobot
import time

mc = MyCobot('COM14',115200) # Establece conexión con el puerto donde se encuentra el coneectado el robot
mc.send_angles([0,0,0,0,0,0],50) # Envía la posición de las juntas para ajustarse a la una velocidad del 50%

# Cierra la conexión
mc.close()
