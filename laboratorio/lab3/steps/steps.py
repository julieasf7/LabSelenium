from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
import time
import logging

# Configurar logging para registrar los resultados de las pruebas
logging.basicConfig(filename="test_results.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@given('I am on the Juice Shop search page')
def step_given_search_page(context):
    context.driver = webdriver.Chrome()  # Puedes cambiarlo a Firefox si lo prefieres
    context.driver.get("https://juice-shop.herokuapp.com/#/search")

    # Cerrar PopUp
    time.sleep(2)
    try:
        close_button = context.driver.find_element(By.CLASS_NAME, 'close-dialog')
        close_button.click()
        logging.info("Popup cerrado exitosamente.")
    except Exception as e:
        logging.warning(f"No se pudo cerrar el popup: {e}")

@when('I enter the payload "{payload}" into the search box')
def step_when_enter_payload(context, payload):
    context.payload = payload  # Guardamos el payload en el contexto para su uso en la verificación

    search_box = context.driver.find_element(By.ID, 'searchQuery')
    search_box.click()

    search_text = context.driver.find_element(By.ID, 'mat-input-0')
    search_text.send_keys(payload)  # Inyecta el código XSS desde el parámetro payload
    search_text.send_keys(Keys.RETURN)
    time.sleep(5)  # Espera que la alerta se dispare

@then('I should see an alert with the message "XSS"')
def step_then_see_alert(context):
    try:
        alert = Alert(context.driver)
        alert_text = alert.text
        assert "XSS" in alert_text, f"Expected 'XSS' but got '{alert_text}'"

        logging.info(f"XSS detectado con el payload: {context.payload}")
        alert.accept()  # Cierra la alerta
    except NoAlertPresentException:
        logging.error(f"No se detectó XSS con el payload: {context.payload}")
        raise AssertionError("No alert detected")
    finally:
        context.driver.quit()
