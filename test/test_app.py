import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

    def test_status(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"status": "running"', response.data)

    def test_about(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"message": "This is a sample Flask application"', response.data)

if __name__ == "__main__":
    unittest.main()
