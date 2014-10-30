import requests
import calendar
from datetime import datetime

class Magicseaweed(object):

    api_url = ''
    
    def __init__(self, api_key):
        base_url = 'http://magicseaweed.com/api/{0}/forecast'
        self.api_url = base_url.format(api_key)

    def get_forecast(self, spot_id, utc_datetime=None):
        """ Makes requests to magicseaweed's forecast API and returns
        a dictionary with the results.
        """
        # The timestamp specifies YYYYMMDD, and it this wrapper's job to
        # return the most approximate forecast
        response = requests.get('{0}?spot_id={1}'.format(self.api_url, spot_id))
        if utc_datetime:
            utc_timestamp = str(calendar.gmtime(utc_datetime.utc_timetuple()))
            for timeframe in response:
                return timeframe if timeframe['timestamp'] == utc_timestamp
        return response.json()

