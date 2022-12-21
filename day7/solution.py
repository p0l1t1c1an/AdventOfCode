
f = open("input", "r")
content = f.read().strip().split('\n')
current_dir = ""
read_ls_out = False
sum_size = 0
sizes = {}
directories = {'/': []}
truth = {}


def true_size(d):
    size = sizes[d]
    if d in directories:
        for sub in directories[d]:
            size += true_size(d + sub + '/')
    truth.update({d: size})
    return size


for c in content:
    split = c.strip().split()
    if '$' in split[0]:
        if read_ls_out:
            sizes.update({current_dir: sum_size})
        sum_size = 0
        read_ls_out = False
        if split[1] == 'cd':
            if split[2].startswith('/'):
                current_dir = split[2]
            elif split[2] == '..':
                index = len(current_dir) - current_dir[::-1].index('/', 1)
                current_dir = current_dir[:index]
            else:
                current_dir += split[2] + '/'
        elif split[1] == 'ls' and current_dir not in sizes:
            read_ls_out = True
    elif read_ls_out:
        if split[0].isnumeric():
            sum_size += int(split[0])
        elif split[0] == 'dir':
            if current_dir in directories:
                directories[current_dir].append(split[1])
            else:
                directories.update({current_dir: [split[1]]})


if read_ls_out:
    sizes.update({current_dir: sum_size})

print(sizes)
#print(directories)

true_size('/')

print()
print(truth)

print()
print("The total size of directories smaller than 100000 is:")
print(sum([truth[x] for x in truth if truth[x] <= 100000]))


