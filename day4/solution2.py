

def overlap(x):
    return not(x[0][1] < x[1][0] or x[0][0] > x[1][1])


f = open("input", "r")
content = f.read().strip().split('\n')

ranges = [[int(t[0]),int(t[1])] for t in [times.split('-') for times in [rng for e in content for rng in e.split(',')]]]
ranges = [x for x in zip(ranges[::2], ranges[1::2])]
total = [x for x in ranges if overlap(x)]
print(total)

print(f"{len(total)} assignment pairs overlap.")

