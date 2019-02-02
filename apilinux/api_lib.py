from flask import Flask, abort, request, jsonify, g, url_for
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
import sys
import pam

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
auth = HTTPBasicAuth()

def linux_login(username=None,password=None):
    """
    Desc: Use the Linux PAM system to authenticate a user against the sytem.
    Input: username - valid linux user name
              password - valid password for the linux user account
    Output: True
                 ERROR
    Note: if the user is not  a valid linux user then authintication will fail.
    """
    if (username==None or password==None):
        return 'ERROR: Account username or password not given'

    p = pam.pam()
    out = p.authenticate(username,password)
    
    if(out == False):
        return 'ERROR: Account not authorized.'

    return out


def generate_auth_token(username=None,password=None,expires=None):
    """
    Desc: Get a token if the user is a vsalid Linux system user.
    Input: None
    Output: Valid auth token
    Error: 400
    Note: 
    """    login = linux_login(username,pasword)    if (login == False):        abort(400)    s = Serializer(app.config['SECRET_KEY'], expires_in=expires)    return s.dumps()    
@staticmethoddef verify_auth_token(token=None,username=None,password=None):    if token == None:        abort(400)    s = Serializer(app.config['SECRET_KEY'])        try:        data = s.loads(token)    except SignatureExpired as e:        return None    # valid token, but expired    except BadSignature as f:        return None   # invalid token        #user = mongo.db.Account.find_one({'userid':data['userid']})    user = linux_login(username,password)        return user 

def run_command():
    pass
