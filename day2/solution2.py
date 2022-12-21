
f = open("input", "r")
content = f.read().strip().split('\n')

#       Rock    Paper   Scissors
opnt = {'A': 1, 'B': 2, 'C': 3}

#       Lose    Draw    Win
play = {'X': 0, 'Y': 3, 'Z': 6}


def game_score(o, p):
    score = play[p]
    if p == 'X':
        score += (opnt[o] + 1) % 3 + 1
    elif p == 'Y':
        score += opnt[o]
    elif p == 'Z':
        score += (opnt[o]) % 3 + 1

    print(f"{o} {p}: {score}")
    return score


score = sum(map(lambda g: game_score(g[0], g[1]), [e.split() for e in content]))

print(f"You earned {score} points in RPS")

