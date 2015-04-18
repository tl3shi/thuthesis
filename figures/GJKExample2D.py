quad = [(-4, 2), (-2.5, 2), (-2.5, 3.5), (-4, 3.5)]
tri = [(-3, 1), (-1,3), (-3, 3)]
diff = []
for q in quad:
    for t in tri:
        diff += [(q[0]-t[0], q[1]-t[1])]
#print set(diff)

dot = -1e10
d = (5, -8.75)
maxDot = ()
for q in quad:
    t = q[0]*d[0]+q[1]*d[1]
    print (t, q)
    if t>dot:
        maxDot = q
        dot = t
print maxDot
d = (-d[0], -d[1])
dot = -1e10
for q in tri:
    t = q[0]*d[0]+q[1]*d[1]
    print (t, q)
    if t>dot:
        maxDot = q
        dot = t
print maxDot

print 'hello world\n'

quad = [(-4, 2), (-2.5, 2), (-2.5, 3.5), (-4, 3.5)]
tri = [(-3, 1), (-1,3), (-1, 1)]
diff = []
for q in quad:
    for t in tri:
        diff += [(q[0]-t[0], q[1]-t[1])]
print set(diff)

#d = (-d[0], -d[1])
dot = -1e10
for q in tri:
    t = q[0]*d[0]+q[1]*d[1]
    print (t, q)
    if t>dot:
        maxDot = q
        dot = t
print maxDot


