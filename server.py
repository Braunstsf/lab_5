#TODO: Students will fill this file
# Name: Medha Nalamada, Ethan Wen
# EIDs: mrn789, ew22955
import threading
import socket
import sys

class Server:
  # initialize the UDP server socket
  def __init__(self, server_addr, backlog=10):
      # TODO: Implement this method
      self.backlog = backlog
      self.server_addr = server_addr
      # TODO: Create a UDP socket here (socket.SOCK_DGRAM)
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      # TODO: set the socket to reuse the address
      self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  def serve(self):
      # TODO: Implement this method

      # TODO: bind the socket to the server address
      self.sock.bind(self.server_addr)
      
      while True:
          # TODO: Receive data from the client
          data, client_addr = self.sock.recvfrom(2048)
          # TODO: Echo the message back to the client
          self.sock.sendto(data, client_addr)
          break
          print('Still continuing....')

      # TODO: close the socket
      self.sock.close()
      print("Closing the socket")

# To be called inside a Process
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python server-python.py [Server Address] [Server Port]")

    serv_addr = sys.argv[1]
    serv_port = int(sys.argv[2])

    server = Server((serv_addr, serv_port))
    server.serve()
