import socket
import signal
import sys


class Client:
  def __init__(self):
    self.buffer_size = 1024
    self.protocol = None
    self.host = None
    self.port = None

    self.sock = None
    self.running = True

  def initSocket(self, protocol, host, port):
    self.protocol = protocol
    self.host = host
    self.port = port

    if self.protocol == "tcp":
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.settimeout(10)
      try:
        self.sock.connect((self.host, self.port))
      except Exception as e:
        print("[error] {}".format(str(e)))
        print("please ensure entering correct ip and port")
        exit(0)
    elif self.protocol == "udp":
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  def onCloseSignal(sig, frame):
    print("asdadsasd")

  def close(self):
    self.running = False
    if self.sock:
      if self.protocol == "tcp":
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()
      # endif protocol

  def send(self, msg):
    if self.protocol == "tcp":
      self.sock.sendall(msg.encode())
    elif self.protocol == "udp":
      self.sock.sendto(msg.encode(), (self.host, self.port))
    

  def start(self):
    while self.running:
      user_input = input("> ")
      self.send(user_input)
      if user_input == "bye":
        self.close()
      else:
        data = self.sock.recv(self.buffer_size)
        print("received: {}".format(data.decode()))
    # end of running loop



if __name__ == "__main__":
  client = None
  def signal_handler(sig, frame):
    print("\nbye")
    if client:
      client.close()
    sys.exit(0)
    
  signal.signal(signal.SIGINT, signal_handler)  
    
  protocol = None
  host = socket.gethostbyname(socket.gethostname())
  port = 3120

  print("Welcome to ELEC3120 programming assignment")
  while True:
    protocol = input("Please select protocol to be used (tcp/udp): ")
    if protocol == "tcp" or protocol == "udp":
      break
    else:
      print("incorrect protocol selected")

  user_input = input("Please enter server IP address, default {}: ".format(host))
  if user_input != None and len(user_input) > 0:
    host = user_input
  
  while True:
    try:
      user_input = input("Please enter server port, default {}: ".format(port))
      if user_input == None or len(user_input) == 0:
        break # use default
      elif user_input.isdigit():
        port = int(user_input)
        break
      else:
        print("invalid port number")
    except Exception as e:
      print("incorrect port number")

  
  client = Client()
  client.initSocket(protocol, host, port)
  client.start()

  


