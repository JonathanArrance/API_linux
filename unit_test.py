import requests
import json

USERNAME='pi'
PASSWORD='DoopyJuice1!'
IP='192.168.1.56'

print "Running API Linux unit tests.\n\n"

print "Getting Token with valid credentials.\n"
try:
    r = requests.get('http://'+IP+':10500/api/1.0/token', auth=requests.auth.HTTPBasicAuth(USERNAME, PASSWORD))
    out = r.raise_for_status()
    if(out != None):
        raise Exception(out)

    token = json.loads(r.text)
    print 'PASS: Token ' + json.loads(r.text) + '\n'
except Exception as e:
    print 'FAIL'

print "Getting Token with invalid credentials.\n"
try:
    r = requests.get('http://'+IP+':10500/api/1.0/token', auth=requests.auth.HTTPBasicAuth(USERNAME, 'password'))
    out = r.raise_for_status()
    if(out != None):
        raise Exception(out)
    print 'PASS: Token coiuld not be obtained with invalid credentials.\n'
except Exception:
    token = json.loads(r.text)
    print 'FAIL: '+ token + '\n'

"""
#send a reading
#curl -i -X POST -H "Content-Type: application/json" -d '{"username":"paul","password":"python"}' -k https://192.168.10.9:8443/api/users
headers = {"content-type":"application/json;charset=UTF-8","X-Auth-Token":str(token['token'])}

print "Sending a new reading to the backend API"
data = "{'reading':'65','reading_type':'temp','sensor_serial':'67676767','reading_unit':'celcious'}"
r = requests.post('http://192.168.1.56:9443/api/1.0/reading', headers=headers, data=data)
out = r.raise_for_status()
if(out != None):
    raise Exception(out)

print 'Get the backend token'
print json.loads(r.text)
"""