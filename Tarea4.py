import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configuramos el navegador
driver = webdriver.Chrome()

# Creamos la función para abrir una URL en Google Chrome
def abrir_url_en_chrome(url):
    try:
        subprocess.run(["start", "chrome", url], shell=True)
        print("Se abrió la URL en Google Chrome.")
    except Exception as e:
        print("Ocurrió un error al abrir la URL en Google Chrome:", e)

# Creamos una carpeta para las imágenes si no existe
if not os.path.exists("imagenes_de_prueba"):
    os.mkdir("imagenes_de_prueba")

if __name__ == "__main__":
    try:
        # Abrimos la primera URL y tomamos captura
        driver.get("https://www3.animeflv.net/")
        driver.save_screenshot("imagenes_de_prueba/screenshot_1.png")
        time.sleep(10)

        # Abrimos la segunda URL y tomamos captura
        driver.get("https://www3.animeflv.net/perfil/Destroyer2729/favoritos")
        driver.save_screenshot("imagenes_de_prueba/screenshot_2.png")
        time.sleep(5)

        # Abrimos la tercera URL y tomamos captura
        driver.get("https://www3.animeflv.net/browse")
        driver.save_screenshot("imagenes_de_prueba/screenshot_3.png")
        time.sleep(5)

    except Exception as e:
        print("Ocurrió un error:", e)

    finally:
        # Cerramos el navegador
        driver.quit()