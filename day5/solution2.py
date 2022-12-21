
f = open("input", "r")
content = f.read().split('\n\n')
print(content[0])

values = content[0].split('\n')
values.reverse()

length = len(values[0].strip().split())
print(length)

stacks = [[] for i in range(length)]

for line in values[1:]:
    for count, val in enumerate(line[1::4]):
        if not val.isspace():
            stacks[count].append(val)

print(stacks)

moves = [(int(v[1]), int(v[3]), int(v[5])) for v in [e.strip().split() for e in content[1].strip().split('\n')]]
#print(moves)

for num, old, new in moves:
    index = len(stacks[old-1]) - num
    for i in range(num):
        stacks[new-1].append(stacks[old-1].pop(index))

print(stacks)


for s in stacks:
    print(s.pop(), end='')

print()
