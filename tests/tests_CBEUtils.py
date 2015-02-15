import unittest
from datetime import datetime
from cbe import CoinbaseExchange
from cbe.utils import ConvertTime

import pytz, vcr

my_vcr = vcr.VCR(
	serializer = 'yaml',
	cassette_library_dir = 'tests/fixtures/cassettes',
	record_mode = 'once',
	match_on = ['uri', 'method'],
)

class TestCBEUtils(unittest.TestCase):
	def setUp(self):
		self.cbe = CoinbaseExchange()

	def test_convertTimeToPython(self):
		json_return = u'2015-02-15 18:59:44.240795+00'
		python_time = pytz.utc.localize( datetime(year=2015, month=2, day=15, hour=18, minute=59, second=44, microsecond=240795) )
		self.assertEqual( ConvertTime(json_return), python_time )

	def test_injectPythonTimes(self):
		with my_vcr.use_cassette('public-getProductTrades-Time.json'):
			python_time = ConvertTime( self.cbe.getProductTrades()[0]['time'] )
			self.assertEqual( self.cbe.getProductTrades()[0]['python_time'], python_time )
