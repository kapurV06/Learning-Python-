x = [1,2,3,4]
y = [1,2,3,4]
z = ['a','b','c','d']

for a,b,c in zip(x,y,z):
    print(a,b,c)
#zip shall create an object
print(zip(x,y,z))
#convert zip to a list
print(list(zip(x,y,z)))
#dict
d = dict(list(zip(x,y)))
print(d)