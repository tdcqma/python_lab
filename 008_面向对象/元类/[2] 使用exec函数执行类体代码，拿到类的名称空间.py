g = {
    'x':1,
    'y':2
}

l = {}

exec('''
global x,z
x=100
z=200

m=300
''',g,l)

print(g)
print('-'*40)
print(l)
