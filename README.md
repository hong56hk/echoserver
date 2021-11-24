# ELEC3120
Programming assignmment

# Server
## runtime
The server is based on python 3.9.1 to develop.

## Usage
To start the server `python3 server.py`
To stop the server, you may press `Ctrl + C`

## Interface 

*Settings*

After the server starts, it prints below message then a series of questions will be asked
```
Welcome to ELEC3120 programming assignment
Please select server protocol to be used (tcp/udp): tcp
Please enter server listening ip default 127.0.0.1: 
Please enter server listening port default 3120: 
waiting for client to come...
```
The user has to first enter `tcp` to select TCP as the server protocol or `udp` as the server protocol.
Then the user can enter the host to be binded. If the user does not enter, a default hostanme will be used which may be `127.0.0.1` or the IP address of the server.

After setting the server, the server waits for client incoming.
The following message is printed
`waiting for client to come...`

*Incoming connection*
If a client comes, its IP address and port will be printed on screen like below:
```
connected by ('127.0.0.1', 50559)
```

All incoming messasges will be printed on screen
```
127.0.0.1 sent msg: Hello
127.0.0.1 sent msg: Hello world, I am client, Please respond me.
```

If the client disconnects or leaves, below messages will be printed and the server will wait for an other new client.

*disconnected*
```
('127.0.0.1', 50559) disconnected
waiting for client to come...
```

*Gracefull disconnect*
```
('127.0.0.1', 50559) left
waiting for client to come...
```
*Exit*

If the user enter `Ctrl + C`, the server will exit and below message will be printed
```
waiting for client to come...
^C
bye
```


# Client

## runtime
The server is based on python 3.9.1 to develop.

## Usage
To start the `python3 server.py`

## Interface

*Start*
```
$ python3 client.py
Welcome to ELEC3120 programming assignment
Please select protocol to be used (tcp/udp): tcp
Please enter server IP address, default 127.0.0.1: 
Please enter server port, default 3120: 
> 
```

The user has to select either TCP or UDP by entering `tcp` or `udp`.
If the user does not enter host or port, default value will be used

*Sending message*
```
> Hello World
received: HeLlO WoRlD
```

*Exit*

The user can either exit by entering `bye` or press `Ctrl + c`
```
> bye
```
