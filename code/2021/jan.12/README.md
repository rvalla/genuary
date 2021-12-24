![icon](https://gitlab.com/azarte/genuary/-/raw/themoststable/public/assets/img/logo_64.png)

# Stock Art

The January 12th prompt was about using an API. I decided to use data from the stock market through
[Alpha Vantage API](https://www.alphavantage.co/). You need a free *api key* to use it. The code use
*Matplotlib* library and take advantage of its colormaps.  

![stockart](https://gitlab.com/azarte/genuary/-/raw/themoststable/code/2021/assets/img/stockart.jpg)

## configure your stock art

If you have an *api key* from [Alpha Vantage API](https://www.alphavantage.co/) you can make your own
stock art. You simply need to run an instance of StockArt:  

```python
from stockart import StockArt

#Alpha Vantage API key
key = 'youralphavantagekey'

#Producing your piece of stock art
sa = StockArt("config/your.json", key)
```
You can configure your art using the *.json* file:

```json
{
	"outPath": "relativeoutputfolder/",
	"outFile": "outputfilename",
	"width": 16,
	"height": 9,
	"resolution": 150,
	"symbols": "tickers,separated,by,comas",
	"VolumeDiv": 20000,
	"startDate": "2020-12-31",
	"endDate": "2020-01-01",
	"colormap": "frommatplotlibcolormaps",
	"background": "red,green,blue"
}
```

Feel free to contact me by [mail](mailto:rodrigovalla@protonmail.ch) or reach me in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).
