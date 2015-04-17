quad = [(-4, 2), (-2.5, 2), (-2.5, 3.5), (-4, 3.5)]
tri = [(-3, 1), (-1,3), (-3, 3)]
diff = []
for q in quad:
    for t in tri:
        diff += [(q[0]-t[0], q[1]-t[1])]
print set(diff)

quad = [(-4, 2), (-2.5, 2), (-2.5, 3.5), (-4, 3.5)]
tri = [(-3, 1), (-1,3), (-1, 1)]
diff = []
for q in quad:
    for t in tri:
        diff += [(q[0]-t[0], q[1]-t[1])]
print set(diff)

