
def visibility(rows, cols, r, c):
    x = rows[r][c]
    row = rows[r]
    col = cols[c]
    score = 1

    temp = 0
    for i in row[0:c][::-1]:
        temp += 1
        if i >= x:
            break

    score *= temp
    temp = 0
    for i in row[c+1:len(row)]:
        temp += 1
        if i >= x:
            break

    score *= temp
    temp = 0
    for i in col[0:r][::-1]:
        temp += 1
        if i >= x:
            break

    score *= temp
    temp = 0
    for i in col[r+1:len(col)]:
        temp += 1
        if i >= x:
            break

    return score * temp


def rows_to_cols(rows):
    cols = []
    for i in range(len(rows[0])):
        cols.append([])
    for row in rows:
        for c, x in enumerate(row):
            cols[c].append(x)
    return cols


f = open("input", "r")
content = f.read().strip().split('\n')
rows = [[int(i) for i in x] for x in content]
cols = rows_to_cols(rows)

visibility_score = [[visibility(rows, cols, r, c) for c in range(len(rows[0]))] for r in range(len(rows))]
# for r in visibility_score:
#    print(r)

visibility_maxes = [max(x) for x in visibility_score]
# print(visibility_maxes)

print(f"Max visibility: {max(visibility_maxes)}")

