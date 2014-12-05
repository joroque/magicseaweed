Magicseaweed
============

Python wrapper for [Magicseaweed](http://magicseaweed.com/developer/forecast-api) marine forecasting API.

## Usage

All result sets are Python dictionaries. Keys are listed in the [API documentation](http://magicseaweed.com/developer/forecast-api).

```python
msw = Magicseaweed(api_key)
forecast = msw.get_forecast(spot_id)
forecast['swell']['minBreakingHeight'] # 1.06
```

Magicseaweed provides 40 forecasts separated by 3-hour intervals (e.g. 00:00, 03:00, 06:00 ... 21:00). By default you'll get a list of dictionaries where each index is the forecast for a particular timeframe.

You can also get the forecast for an specific timeframe by passing a ```dateime.datetime``` object.

```python
timeframe = datetime.datetime.utcnow()
msw.get_forecast(spot_id, local_datetime=timeframe)
```

If there's no forecast for the ```datetime.datetime``` object you pass as argument, this wrapper will round ```datetime.datetime``` to the closest available forecast. For instance, if you ask for the forecast for 10:00 (not available) you'll get the one for 12:00 (available).

### Measurement Units

By default, European units are used (m, kph, c). You can use choose among 3 different sets of measurement units:

- uk (ft, mph, c)
- us (ft, mph, f)
- eu (m, kph, c)

```python
forecast = msw.get_forecast(spot_id, units='us')
```

Thank [Garret](https://github.com/gsquire) for this addition.


## License

Copyright © 2014 Jorge Romero. Released under The MIT License.

