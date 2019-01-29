# API_linux

API_linux is a light weight process that will allow a user to execute commands on a target linux system using a REST API endpoint.

## Login
--------

```
Get a token
curl -u username:password -k -i https://mylinuxhost/login

Use the token to login to execute a command with flags
```

## Execute Command
------------------

```
ex. # ls -al
    # curl -u TOKEN:x -k -i https://mylinuxhost/command -d {'command':'ls','flags':['-a','-l']}

or

Use a token to login and execute a command with options

ex. # command --flag1 arg --flag2 arg 
    # curl -u TOKEN:x -k -i https://mylinuxhost/command -d {'command':'linux_command','flags':{'flag1':'arg','flag2':'arg'}}

```
