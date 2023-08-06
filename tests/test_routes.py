import unittest
from app import create_app 
import json

class TestRoutes(unittest.TestCase):
   

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.test_csv_file = 'tests/data.csv'



    def test_transactions(self):
        with open(self.test_csv_file, 'rb') as f:
            response = self.client.post('/transactions', content_type='multipart/form-data', data={'file': f})
        
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['status'], "success")

    def test_report(self):
        expected_gross_revenue = 225
        expected_expenses = 72.93
        expected_net_revenue = expected_gross_revenue - expected_expenses
        with open(self.test_csv_file, 'rb') as f:
            self.client.post('/transactions', content_type='multipart/form-data', data={'file': f})
        response = self.client.get('/report')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        print("yp ",  response_data)
        self.assertEqual(response_data['gross-revenue'], expected_gross_revenue)
        self.assertEqual(response_data['expenses'], expected_expenses)
        self.assertEqual(response_data['net-revenue'], expected_net_revenue)

if __name__ == '__main__':
    unittest.main()
