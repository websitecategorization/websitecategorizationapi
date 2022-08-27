# Website Classification API

Python3 client library for Website Classification service. 

Website classification API s a python library that allows to classify websites based on IAB and E-commerce taxonomies. 

## Installation 
```
pip install websiteclassificationapi
```
## Requirements

Only Python 3 is supported. You need an API key which you can obtain at www.websitecategorizationapi.com. 
Python library requires only requests package. 

## Documentation 

More detailed API documentation is available here: https://www.websitecategorizationapi.com/api.php

## Examples 

```
import categorization

api_key = 'enter_your_API_key' # you can get API key from www.websitecategorizationapi.com
url = 'www.alpha-quantum.com' # can be set to any valid URL
classifier_type = 'iab1' # should be set to either iab1 (Tier 1 categorization) or iab2 (Tier 2 categorization) for general websites or ecommerce1, ecommerce2 and ecommerce3 for E-commerce or product websites

# calling the API
print(categorization.get_categorization(url,api_key,classifier_type))
```


