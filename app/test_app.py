import unittest
from app import app

class BasicTests(unittest.TestCase):

    # 1. Preparazione del test
    def setUp(self):
        # Mettiamo l'app in modalità test
        app.testing = True
        self.app = app.test_client()

    # 2. Controlla se la Homepage risponde
    def test_home_page_loads(self):
        # Finge di andare su "/" (la home)
        response = self.app.get('/')
        
        # Verifica che il codice di risposta sia 200 
        self.assertEqual(response.status_code, 200)
        
        # Verifica che nella pagina ci sia la scritta giusta
        self.assertIn(b"Markdown Converter", response.data)

if __name__ == "__main__":
    unittest.main()