# Echo server and Echo client, single client version
The idea of the server and client is taken from ELEC3120 programming assignment.

*Echo Server*
In the first part of this assignment you are going to implement an echo server which receives text message from client and sends it back to the client. (That’s why we call it echo server) When the server receives the text message from client, it capitalizes the odd characters of the text message. For example, when the client sends a text message of “hello elec 3120 student”, the server should return a text message of “HeLlO ElEc 3120 StUdEnT”.
Detailed requirements:
1. Implement the server in both TCP and UDP and allow the user to choose which protocol to use atruntime.
2. For TCP programming, your program should be a persistent server so that after transmitting each packet, the TCP
connection should be kept alive.
3. The server only needs to serve one client at a time (no multithreading).
4. When the server receives a message from the client, print it out on the screen with the client’s IP address on the server
side.
5. After printing the message on the screen, the server capitalizes the odd characters of the message and sends the modified
version back to the client.
6. When a client disconnects, the server closes the socket and waits for the next client to connect.

*Echo Client*
In the second part of this assignment you are going to implement an echo client which connects and sends plain text messages to an echo server. Moreover, when it receives message from the echo server, it directly prints the message out on the screen.
Detailed requirements:
1. Implement the client in both TCP and UDP and allow the user to choose which protocol to use atruntime.
2. For TCP programming, your program should be “persistent”, so that after each packet’s transmission, the TCP connection
should be kept alive.
3. The client only connects to one echo server at a time (no multithreading).
4. Users input messages using the keyboard, and the client transmits messages to the connected server.
5. When a message is received from the server, print it out on the screen on the client side.
6. When a user types “bye”, the client program closes all connections and quits.
7. Handle common errors in socket programming (e.g., assigned port being occupied by other programs, client resetting the
connections).

# Server
## Runtime
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

*Gracefully disconnect*
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

## Runtime
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
