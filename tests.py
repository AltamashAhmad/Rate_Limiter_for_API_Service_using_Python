import unittest
import time
from app import app, redis_conn

class RateLimiterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_within_rate_limit(self):
        headers = {'X-User-ID': 'test_user', 'X-User-Tier': 'free'}
        for _ in range(10):
            response = self.app.post('/api/v1/analytics/submit', json={}, headers=headers)
            self.assertEqual(response.status_code, 200)

    def test_exceed_rate_limit(self):
        headers = {'X-User-ID': 'test_user', 'X-User-Tier': 'free'}
        for _ in range(11):
            response = self.app.post('/api/v1/analytics/submit', json={}, headers=headers)
        self.assertEqual(response.status_code, 429)

if __name__ == '__main__':
    unittest.main()
