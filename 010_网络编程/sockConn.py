import sys
import socket

dhost = sys.argv[1]
dport = int(sys.argv[2])
print('HOST:%s,PORT:%d' % (dhost,dport))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((dhost,dport))
msg = s.recv(1024)
s.close()

print(msg.decode('utf-8'))
