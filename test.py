f = {}

f[0] = 10
f[1] = 5
f[2] = 11
f[3] = 21

l = []
for idVertice, tempoVertice in f.items():
    l.append((idVertice, tempoVertice))
print(l)
l.sort(key=lambda x: x[1], reverse=True)
print(l)
l = map(lambda x: x[0], l)
print(l)
