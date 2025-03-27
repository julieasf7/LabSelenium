# Prueba para verificar que la página Juice Shop carga correctamente
def test_juice_shop_title(driver):
    # Ruta de la aplicacion
    driver.get("https://juice-shop.herokuapp.com/#/") 
    
    # Verificar que el título de la página no está vacío
    assert driver.title.strip() != "", "El título de la página está vacío"

    # Capturar pantalla
    driver.save_screenshot("imagenes/lab1.png")
