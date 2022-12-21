
f = open("input", "r")
content = f.read().strip().split('\n')

#       Rock    Paper   Scissors
opnt = {'A': 1, 'B': 2, 'C': 3}
play = {'X': 1, 'Y': 2, 'Z': 3}


def game_score(o, p):
    diff = opnt[o] - play[p]
    score = play[p]
    if diff in [-1, 2]:
        score += 6
    elif diff == 0:
        score += 3
    print(f"{o} {p}: {score}")
    return score


score = sum(map(lambda g: game_score(g[0], g[1]), [e.split() for e in content]))

print(f"You earned {score} points in RPS")

