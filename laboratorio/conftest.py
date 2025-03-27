import pytest # pytest es un framework de pruebas para Python que facilita la ejecución y organización de tests automatizados.

# Agrega la opción --browser para elegir entre Chrome o Firefox
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Elige el navegador: chrome o firefox")

# Configura y retorna el WebDriver de Chrome o Firefox según la opción ingresada.
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()

    from selenium import webdriver
    from selenium.common.exceptions import WebDriverException

    try:
        if browser == "chrome":
            driver = webdriver.Chrome()
            # Usar esta linea En caso de realizar la instalacion manual del driver
            # driver = webdriver.Chrome(executable_path="ruta/al/chromedriver")
        elif browser == "firefox":
            driver = webdriver.Firefox()
            # Usar esta linea En caso de realizar la instalacion manual del driver
            # driver = webdriver.Firefox(executable_path="ruta/al/geckodriver")
        else:
            pytest.exit("❌ Navegador no soportado. Usa --browser=chrome o --browser=firefox", returncode=1)
    except WebDriverException as e:
        pytest.exit(f"❌ Error: El driver de {browser} no está instalado o configurado correctamente.\n{e}", returncode=1)

    yield driver
    driver.quit()
