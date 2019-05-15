import hashlib

m = hashlib.md5()
l_str ='"membership_id":1,"openId":"oQDU443O6GkUhOjapRutP0Esv-vY","user_id":12,"paymentCalculation":null'


m.update(l_str.encode('utf-8'))
print(m.hexdigest())