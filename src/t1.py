

d=['ab',['cd','ef']]
w=d[0]
p=d[1]

z=[w]+[_ for _ in p]

zz=''.join(z)

print (z)
print (zz)
