# 경로를 잡아줘야대지만 연습용이라 무시함.
import sys
from os import path
sys.path.append(path.dirname(path.dirname( path.abspath(__file__))))

import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, World!"})

    def test_read_item(self):
        response = self.client.get("/items/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1, "q": None})

    def test_read_item_with_query_param(self):
        response = self.client.get("/items/1?q=test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1, "q": "test"})

if __name__ == "__main__":
    unittest.main()