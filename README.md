# API_linux

API_linux is a light weight process that will allow a user to execute commands on a target linux system using a REST API endpoint.

## Login
--------

```
Get a token
curl -u username:password -k -i https://mylinuxhost/login
```

## Execute Command
------------------

```
Use a token to login to the host and execute a command with flags.

ex. # ls -al
    # curl -u TOKEN:x -k -i https://mylinuxhost/command -d {'command':'ls','flags':['-a','-l']}

or

Use a token to login and execute a command with arguments

ex. # command --flag1 arg --flag2 arg 
    # curl -u TOKEN:x -k -i https://mylinuxhost/command -d {'command':'linux_command','flags':{'flag1':'arg','flag2':'arg'}}
```

## Install
----------
### Git
```
# git clone https://github.com/JonathanArrance/API_linux.git

# cd apilinux

# python apilinux
```

### PIP
```
# pip install api-linux
```
