# test_cryptoapi.py
"""
Tests for CryptoAPI module.
"""

import unittest
from cryptoapi import CryptoAPI

class TestCryptoAPI(unittest.TestCase):
    """Test cases for CryptoAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoAPI()
        self.assertIsInstance(instance, CryptoAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
