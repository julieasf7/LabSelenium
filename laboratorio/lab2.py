from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import pytest

# Abre la aplicacion y cierra el popup inicial
@pytest.fixture
def open_app(driver):
    try:
        driver.get("https://juice-shop.herokuapp.com/#/search")
        time.sleep(2)  # Espera para que cargue el popup
        close_button = driver.find_element(By.CLASS_NAME, 'close-dialog')
        close_button.click()
    except Exception as e:
        print(f"No se pudo cerrar el popup: {e}")

# Prueba de Cross-Site Scripting (XSS)
def test_xss(driver, open_app):
    search_box = driver.find_element(By.ID, 'searchQuery')
    search_box.click()
    
    # Intento de inyección de script (XSS)
    search_text = driver.find_element(By.ID, 'mat-input-0')
    search_text.send_keys('<iframe src="javascript:alert(\'XSS\')">')
    search_text.send_keys(Keys.RETURN)
    time.sleep(2)
    
    # Verificación de la ejecución del script
    try:
        alert = Alert(driver)
        alert_text = alert.text
        
        assert "XSS" in alert_text, "Alerta no contiene XSS"
        alert.accept()
    except Exception as e:
        pytest.fail(f"No se encontró alerta o error al manejarla: {e}")