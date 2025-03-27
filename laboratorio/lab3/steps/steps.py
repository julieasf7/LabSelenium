from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
import time


@given('I am on the Juice Shop search page')
def step_given_search_page(context):
    #context.driver = webdriver.Firefox()  # Asegúrate de tener el geckodriver configurado
    context.driver = webdriver.Chrome() 
    context.driver.get("https://juice-shop.herokuapp.com/#/search")
    
    # Cerrar PopUp
    time.sleep(2)
    close_button = context.driver.find_element(By.CLASS_NAME, 'close-dialog')
    close_button.click()

@when('I enter the payload "{payload}" into the search box')
def step_when_enter_payload(context, payload):
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
        assert "XSS" in alert_text, f"Expected 'XSS' but got {alert_text}"

        print("XSS successfully executed!")
        alert.accept()  # Acepta la alerta
    except NoAlertPresentException as e:
        # Genera un fallo explícito si no aparece la alerta
        raise AssertionError("No alert")
    finally:
        context.driver.quit()
