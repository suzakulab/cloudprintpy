# CloudPrint.py

Simple wrapper of Google Cloudprint API for python

## Install

`pip install git+https://github.com/suzakulab/cloudprintpy`

## Usage

see examples or below.


```python
from google.oauth2 import service_account
import cloudprint

credentials = service_account.Credentials.from_service_account_file("account-xxxxxxx.json")

client = cloudprint.Client(credentials)

# do something with client
```


## Author

theoldmoon0602
