
def hasrepeat(s):
    for c in s:
        if s.count(c) > 1:
            return True
    return False


f = open("input", "r")
content = f.read().strip()

sequences = [content[i:i+14] for i in range(len(content) - 13)]
repeats = list(map(hasrepeat, sequences))

print(sequences)
print(repeats)

print(len(repeats))
print(repeats[2300:2310])

first = repeats.index(False)


print(f"The first index that has no repeats starts at {first+1} and ends at {first+14}")
