"""
Example for using Python wrapper for website categorization API (from www.websitecategorizationapi.com). 

You can get API key from www.websitecategorizationapi.com. 

Explanation of available classifiers: 

Classifier_type should be set to either iab1 (Tier 1 categorization) or iab2 (Tier 2 categorization) for general websites or ecommerce1, ecommerce2 and ecommerce3 for E-commerce or product websites. 

IAB Tier 1 categorization returns probabilities of text being classified as one of 29 possible categories.

IAB Tier 2 categorization returns probabilities of text being classified as one of 447 possible categories.

Ecommerce Tier 1 categorization returns probabilities of text being classified as one of 21 possible categories.

Ecommerce Tier 2 website categorization returns probabilities of text being classified as one of 182 possible categories.

Ecommerce Tier 3 website categorization returns probabilities of text being classified as one of 1113 possible categories.
"""

from websiteclassificationapi import websiteclassificationapi

api_key = 'h2XurA2Rw' # you can get API key from www.websitecategorizationapi.com
url = 'www.alpha-quantum.com' # can be set to any valid URL
classifier_type = 'iab1' # should be set to either iab1 (Tier 1 categorization) or iab2 (Tier 2 categorization) for general websites or ecommerce1, ecommerce2 and ecommerce3 for E-commerce or product websites

# calling the API
print(websiteclassificationapi.get_categorization(url,api_key,classifier_type))