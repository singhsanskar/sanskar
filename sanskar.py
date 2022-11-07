
def tournamentwinner(results, competitions):
    winner = 1
    best_team = ""
    scores = {best_team : 0}

    for i, competition in enumerate(competitions):
        result = results[i]
        home_team, away_team = competition
        winning_team = home_team if result == winner else away_team

        update_score(winning_team, 3, scores)

        if scores[winning_team] > scores[best_team]:
            best_team = winning_team
    return best_team

def update_score(team, points, score):
    if team not in score:
        score[team] = 0
    score[team] += points

win = tournamentwinner([0, 0, 0], [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
])
print(win)
result = [0, 0, 1]