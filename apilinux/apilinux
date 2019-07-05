#!/usr/bin/env python
#all of this needs to be chnaged use as an example and guide
import os
import sys
import settings
import json
import linux_lib

from flask import request, jsonify, g

api = settings.API_VERSION
linux = linux_lib.Linux()

@linux_lib.auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = linux.verify_auth_token(username_or_token)
    if user is False:
        # try to authenticate with username/password
        user = linux.linux_login(username_or_token,password)
        if user is False:
            return False
   # g.user = user
    return True

#curl -u backend:rackbrain -i -k -X GET http://192.168.1.56:9443/api/1.0/token
@linux_lib.app.route('/api/'+api+'/token',methods=['GET'])
@linux_lib.auth.login_required
def get_auth_token():
    token = linux.generate_auth_token(3600)
    return jsonify({'token': token.decode('ascii'), 'duration': 3600})

@linux_lib.app.route('/api/'+api+'/alive',methods=['POST'])
def get_alive():
    return jsonify({'data': 'Linux api is alive.'})

#use lsblk and ls
@linux_lib.app.route('/api/'+api+'/command',methods=['POST'])
@linux_lib.auth.login_required
def run_command():
    req_data = request.get_json()
    return linux.run_linux_command(req_data)

if __name__ == '__main__':
    linux_lib.app.run(host='0.0.0.0',port=10500, debug=True,ssl_context='adhoc')
    #mongo_lib.app.run(host='0.0.0.0',port=10500, debug=True)