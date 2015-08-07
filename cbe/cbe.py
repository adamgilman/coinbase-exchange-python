import requests, simplejson
from time import sleep
from utils import insertPythonTime
from websocket import create_connection


class CoinbaseExchange(object):
	def __init__(self):
		self.api_url = 'http://api.exchange.coinbase.com/'
		self.ws = None
		self.ws_messages = None

	def _call(self, method, params={}):
		url = {
				'products' 			: 'products',
				'order_book'		: 'products/BTC-USD/book',
				'product_ticker'	: 'products/BTC-USD/ticker',
				'product_trades'	: 'products/BTC-USD/trades',
				'product_stats'		: 'products/BTC-USD/stats',
				'currencies'		: 'currencies/',
				'time'				: 'time/'
		}

		return insertPythonTime( requests.get(self.api_url + url[method], params=params).json() )

	def getProducts(self):
		return self._call("products")

	def getProductOrderBook(self, level=1):
		return self._call("order_book", {'level':level})

	def getProductTicker(self):
		return self._call("product_ticker")
		
	def getProductTrades(self):
		return self._call("product_trades")

	def getProductHistoricRates(self):
		raise Exception("not implemented yet")

	def getProductStats(self):
		return self._call("product_stats")

	def getCurrencies(self):
		return self._call("currencies")

	def getTime(self):
		return self._call("time")

	# WebSocket Based OrderBook

	def subscribe(self):
		if self.ws is None:
			self.ws = create_connection("wss://ws-feed.exchange.coinbase.com",
											on_message = self._ws_on_message,
											on_error = self._ws_on_error,
											on_close = self._ws_on_close)
			subscribe_message = simplejson.dumps('{"type": "subscribe", "product_id": "BTC-USD"}')
			self.ws.send(subscribe_message)

	def _ws_on_error(self): pass

	def _ws_on_close(self): 
		self.ws = None
		self.ws_messages = None

	def _ws_on_message(self, message):
		if self.ws_messages is not None:
			self.ws_messages.append(message)
		else:
			pass
			#no streaming client connect open, toss messages
			

	def streaming_orderbook(self): #generator
		self.ws_messages = []
		while True:
			if len(self.ws_messages) == 0:
				sleep(.1)
			else:
				yield self.ws_messages.pop()



