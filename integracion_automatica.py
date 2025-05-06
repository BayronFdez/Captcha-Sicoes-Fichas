import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar perfil de usuario y evasión de detección
#Cambiar dependiendo del Sistema Operativo y nombre de USUARIO
#Linux
#user_data_dir = "/home/Usuario/snap/chromium/common/chromium"
#Windows
user_data_dir = "C:\\Users\\USUARIO\\AppData\\Local\\Chromium\\User Data"
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Iniciar driver con configuración
driver = webdriver.Chrome(options=chrome_options)

# Ocultar navigator.webdriver
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    '''
})

# Función: abrir SICOES y entrar a "Convocatorias"
def ingresar_a_convocatorias(driver):
    driver.get("https://www.sicoes.gob.bo/portal/index.php")
    time.sleep(2)

    # Cerrar modal si aparece
    try:
        boton_cerrar = driver.find_element(By.XPATH, "//div[@id='modalComunicados'][contains(@style, 'display: block')]//button[@class='close']/span[text()='×']/..")
        boton_cerrar.click()
        time.sleep(1)
    except:
        pass  

    # Click en "Convocatorias"
    convocatorias = driver.find_element(By.XPATH, '//a[contains(@onclick, "irLink") and .//h4[text()="Convocatorias"]]')
    convocatorias.click()
    time.sleep(3)

# Función principal: recorrer filas y abrir ficha
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

        # Esperar (simulamos análisis)
        time.sleep(2)
        
        try:
            # Esperar hasta 20 segundos a que aparezca el iframe
            captcha_iframe = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
            )

            # Cambiar al iframe
            driver.switch_to.frame(captcha_iframe)
            print("✅ Cambiado al iframe de reCAPTCHA")

            # Esperar que el checkbox esté listo
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
            )
            checkbox.click()
            print("🟢 CAPTCHA marcado con éxito.")

            # Volver al contenido principal
            driver.switch_to.default_content()

        except Exception as e:
            print("❌ No se pudo interactuar con el CAPTCHA:", e)
        # Cerrar ficha y volver a la pestaña anterior
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print("🔁 Regresando al inicio")

# Ejecutar
try:
    procesar_convocatorias(driver, filas_a_procesar=3)
finally:
    driver.quit()
