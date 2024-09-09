import unittest
from datetime import datetime

def validate_stock_data(data):
    try:
        assert isinstance(data['open'], (float, int)), "Open should be a decimal"
        assert isinstance(data['high'], (float, int)), "High should be a decimal"
        assert isinstance(data['low'], (float, int)), "Low should be a decimal"
        assert isinstance(data['close'], (float, int)), "Close should be a decimal"
        assert isinstance(data['volume'], int), "Volume should be an integer"
        assert isinstance(data['instrument'], str), "Instrument should be a string"
        assert isinstance(data['datetime'], datetime), "Datetime should be a datetime object"
        
        return True  
    except AssertionError as e:
        return str(e) 

class TestStockDataValidation(unittest.TestCase):
    
    def setUp(self):
        self.valid_data = {
            'open': 120.50,
            'high': 125.00,
            'low': 119.75,
            'close': 123.45,
            'volume': 1000,
            'instrument': "AAPL",
            'datetime': datetime(2023, 9, 9, 10, 30)
        }
    
    # Test case: Check if all data is valid
    def test_valid_data(self):
        result = validate_stock_data(self.valid_data)
        self.assertTrue(result)
    
    # Test case: Check if 'open' is not a decimal
    def test_invalid_open(self):
        invalid_data = self.valid_data.copy()
        invalid_data['open'] = '120.50'  # Invalid: should be a float, not string
        result = validate_stock_data(invalid_data)
        self.assertEqual(result, "Open should be a decimal")
    
    # Test case: Check if 'volume' is not an integer
    def test_invalid_volume(self):
        invalid_data = self.valid_data.copy()
        invalid_data['volume'] = 1000.5  # Invalid: volume should be an integer
        result = validate_stock_data(invalid_data)
        self.assertEqual(result, "Volume should be an integer")
    
    # Test case: Check if 'instrument' is not a string
    def test_invalid_instrument(self):
        invalid_data = self.valid_data.copy()
        invalid_data['instrument'] = 123  # Invalid: should be a string
        result = validate_stock_data(invalid_data)
        self.assertEqual(result, "Instrument should be a string")
    
    # Test case: Check if 'datetime' is not a datetime object
    def test_invalid_datetime(self):
        invalid_data = self.valid_data.copy()
        invalid_data['datetime'] = '2023-09-09'  # Invalid: should be datetime object, not string
        result = validate_stock_data(invalid_data)
        self.assertEqual(result, "Datetime should be a datetime object")

if __name__ == '__main__':
    unittest.main()
