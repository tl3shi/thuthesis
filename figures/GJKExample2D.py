def dotVec(q, d):
    return q[0]*d[0]+q[1]*d[1]

def support1(quad, d):
    maxDot = ()
    dot = -1e10
    for q in quad:
        t = dotVec(q, d)
        if t>dot:
            maxDot = q
            dot = t
    return maxDot
def support2(A, B, d):
    a = support1(A, d)
    md = (-d[0], -d[1])
    b = support1(B, md)
    print str(a) + '-' + str(b)
    return (a[0]-b[0], a[1] - b[1])

def scaleVec(r, vec):
    return (r*vec[0], r * vec[1])
def addVec(a, b):
    return (a[0]+b[0], a[1] + b[1])
def minVec(a, b):
    return (a[0]-b[0], a[1] - b[1])

def tripProduct(A, B, C):
    return addVec(scaleVec(-dotVec(C,B), A), scaleVec(dotVec(C, A), B))

quad = [(-4, 2), (-2.5, 2), (-2.5, 3.5), (-4, 3.5)]
tri = [(-3, 1), (-1,3), (-3, 3)]
diff = []
for q in quad:
    for t in tri:
        diff += [(q[0]-t[0], q[1]-t[1])]
#print set(diff)

d = (5, -8.75)

quad = [(-4, 2), (-2.5, 2), (-2.5, 3.5), (-4, 3.5)]
tri1 = [(-3, 1), (-1,3), (-1, 1)]

print support2(quad, tri1, (6, -6))
print support2(quad, tri1, d)
exit()
print support2(quad, tri1, (0.5, -1))

d3=(-1.5, -1)
d2=(-3, -1)
d1=(0.5, 1)

print tripProduct(minVec(d2,d3), minVec(d1, d3), minVec(d2,d3))
print tripProduct(minVec(d1,d3), minVec(d2, d3), minVec(d1,d3))

d3=(.5, -1)
d2=(-3, -1)
d1=(0.5, 1)

print tripProduct(minVec(d1,d3), minVec(d2, d3), minVec(d1,d3))
print tripProduct(minVec(d2,d3), minVec(d1, d3), minVec(d2,d3))


