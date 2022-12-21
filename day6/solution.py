
def hasrepeat(s):
    for c in s:
        if s.count(c) > 1:
            return True
    return False


f = open("input", "r")
content = f.read().strip()

sequences = [content[i:i+4] for i in range(len(content) - 3)]
repeats = list(map(hasrepeat, sequences))

print(sequences)
print(repeats)

first = repeats.index(False)

print(f"The first index that has no repeats starts at {first+1} and ends at {first+4}")
