#!/usr/bin/python
import api_lib as al
import sys

#api version
API_VERSION='1.0'

@al.auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = al.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = mongo_lib.Account.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@al.app.route('/api/'+API_VERSION+'/token')
@al.auth.login_required
def get_auth_token():
    req_data = request.get_json()
    token = g.user.generate_auth_token(req_data['username'],req_data['password'],3600)
    return jsonify({'token': token.decode('ascii'), 'duration': 3600})
"""
@al.app.route('/api/'+API_VERSION+'/resource')
@al.auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user})
"""  
if __name__ == '__main__':
    al.app.run(host='0.0.0.0',port=10500, debug=True,ssl_context='adhoc')