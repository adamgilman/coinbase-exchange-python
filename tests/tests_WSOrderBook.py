import unittest
from cbe import CoinbaseExchange

import vcr

my_vcr = vcr.VCR(
	serializer = 'yaml',
	cassette_library_dir = 'tests/fixtures/cassettes',
	record_mode = 'once',
	match_on = ['uri', 'method'],
)


class TestCBEWSOrderBook(unittest.TestCase):
	def setUp(self):
		self.cbe = CoinbaseExchange()
	
	def test_OrderBookSubscribe(self):
		pass #unknown how to test?

	def test_OrderBookMessages(self):
		self.cbe.subscribe()
		for msg in self.cbe.streaming_orderbook():
			print msg
			self.assertTrue(msg.has_key('sequence'))
			self.assertTrue(msg.has_key('order_id'))



'''
Send a subscribe message for the product of interest.
Queue any messages received over the websocket stream.
Make a REST request for the order book snapshot from the REST feed.
Playback queued messages, discarding sequence numbers before or equal to the snapshot sequence number.
Apply playback messages to the snapshot as needed (see below).
After playback is complete, apply real-time stream messages as they arrive.
'''

'''	def test_getProducts(self):
		with my_vcr.use_cassette('public-getProducts.json'):
			correct = [{u'quote_currency': u'USD', u'display_name': u'BTC/USD', u'quote_increment': 0.01, u'base_max_size': 10000, u'base_currency': u'BTC', u'id': u'BTC-USD', u'base_min_size': 0.01}]
			self.assertEqual( self.cbe.getProducts(), correct )
'''
	