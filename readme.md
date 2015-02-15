# Coinbase Exchange
The un-official Python library for the [Coinbase Exchange
API](https://docs.exchange.coinbase.com/).

*Note: this library may be subtly broken or buggy. The code is released under
the MIT License – please take the following message to heart:*

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
*

## In Active Development
* Public facing (non-authenticated) API completed
* Private facing (authenticated) API unstarted

## Quick Start

### The Public API Client
The Coinbase Exchange API has both public and private endpoints. If you're only
interested in the public endpoints, you should use a `PublicClient`.

```python
from cbe import CoinbaseExchange
cbe = CoinbaseExchange()
```

#### Public API Methods

* [`getProducts`](https://docs.exchange.coinbase.com/#get-products)
```cbe.getProducts()```

* [`getProductOrderBook`](https://docs.exchange.coinbase.com/#get-product-order-book)
```
cbe.getProductOrderBook() #defaults level=1
cbe.getProductOrderBook(level=3)
```

* [`getProductTicker`](https://docs.exchange.coinbase.com/#get-product-ticker)
```cbe.getProductTicker()```

* [`getProductTrades`](https://docs.exchange.coinbase.com/#get-trades)
```cbe.getProductTrades()```

* [`getProductHistoricRates`](https://docs.exchange.coinbase.com/#get-historic-rates)
```cbe.getProductHistoricRates()```

* [`getProduct24HrStats`](https://docs.exchange.coinbase.com/#get-24hr-stats)
```cbe.getProduct24HrStats()```

* [`getCurrencies`](https://docs.exchange.coinbase.com/#get-currencies)
```cbe.getCurrencies()```

* [`getTime`](https://docs.exchange.coinbase.com/#time)
```cbe.getTime()```
