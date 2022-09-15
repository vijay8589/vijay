v = [-1, 2, 3, 4, -3, 5]
v.sort()
a = []
b = []
c = []
i = 0
while i < len(v):
    if v[i] < 0:
        a.append(v[i])
    else:
        b.append(v[i])
        i += 1
c.append(max(a))
c.append(min(b))
print(min(c))

