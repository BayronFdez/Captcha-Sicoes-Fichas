import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Cambiar dependiendo del Sistema Operativo y nombre de USUARIO
#Linux
#user_data_dir = "/home/Usuario/snap/chromium/common/chromium"
#Windows
user_data_dir = "C:\\Users\\USUARIO\\AppData\\Local\\Chromium\\User Data"

# Opciones de Chrome
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--profile-directory=Default")  # Cambia si usas otro perfil
chrome_options.add_experimental_option("detach", True)

# Ocultar que es Selenium
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Iniciar el driver
driver = webdriver.Chrome(options=chrome_options)

# Ocultar navigator.webdriver
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': '''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    '''
})

# Ir al demo de reCAPTCHA
driver.get("https://www.google.com/recaptcha/api2/demo")

# Espera aleatoria
time.sleep(random.uniform(2.5, 4.5))

# Simular comportamiento humano
ActionChains(driver).move_by_offset(100, 100).perform()
time.sleep(random.uniform(0.5, 1.5))
driver.execute_script("window.scrollTo(0, 300);")
time.sleep(random.uniform(1, 2))

# Cambiar a iframe y esperar que el checkbox esté listo
WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
)

checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
)
checkbox.click()

print("[+] CAPTCHA marcado.")

# No cerramos el navegador porque usamos detach=True'''


