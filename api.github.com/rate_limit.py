import json
from requests import get

json = get("https://api.github.com/rate_limit").json()
print(str(json))
