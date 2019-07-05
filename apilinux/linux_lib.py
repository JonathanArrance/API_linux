#!/bin/python
import subprocess
import pam
import pwd
import pprint

#settings file
import settings

from flask import Flask, abort, request, jsonify, g
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

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
        #Build up the command to run
        #1. Command should be lower case
        #2. if PATH1 and PATH2 are not specified local path should be used
        #3. flags should be input as an array if multiple flags are present
            #should be ignored if no flags present
            #should be able to run any sort of flag
        
        out = None
        args = []
        try:
            string = input_dict['command'].encode("utf-8")
            args.append(str(string).lower())
        except Exception:
            abort(400)
        
        #clean up the flags
        if 'flags' in input_dict:
            try:
                flag_string = input_dict['flags'].encode("utf-8")
                flags = flag_string.split(',')
                args = args + flags
            except:
                abort(400)

        if 'path' in input_dict and input_dict['path'] != '':
            try:
                args.append(str(input_dict['path'].encode("utf-8")))
            except:
                abort(400)

        if 'path' not in input_dict or input_dict['path'] == '':
            if ('path1' in input_dict and input_dict['path1'] != ''):
                args.append(str(input_dict['path1'].encode("utf-8")))
                if ('path2' in input_dict and input_dict['path2'] != ''):
                    args.append(str(input_dict['path2'].encode("utf-8")))
        try:
            out = subprocess.Popen(args, stdout=subprocess.PIPE)
            # Run the command
            output = out.communicate()[0]
        except Exception as e:
            abort(400)
            
        
        return (jsonify(output),200)