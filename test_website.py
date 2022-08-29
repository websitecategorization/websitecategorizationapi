import unittest

from websiteclassificationapi import websiteclassificationapi

api_key = 'h2XurA2' # you can get API key from www.websitecategorizationapi.com
url = 'www.alpha-quantum.com' # can be set to any valid URL
classifier_type = 'iab1' # should be set to either iab1 (Tier 1 categorization) or iab2 (Tier 2 categorization) for general websites or ecommerce1, ecommerce2 and ecommerce3 for E-commerce or product websites


class Test(unittest.TestCase):
    def test_method(self):
        self.assertEqual(websiteclassificationapi.get_categorization(url,api_key,classifier_type), "Technology & Consulting")

