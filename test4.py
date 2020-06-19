names = locals()
for i in range(1, 101):
    names['x%s' %i] = i
print(names['x100'])