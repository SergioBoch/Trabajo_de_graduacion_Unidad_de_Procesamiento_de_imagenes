<div style="display: flex; justify-content: space-between; align-items: center;">
    <img src="https://redfia.usac.edu.gt/wp-content/uploads/2019/09/logos-2017-hq-01_1_orig-1024x288.png" alt="Logo UVG" style="width: 45%; margin-bottom: -20px;"/>
    <img src="https://res.cloudinary.com/webuvg/image/upload/f_auto,q_auto,w_329,c_scale,fl_lossy,dpr_2.63/v1684945887/WEB/Academico/Facultades/FacultadIngenieria.png" alt="Logo Ingeniería" style="width: 45%;"/>
</div>


<div style="text-align: center; padding: 20px; border-radius: 8px;">
    <h1 style="margin: 0;">Optimización de la herramienta de procesamiento de imágenes para el sistema Brainlab de HUMANA</h1>
    <h2 style="margin: 5px 0 0 0;">Fase IV</h2>
    <h3 style="margin: 5px 0;">
        <a href="mailto:boc20887@uvg.edu.gt" target="_blank">Sergio Alejandro Boch Ixén</a>
    </h3>
    <h4 style="margin: 5px 0;">Departamento de Ingeniería Mecatrónica</h4>
    <h4 style="margin: 5px 0;">Universidad del Valle de Guatemala</h4>
</div>

---
##  **Descripción**
Este trabajo de graduación se centra en la optimización de algoritmos para el procesamiento de imágenes y el reconocimiento óptico de caracteres en el sistema **Brainlab de HUMANA**, así como en su integración con un sistema robótico físico. La investigación aborda el desarrollo de un protocolo de comunicación y una **interfaz gráfica de usuario (GUI)** que permite una interacción fluida y eficaz entre el sistema de procesamiento y el robot.

El procesamiento de imágenes es esencial para aplicaciones médicas avanzadas, como las que se utilizan en procedimientos quirúrgicos donde la precisión y la eficiencia son críticas. Este proyecto busca mejorar los procesos manuales actuales con herramientas automatizadas que puedan ser utilizadas en entornos reales.

<div style="text-align: center;">
    <img src="https://www.brainlab.com/cdn-cgi/image/w=7678,f=jpeg/https://assetmanagement.brainlab.com/Images/Cirq%26Curve%200724_300dpi_03s.jpg" alt="Sistema Brainlab de HUMANA" style="width: 60%; margin-bottom: 10px;"/>
    <p style="font-size: 14px; color: gray;">Fuente: [Cirq para neurocirugía funcional](https://www.brainlab.com/es/productos-de-cirugia/fsn-hubpage/cirq-fsn/)</p>
</div>

---
### **Objetivos**
- **Optimización de algoritmos de procesamiento de imágenes.**
- **Implementación y validación de un protocolo de comunicación UART.**
- **Desarrollo de una GUI amigable y funcional.**
- **Integración completa con un sistema robótico físico.**

---

## Enfoque y Metodología

### Procesamiento de Imágenes
Utilizando librerías como **OpenCV** y **PyTesseract**, se implementaron técnicas de escalado a grises, umbralización y reducción de ruido para mejorar la calidad de las imágenes antes del reconocimiento de caracteres.

### Comunicación con Sistemas Robóticos
El protocolo **UART** se implementó para garantizar la comunicación segura y eficaz entre el sistema de procesamiento de imágenes y el robot, permitiendo el envío y la confirmación de comandos en tiempo real.

---

## Características del Proyecto

- **Procesamiento de imágenes con algoritmos optimizados**.
- **Reconocimiento Óptico de Caracteres (OCR)** utilizando Tesseract y pruebas con otros motores como Asprise OCR.
- **Integración de un protocolo UART** para la comunicación bidireccional con un sistema robótico.
- **Desarrollo de una GUI interactiva** que permite capturas de pantalla, procesamiento de imágenes y gestión de datos.

---

## Tecnologías y Librerías Utilizadas

- **Python**: Lenguaje de programación principal para el desarrollo de scripts y la interfaz gráfica.
- **OpenCV**: Para el procesamiento de imágenes y la manipulación de imágenes en tiempo real.
- **Tesseract OCR**: Herramienta de código abierto para el reconocimiento de caracteres.
- **Tkinter**: Utilizado para la creación de la GUI.
- **Asprise OCR (opcional)**: Motor comercial de reconocimiento de caracteres.
- **Numpy y Scipy**: Para operaciones matemáticas y de procesamiento numérico.
- **PySerial**: Para la implementación del protocolo de comunicación UART.

---

## Guía de instalación de librerías
Este proyecto utiliza varias bibliotecas y herramientas para crear una interfaz gráfica de usuario (GUI) y realizar control robótico, procesamiento de imágenes, comunicación serial y visualización de datos. Las siguientes instrucciones te guiarán en cómo instalar cada biblioteca requerida y configurar tu entorno para ejecutar el proyecto sin problemas.

## Prerrequisitos
Asegúrate de tener Python 3.x instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Guía de Instalación Paso a Paso
Abre tu terminal y ejecuta los siguientes comandos para instalar los paquetes necesarios:

```bash
# Actualizar pip a la última versión
python -m pip install --upgrade pip

# Instalar tkinter (normalmente incluido con Python, pero se puede instalar si no está presente)
# Windows:
python -m pip install tk

# Instalar ttkthemes para widgets temáticos
python -m pip install ttkthemes

# Instalar pyautogui para automatización de GUI
python -m pip install pyautogui

# Instalar Pillow para procesamiento de imágenes
python -m pip install pillow

# Instalar serial para comunicación serial
python -m pip install pyserial

# Instalar OpenCV para visión por computadora
python -m pip install opencv-python

# Instalar numpy para operaciones numéricas
python -m pip install numpy

# Instalar pytesseract para reconocimiento óptico de caracteres (OCR)
python -m pip install pytesseract

# Instalar pymycobot para control robótico de MyCobot
python -m pip install pymycobot

# Instalar pandas para manipulación de datos
python -m pip install pandas

# Instalar matplotlib para graficar y visualizar datos
python -m pip install matplotlib

# Instalar roboticstoolbox para simulación y cinemática de robots
python -m pip install roboticstoolbox-python

# Instalar spatialmath para transformaciones 3D y cálculos de poses
python -m pip install spatialmath-python

# Asegurarse de que MATLAB Engine API para Python esté instalado
# Nota: MATLAB debe instalarse por separado, y seguir las instrucciones en:
# https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html
```

### Configuración Adicional
- **pytesseract** requiere que Tesseract-OCR esté instalado en tu sistema. Sigue las instrucciones [aqui](https://github.com/tesseract-ocr/tesseract) para instalarlo.
- Para **MATLAB Engine API**, asegúrate de tener MATLAB instalado y configurado correctamente según la documentación de MathWorks.

### Verificación de Instalaciones
Puedes verificar que las bibliotecas estén instaladas correctamente ejecutando:

```bash
python -m pip show tk ttkthemes pyautogui pillow pyserial opencv-python numpy pytesseract pymycobot pandas matplotlib roboticstoolbox-python spatialmath-python
```

Esto mostrará la versión y detalles de cada paquete.

## Solución de Problemas
Si encuentras problemas durante la instalación o ejecución del proyecto, considera:
- Verificar si hay errores tipográficos en tu código.
- Asegurarte de que tu entorno de Python esté configurado correctamente.
- Consultar la documentación de cada biblioteca para errores específicos.

---

## Resultados y Conclusiones

- **Mejoras significativas en la precisión de reconocimiento de caracteres.**
- **Interfaz de usuario intuitiva y fácil de usar.**
- **Integración exitosa con sistemas robóticos, validada con pruebas físicas.**

Este trabajo marca un avance en la integración de herramientas de procesamiento de imágenes en aplicaciones médicas y robóticas, ofreciendo soluciones más rápidas y confiables para profesionales del sector.

---

## Créditos y Agradecimientos

Este proyecto fue realizado con la colaboración del **Centro de Epilepsia y Neurocirugía Funcional HUMANA** y la **Facultad de Ingeniería de la Universidad del Valle de Guatemala**.

