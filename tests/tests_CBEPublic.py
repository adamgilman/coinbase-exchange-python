import unittest
from cbe import CoinbaseExchange

import vcr

my_vcr = vcr.VCR(
	serializer = 'yaml',
	cassette_library_dir = 'tests/fixtures/cassettes',
	record_mode = 'once',
	match_on = ['uri', 'method'],
)


class TestCBEPublic(unittest.TestCase):
	def setUp(self):
		self.cbe = CoinbaseExchange()

	def test_getProducts(self):
		with my_vcr.use_cassette('public-getProducts.json'):
			correct = [{u'quote_currency': u'USD', u'display_name': u'BTC/USD', u'quote_increment': 0.01, u'base_max_size': 10000, u'base_currency': u'BTC', u'id': u'BTC-USD', u'base_min_size': 0.01}]
			self.assertEqual( self.cbe.getProducts(), correct )

	def test_getProductOrderBook_1(self):
		with my_vcr.use_cassette('public-getProductOrderBook-1.json'):
			correct = 10306972
			self.assertEqual( self.cbe.getProductOrderBook(level=1)['sequence'], correct )

	def test_getProductOrderBook_2(self):
		with my_vcr.use_cassette('public-getProductOrderBook-2.json'):
			correct = 10306974
			self.assertEqual( self.cbe.getProductOrderBook(level=2)['sequence'], correct )

	def test_getProductOrderBook_3(self):
		with my_vcr.use_cassette('public-getProductOrderBook-3.json'):
			correct = 10306989
			self.assertEqual( self.cbe.getProductOrderBook(level=3)['sequence'], correct )
					
	def test_getProductTicker(self):
		with my_vcr.use_cassette('public-getProductTicker.json'):
			correct = 220334
			self.assertEqual( self.cbe.getProductTicker()['trade_id'], correct )

	def test_getProductTrades(self):
		with my_vcr.use_cassette('public-getProductTrades.json'):
			correct = u'2015-02-15 18:59:44.240795+00'
			self.assertEqual( self.cbe.getProductTrades()[0]['time'], correct )

	def test_getProductStats(self):
		with my_vcr.use_cassette('public-getProductStats.json'):
			correct = u'19382.09151854'
			self.assertEqual( self.cbe.getProductStats()['volume'], correct)

	def test_getCurrencies(self):
		with my_vcr.use_cassette('public-getCurrencies.json'):
			correct = "USD"
			self.assertEqual( self.cbe.getCurrencies()[0]['id'], correct )

	def test_getTime(self):
		with my_vcr.use_cassette('public-getTime.json'):
			correct = 1424034007.831
			self.assertEqual( self.cbe.getTime()['epoch'], correct )