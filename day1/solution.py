
f = open("input", "r")
content = f.read().split('\n\n')
elf_calories = [sum([int(num) for num in e.strip().split()]) for e in content]

max_cal = max(elf_calories)
max_elf = elf_calories.index(max_cal)

print(f"The elf at index {max_elf} has the most calories of {max_cal}")

