import urllib.request
import urllib.parse
import json, time

def checkToast():
    url = 'https://2bnfr1wcth.execute-api.us-west-2.amazonaws.com/Prod/totoastornottotoast'
    req = urllib.request.Request(url)
    # Customize the default User-Agent header value:
    req.add_header('x-api-key', 'Id4gLtG4vt7lC94nTMCKP40kk9Aha25Q4e5VfFaI')
    req.add_header('Content-type', 'application/json')
    r = urllib.request.urlopen(req)
    json_str = json.loads(r.read().decode('UTF-8'))
    print(json_str['loadSide'])
    print(json_str['sendEmail'])

while True:
    checkToast()
    time.sleep(5)