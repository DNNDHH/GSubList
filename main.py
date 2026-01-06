import requests
import json
import os

requests.urllib3.disable_warnings()
session = requests.Session()
session.verify = False

def NewSession():
    return requests.Session()

s = NewSession()


url_A = os.environ.get('URL_A')
headers_A = os.environ.get('HEADERS_A')
headers1 = headers_A
res = s.get(url_A, headers=headers1, verify=False)
_csrf = s.cookies.get("_csrf")
print("1")


info = os.environ.get('INFO')
payload = f"_csrf={_csrf}&{info}"
headers_B = os.environ.get('HEADERS_B')
headers2 = headers_B
res2 = s.post(url_A, data=payload, headers=headers2, verify=False)
print("2")


url_B = os.environ.get('URL_B')
headers_C = os.environ.get('HEADERS_C')
headers3 = headers_C
response3 = s.get(url_B, headers=headers3, verify=False)
print("3")


url_C = os.environ.get('URL_C')
headers_D = os.environ.get('HEADERS_D')
headers4 = headers_D
res = s.get(url_C, headers=headers4, verify=False)
data = res.json()

with open("update.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
