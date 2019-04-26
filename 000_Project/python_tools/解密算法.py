import hashlib,urllib

hl = hashlib.md5()
a=open('input2.txt').read()
arr=a.split("&")[0:-1]
arr=sorted(arr)
s="".join(arr)+"jabk.pinaagaddn.com"

hl.update(s.encode(encoding='utf-8'))
print('--->',hl.hexdigest())