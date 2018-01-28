import sys
import requests

url="https://github1.com"

try:
    responce = requests.get(url, timeout = 30)
    # несуществующий адрес-> генерация HTTPError
    responce.raise_for_status()
except requests.Timeout:
    print("Timeout error, url:", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print(f"err url: {url}, code:{code}")
except requests.RequestException:
    print("err of BaseClass")
else:
    print(responce.content)