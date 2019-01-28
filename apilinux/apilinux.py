#!/usr/bin/python
import eve
import sys
import pam

def linux_login(username=None,password=None):
    """
    Desc: Use the Linux PAM system to authenticate a user against the sytem.
    Input: username - valid linux user name
              password - valid password for the linux user account
    Output: True
                 ERROR
    Note: if the user is not  a valid linux user then authintication will fail.
    """
    if (username=None or password=None):
        return 'ERROR: Account username or password not given'

    p = pam.pam()
    out = p.authenticate(username,password)
    
    if(out == False):
        return 'ERROR: Account not authorized.'

    return out


def token():
    """
    Desc: Get a token if the user is a vsalid Linux system user.
    Input: None
    Output: Valid auth token
    Error: 400
    Note: 
    """

def run_command():
    pass

def run()
    #check if the credentials passed in are valid system credentials
    
    

if  __name__ == '__main__':
    run()