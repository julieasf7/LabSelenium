# LabSelenium
<p align="left">
 <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
</p>
Este laboratorio proporciona un entorno de pruebas automatizadas utilizando Selenium en Python. A continuación, se detallan los pasos necesarios para configurarlo y ejecutarlo correctamente.

### 📌 Requisitos
* Python: 3.12.7 (Recomendado)
> [!WARNING]
>  Este laboratorio fue desarrollado y probado en Python 3.12.7. Se recomienda utilizar esta versión para evitar incompatibilidades. Sin embargo, versiones cercanas de Python 3.10+ podrían funcionar, aunque no han sido probadas.
* Mozilla Firefox o Google Chrome
* Geckodriver (para Firefox) o Chromedriver (para Chrome)
  

### 🚀 Instalación
1. Clonar el repositorio:
    ```
    git clone https://github.com/julieasf7/LabSelenium
    cd LabSelenium
    ```
2. Crear y activar un entorno virtual:
    ```
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate     # En Windows
    ```
3. Instalar las dependencias:
    ```
    pip install -r requirements.txt
    ```

### 🌍 Configurar el Driver de Selenium
#### 🔹Opción 1: Firefox (Recomendado)
1. Descargar Geckodriver desde la página oficial:
    - Descargar [Geckodriver](https://github.com/mozilla/geckodriver/releases)
    - Seleccionar la versión adecuada para tu sistema operativo.

2. Extraer el archivo y moverlo a una ubicación accesible:
    - Se recomienda guardar el driver en la carpeta drivers/ dentro del proyecto.

3. Verificar la instalación ejecutando:
    ```
    geckodriver --version
    ```

#### 🔹 Opción 2: Google Chrome
1. Descargar Chromedriver desde la página oficial:
    - Descargar [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=es-419)
    - Asegurarte de que la versión sea compatible con tu navegador.

2. Guardar el ejecutable en una ruta accesible.
     - Se recomienda guardar el driver en la carpeta drivers/ dentro del proyecto.
