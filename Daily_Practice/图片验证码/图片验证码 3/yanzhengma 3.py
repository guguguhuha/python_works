import gvcode
s,v = gvcode.generate()
s.save('./%s.jpg' % v)
print(type(s))
print(v)
print(type(v))
