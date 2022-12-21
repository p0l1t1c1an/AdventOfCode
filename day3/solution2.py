
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

values = dict(zip(alphabet, (i+1 for i in range(len(alphabet)))))

f = open("input", "r")
content = f.read().strip().split('\n')

lines = [set(e) for e in content]
score = sum([values[i] for s in zip(lines[::3], lines[1::3], lines[2::3]) for i in (s[0] & s[1] & s[2])])

print(f"Sum of priorities for items shared between compartments is equal to {score}")

