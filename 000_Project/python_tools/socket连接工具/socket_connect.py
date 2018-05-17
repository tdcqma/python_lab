import sys
import socket

"""
 usage: python3 socket_connect.py host port'
"""

dhost = sys.argv[1]
dport = int(sys.argv[2])
print('\n扫描服务器：Host:%s,Port:%d\n' % (dhost,dport))

# 建立socket连接
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((dhost,dport))
print('socket connect successful!')

# 尝试发送payload
data = 'CVE-2018-****测试'.encode(encoding="utf-8")
while data:
	s.sendall(data)
	print('payload send successful!')
	data = s.recv(1024)
	print('\n%s:%d => recv length:%s, \nrecv info:：' % (dhost,dport,len(data)) )
	print(data.decode('utf-8'))

s.close()
