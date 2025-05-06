# Captcha-Sicoes-Fichas

Este repositorio contiene tres scripts de Python desarrollados con la librería Selenium, diseñados para interactuar con el sitio web del Sicoes (Sistema de Contrataciones Estatales).

## Descripción de los Scripts

1.  **`explorar_sicoes.py` (Nombre Sugerido):**
    * **Función:** Este script automatiza la navegación a través de las tablas de datos del Sicoes. Recorre cada fila de la tabla e ingresa individualmente a la página de "Ver Ficha" correspondiente a cada registro.
    * **Objetivo:** Facilitar la exploración detallada de la información de cada proceso de contratación listado en las tablas del Sicoes.

2.  **`superar_captcha.py` (Nombre Sugerido):**
    * **Función:** Este script tiene como objetivo superar automáticamente el sistema CAPTCHA presente en el sitio web del Sicoes. Utiliza la información de la sesión del usuario almacenada en el navegador para validar el CAPTCHA sin intervención manual.
    * **Objetivo:** Automatizar el proceso de autenticación y acceso a las secciones protegidas por CAPTCHA, agilizando la interacción con el sitio.

3.  **`integracion_automatica.py` (Nombre Sugerido):**
    * **Función:** Este script busca integrar la funcionalidad de los dos scripts anteriores en una única ejecución.
    * **Estado Actual:** Actualmente, la detección del CAPTCHA en la sección de "ficha del proceso" no está funcionando correctamente en esta implementación integrada.
    * **Objetivo (Previsto):** Automatizar completamente el flujo de trabajo, desde la navegación por las tablas hasta la superación del CAPTCHA al acceder a la información detallada de cada ficha.

## Requisitos

* **Python 3.x** instalado en su sistema.
* Las siguientes librerías de Python deben estar instaladas:
    ```bash
    pip install selenium
    ```
* Un navegador web compatible con Selenium (por ejemplo, Google Chrome o Mozilla Firefox) y el respectivo WebDriver instalado y configurado en su PATH o especificado en el script.
* Acceso al sitio web del Sicoes.
* Sesión de usuario activa en el navegador utilizado por el script para la funcionalidad de superación de CAPTCHA.

## Instrucciones de Uso

1.  **Clonar el Repositorio (Opcional):**
    ```bash
    git clone [https://del-source.com/](https://del-source.com/)
    cd Captcha-Sicoes-Fichas
    ```

2.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt  # Si se incluye un archivo requirements.txt
    ```
    Asegúrese de instalar Selenium manualmente:
    ```bash
    pip install selenium
    ```

3.  **Configurar los Scripts (Si es necesario):**
    * Revise los scripts (`.py` files) y ajuste cualquier configuración necesaria, como las rutas a los WebDrivers (si no están en el PATH), las URLs del Sicoes, o los selectores de elementos web si el sitio cambia.

4.  **Ejecutar los Scripts:**
    * Para ejecutar el primer script (explorar las tablas):
        ```bash
        python explorar_sicoes.py
        ```
    * Para ejecutar el segundo script (superar el CAPTCHA):
        ```bash
        python superar_captcha.py
        ```
    * Para intentar ejecutar el script integrado (con la advertencia sobre el CAPTCHA):
        ```bash
        python integracion_automatica.py
        ```

## Estado del Proyecto

* **Script 1 (Exploración de Tablas):** Funcional.
* **Script 2 (Superación de CAPTCHA):** Funcional, dependiendo de la validez de la sesión del navegador.
* **Script 3 (Integración):** Funcional en la navegación, pero **la detección del CAPTCHA en la sección de la ficha del proceso no está funcionando actualmente.** Se requiere investigación y posible refactorización para solucionar este problema.
