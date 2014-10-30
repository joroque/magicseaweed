import os
import unittest

class MagicseaweedTestCase(unittest.TestCase):

    # export environment variable MSW_KEY=<MSW_KEY> to run this tests
    msw = Magicseaweed(os.environ['MSW_KEY'])

    def test_get_forecast(self):
        """ Charts URLs are the only piece of data that won't change. """
        forecast = self.msw.get_forecast(920)
        swell_chart_url = forecast[0]['charts']['swell']
        # A well-formed url:
        # http://hist-5.msw.ms/wave/750/1-1415048400-1.gif
        self.assertIn('wave', swell_chart_url)

    def test_get_forecast_with_utc(self):
        forecast = self.msw.get_forecast(920, utc_timestamp=datetime.utcnow())
        self.assertEqual(len(forecast), 1)
        
if __name__ == '__main__':
    unittest.main()
