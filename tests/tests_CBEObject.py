import unittest
from cbe import CoinbaseExchange

class TestCBEObject(unittest.TestCase):
	def setUp(self):
		self.cbe = CoinbaseExchange()

	def test_CBEExists(self):		
		self.assertEqual( type(self.cbe), CoinbaseExchange )
