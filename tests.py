import os
import unittest
from datetime import datetime

from magicseaweed import Magicseaweed

class MagicseaweedTestCase(unittest.TestCase):

    # Export environment variable MSW_KEY=<MSW_KEY> to run this tests
    msw = Magicseaweed(os.environ['MSW_KEY'])

    def test_get_forecast(self):
        """ Charts URLs are the only piece of data that won't change. """
        forecast = self.msw.get_forecast(920)
        swell_chart_url = forecast[0]['charts']['swell']
        # A well-formed url:
        # http://hist-5.msw.ms/wave/750/1-1415048400-1.gif
        self.assertIn('wave', swell_chart_url)

    def test_get_forecast_with_datetime(self):
         forecast = self.msw.get_forecast(920, local_datetime=datetime.utcnow())
         self.assertIsNotNone(forecast['localTimestamp'])

    def test_round_timeframe(self):
        dt = datetime(2014, 10, 30, 7, 30, 0) # 2014-10-30 7:30:00
        result = self.msw.round_timeframe(dt)
        self.assertEqual(result.hour, 9)
        dt = datetime(2014, 10, 30, 15, 30, 0) # 2014-10-30 15:30:00
        result = self.msw.round_timeframe(dt)
        self.assertEqual(result.hour, 15)

    def test_units(self):
        """ Test measurement units
        Query the API using EU units (m, kph, c), this is the default.
        Then query the API again using the same spot_id, but this time using
        US units (ft, mph, f). Speed magnitudes are greater in kph than in mph.
        """
        forecast_eu = self.msw.get_forecast(920,
                                            local_datetime=datetime.utcnow())
        forecast_us = self.msw.get_forecast(920,
                                            local_datetime=datetime.utcnow(),
                                            units='us')
        speed_kph = forecast_eu['wind']['speed']
        speed_mph = forecast_us['wind']['speed']
        self.assertGreater(speed_kph, speed_mph)
        
        
if __name__ == '__main__':
    unittest.main()
