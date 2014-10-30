import requests
import calendar
from datetime import datetime

class Magicseaweed(object):

    api_url = ''
    
    def __init__(self, api_key):
        base_url = 'http://magicseaweed.com/api/{0}/forecast'
        self.api_url = base_url.format(api_key)

    def timestamp_from_datetime(dt):
        """ Returns an UNIX timestamp as int given a datetime instance. """
        return str(calendar.gmtime(dt.utc_timetuple()))

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
        If datetime.datetime(2014, 10, 30 10, 0, 0) is passed as argument,
        this function returns datetime.datetime(2014, 10, 30 12, 0, 0)

        """
        if dt.hour % 3 != 0:
            rounded = dt.hour
            while rounded % 3 != 0:
                rounded +=1
            return datetime(dt.year, dt.month, dt.day, rounded, 0, 0)
        return datetime(dt.year, dt.month, dt.day, dt.hour, 0, 0)

    def get_forecast(self, spot_id):
        """ Makes requests to magicseaweed's forecast API and returns
        a dictionary with the results.
        """
        response = requests.get('{0}?spot_id={1}'.format(self.api_url, spot_id))
        # if utc_datetime:
        #     date = utc_datetime.date
        #     utc_timestamp = 1
        #     for timeframe in response:
        #         return timeframe if timeframe['timestamp'] == utc_timestamp
        return response.json()

