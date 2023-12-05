from functools import cache

with open("/Users/nolanpestano/Documents/GitHub/2023_AOC/4_day/input.txt") as f:
    lines = f.readlines()
    
def score_card(l):
    _, body = l.split(":")
    win, bet = body.split("|")
    winners = set(win.strip().split())
    bettors = set(bet.strip().split())
    joined = winners & bettors
    print(joined)
    return len(joined)


score_table = [score_card(l) for l in lines]
total = sum([2 ** (s-1) for s in score_table])

print("Phase 1: ", total)
