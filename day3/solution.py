
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

values = dict(zip(alphabet, (i+1 for i in range(len(alphabet)))))

f = open("input", "r")
content = f.read().strip().split('\n')

score = sum([values[c] for e in content for c in set(e[:len(e)//2]) & set(e[len(e)//2:])])

print(f"Sum of priorities for items shared between compartments is equal to {score}")

