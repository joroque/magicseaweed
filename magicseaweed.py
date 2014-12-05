import calendar
import requests

from datetime import datetime, timedelta

class Magicseaweed(object):

    api_url = ''
    
    def __init__(self, api_key):
        base_url = 'http://magicseaweed.com/api/{0}/forecast'
        self.api_url = base_url.format(api_key)

    def timestamp_from_datetime(self, dt):
        """ Returns an UNIX timestamp as str given a datetime instance. """
        return calendar.timegm(dt.timetuple())

    def round_timeframe(self, dt):
        """ Returns the next available forecast timeframe as datetime.

        Magicseaweed provides 8 forecasts for a given day, as follows:
        1  00:00:00
        2  03:00:00
        3  06:00:00
        4  09:00:00
        5  12:00:00
        6  15:00:00
        7  18:00:00
        8  21:00:00

        Example:
        If datetime.datetime(2014, 10, 30, 10, 0, 0) is passed as argument,
        this function returns datetime.datetime(2014, 10, 30, 12, 0, 0).

        """
        while dt.hour % 3 != 0:
            dt = dt + timedelta(hours=1)
        return datetime(dt.year, dt.month, dt.day, dt.hour, 0, 0)

    def get_forecast(self, spot_id, units='eu', local_datetime=None):
        """ Makes requests to magicseaweed's forecast API. The default unit is
        European.
        """
        response = requests.get('{0}?spot_id={1}&units={2}'
                                .format(self.api_url, spot_id, units))

        if local_datetime is not None:
            try:
                local_datetime = self.round_timeframe(local_datetime)
            except:
                raise TypeError(
                        'local_datetime must be of type datetime.datetime')
            local_timestamp = self.timestamp_from_datetime(local_datetime)
            for forecast in response.json():
                if forecast['localTimestamp'] == local_timestamp:
                    return forecast
            return None
        return response.json()
