# API_linux

API_linux is a light weight process that will allow a user to execute commands on a target linux system using a REST API endpoint.

## Login
--------
The user account must exist on the target Linux system.

```
Get a token
curl -u username:password -k -i https://mylinuxhost/login
```

## Execute Command
------------------

```
Use a token to login to the host and execute a command with flags.

ex. # ps -ef 
    # curl -u TOKEN:x -i -k -X POST https://192.168.1.64:10500/api/1.0/command -H "Content-Type: application/json" -d '{"command":"ps","flags":"-ef"}'

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
