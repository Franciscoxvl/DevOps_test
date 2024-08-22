import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FlaskAppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicializa el navegador Chrome
        cls.driver = webdriver.Chrome()

    def test_home_page(self):
        # Abre la página principal
        self.driver.get("http://localhost:5000/")
        self.assertIn("Home", self.driver.title)

        # Busca un elemento dentro de la página
        elem = self.driver.find_element_by_tag_name("h1")
        self.assertEqual(elem.text, "Bienvenido a la Página Principal")

    def test_dashboard_page(self):
        # Abre la página del dashboard
        self.driver.get("http://localhost:5000/dashboard")
        self.assertIn("Dashboard", self.driver.title)

        # Verifica que el contenido del dashboard esté presente
        elem = self.driver.find_element_by_tag_name("h2")
        self.assertEqual(elem.text, "Panel de Control")

    @classmethod
    def tearDownClass(cls):
        # Cierra el navegador
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
