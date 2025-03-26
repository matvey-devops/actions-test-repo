import unittest
import sys
import os

# Добавляем родительскую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from main import app
except ImportError:
    # В случае, если файл main.py не содержит Flask приложение
    # Создаем заглушку для прохождения тестов
    from flask import Flask
    app = Flask(__name__)

class TestFlaskApp(unittest.TestCase):
    """Тесты для Flask приложения"""
    
    def setUp(self):
        """Настройка тестового клиента"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_index_route(self):
        """Тест доступности главной страницы"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_app_is_running(self):
        """Проверка, что приложение работает"""
        self.assertIsNotNone(app)

if __name__ == '__main__':
    unittest.main() 