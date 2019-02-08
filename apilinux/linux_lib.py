#!/bin/python
import subprocess
import pam
import pwd

#settings file
import settings

from flask import Flask, abort, request, jsonify, g
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY

auth = HTTPBasicAuth()

class Linux():

    def linux_login(self,username,password):   
        if (username==None or password==None):
            return False
        p = pam.pam()
        out = p.authenticate(username,password)
        if(out == False):
            return False
        else:
            self.uid = pwd.getpwnam(username).pw_uid
        
        self.out = {'exist':True,'uid':self.uid}
        
        return self.out

    def generate_auth_token(self,expiration):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps(self.out)
    
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired as e:
            return False    # valid token, but expired
        except BadSignature as f:
            return False   # invalid token
        except:
            return False
    
        if data['exist'] is False:
            return False
    
        return True
    
        
    @staticmethod
    def run_linux_command(input_dict):
        if input_dict['command'] == None:
            abort(400)
        
        if command not in input_dict:
            abort(400)
            
        out = None
        args = []
    
        if input_dict['flags'] == None:
            args.append(command)
            out = subprocess.Popen(args, stdout=subprocess.PIPE)
            
        if isinstance(list, input_dict['flags']):
            args.append(command)
            args = args + flags
            out = subprocess.Popen(args, stdout=subprocess.PIPE)
            
        if isinstance(dict,input_dict['flags']):
            args.append(command)
            for k,v in input_dict['flags'].iteritems():
                args.append(k)
                args.append(v)
            out = subprocess.Popen(args, stdout=subprocess.PIPE)
        
        output, err = out.communicate()
        return {'output':output,'error':err}