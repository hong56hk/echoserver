import socket
import signal
import sys

class Server:
  def __init__(self, protocol:str, host:str, port:int):
    self.buffer_size = 1024
    self.protocol = protocol
    self.host = host
    self.port = port

    self.tcp_sock = None
    self.udp_sock = None

  
  ## -------------- process input from client and return the processed msg
  def process_msg(self, msg):
    resp = ""
    for i in range(len(msg)):
      c = msg[i]
      if i%2 == 0:
        resp += c.upper()
      else:
        resp += c
    return resp

  ## -------------- close
  def close(self):
    if self.tcp_sock:
      self.tcp_sock.close()

  ## -------------- init server socket
  def start(self):
    if self.protocol == "tcp":
      self.startTCPServer()
    elif self.protocol == "udp":
      self.startUDPServer()
    else:
      print("unknown protocol")
  
  ## -------------- init TCP server socket
  def startTCPServer(self):
    try:
      self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
      self.tcp_sock.bind((self.host, self.port))
      self.tcp_sock.listen(1)
    except Exception as e:
      print("cannot create server socket")
      print(e)
      return 

    while True:
      print("waiting for client to come...")
      conn, addr = self.tcp_sock.accept()
      print('connected by {}'.format(addr))
      while True:
        try:
          data = conn.recv(self.buffer_size)
          if len(data) == 0:
            print("{} disconnected".addr)
            break
          msg = data.decode()
          print("{} sent msg: {}".format(addr[0], msg))
          if msg == "bye":
            print("{} left".format(addr))
            break
          
          resp_msg = self.process_msg(msg)
          conn.sendall(resp_msg.encode())
        except Exception as e:
          print("{} disconnected".format(addr))
          break
      conn.close()
  
  ## -------------- init UDP server socket
  def startUDPServer(self):
    try:
      self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.udp_sock.bind((self.host, self.port))
    except Exception as e:
      print("cannot create server socket")
      print(e)
      return

    while True:
      try:
        data, addr = self.udp_sock.recvfrom(self.buffer_size)
        msg = data.decode()
        print("{} sent msg: {}".format(addr[0], msg))

        if msg != "bye":
          resp_msg = self.process_msg(msg)
          self.udp_sock.sendto(resp_msg.encode(), addr)
      except Exception as e:
        print("error when receiving msg: {}".format(e))


  

if __name__ == "__main__":
  server = None
  protocol = None
  host = socket.gethostbyname(socket.gethostname())
  port = 3120

  def signal_handler(sig, frame):
    print("\nbye")
    if server:
      server.close()
    sys.exit(0)
  signal.signal(signal.SIGINT, signal_handler)  

  print("Welcome to ELEC3120 programming assignment")
  while True:
    protocol = input("Please select server protocol to be used (tcp/udp): ")
    if protocol == "tcp" or protocol == "udp":
      break
    else:
      print("incorrect protocol selected")
  

  user_input = input("Please enter server listening ip default {}: ".format(host))
  if user_input != None and len(user_input) > 0:
    host = user_input
  
  while True:
    try:
      user_input = input("Please enter server listening port default {}: ".format(port))
      if user_input == None or len(user_input) == 0:
        break # use default
      elif user_input.isdigit():
        port = int(user_input)
        print("using port {}:".format(port))
        break
      else:
        print("invalid port number")
    except Exception as e:
      print("incorrect port number")

  server = Server(protocol, host, int(port))
  server.start()

