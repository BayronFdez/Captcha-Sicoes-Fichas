from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    options = Options()
    # options.add_argument("--headless")  # opcional para ejecutar sin abrir ventana
    return webdriver.Chrome(options=options)

def ingresar_a_convocatorias(driver):
    driver.get("https://www.sicoes.gob.bo/portal/index.php")
    time.sleep(3)

    # Cerrar el modal
    try:
        boton_cerrar = driver.find_element(By.XPATH, "//div[@id='modalComunicados'][contains(@style, 'display: block')]//button[@class='close']/span[text()='×']/..")
        boton_cerrar.click()
        time.sleep(2)
    except:
        pass  # Por si no aparece

    # Click en "Convocatorias"
    convocatorias = driver.find_element(By.XPATH, '//a[contains(@onclick, "irLink") and .//h4[text()="Convocatorias"]]')
    convocatorias.click()
    time.sleep(3)

def procesar_convocatorias(driver, filas_a_procesar=3):
    for i in range(filas_a_procesar):
        print(f"\n🌀 Procesando fila {i + 1}...")

        # Entrar a convocatorias otra vez
        ingresar_a_convocatorias(driver)

        # Esperar que cargue la tabla
        time.sleep(3)

        # Buscar filas de la tabla
        filas = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        if i >= len(filas):
            print("No hay más filas.")
            break

        fila = filas[i]

        # Buscar botón "Ver Ficha"
        ver_ficha = fila.find_element(By.XPATH, './/a[contains(text(), "Ver Ficha")]')
        ver_ficha.click()
        # Abrir en nueva pestaña con JS

        print("✅ Ficha abierta:", driver.current_url)

        # Esperar (Apartado Captcha)
        time.sleep(3)




        # Cerrar ficha y volver a la pestaña anterior
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("🔁 Regresando al inicio")

# MAIN
driver = setup_driver()
try:
    procesar_convocatorias(driver, filas_a_procesar=10)
finally:
    driver.quit()
