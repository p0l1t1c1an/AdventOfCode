
f = open("input", "r")
content = f.read().split('\n\n')
elf_calories = [sum([int(num) for num in e.strip().split()]) for e in content]

elf_calories.sort(reverse=True)
#print(elf_calories)

print(f"Highest 3 elf calories are {elf_calories[:3]}")
print(f"Sum: {sum(elf_calories[:3])}")
