
def view_left_right(rows):
    rev = [row[::-1] for row in rows]
    left = [[True if c == 0 or i > max(row[0:c]) else False for c, i in enumerate(row)] for row in rows]
    right = [[True if c == 0 or i > max(row[0:c]) else False for c, i in enumerate(row)][::-1] for row in rev]
    return (left, right)


def rows_to_cols(rows):
    cols = []
    for i in range(len(rows[0])):
        cols.append([])
    for row in rows:
        for c, x in enumerate(row):
            cols[c].append(x)
    return cols


def view_down_up(cols):
    rev = [col[::-1] for col in cols]
    down = [[True if c == 0 or i > max(col[0:c]) else False for c, i in enumerate(col)] for col in cols]
    up = [[True if c == 0 or i > max(col[0:c]) else False for c, i in enumerate(col)][::-1] for col in rev]
    return (down, up)


f = open("input", "r")
content = f.read().strip().split('\n')
rows = [[int(i) for i in x] for x in content]
cols = rows_to_cols(rows)

left, right = view_left_right(rows)
down, up = view_down_up(cols)

or_views = lambda r, c: left[r][c] or right[r][c] or down[c][r] or up[c][r]

visible = [True for r in range(len(rows)) for c in range(len(rows[0])) if or_views(r, c)]
print(sum(visible))

visibility = [[1 if or_views(r, c) else 0 for c in range(len(rows[0]))] for r in range(len(rows))]
for r in visibility:
    print(r)

