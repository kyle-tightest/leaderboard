import sys

def calculate_points(scores):
    team1_score, team2_score = scores
    if team1_score > team2_score:
        return 3, 0
    elif team1_score < team2_score:
        return 0, 3
    else:
        return 1, 1

def main():
    teams = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            team1_str, team2_str = line.split(',')
            team1_name, team1_score = team1_str.rsplit(' ', 1)
            team2_name, team2_score = team2_str.rsplit(' ', 1)

            team1_score = int(team1_score)
            team2_score = int(team2_score)

            team1_name = team1_name.strip()
            team2_name = team2_name.strip()

            if team1_name not in teams:
                teams[team1_name] = 0
            if team2_name not in teams:
                teams[team2_name] = 0

            team1_points, team2_points = calculate_points((team1_score, team2_score))
            teams[team1_name] += team1_points
            teams[team2_name] += team2_points
        except ValueError:
            print(f"Skipping invalid line: {line}", file=sys.stderr)


    sorted_teams = sorted(teams.items(), key=lambda item: (-item[1], item[0]))

    for i, (team, points) in enumerate(sorted_teams, 1):
        pts_str = "pt" if points == 1 else "pts"
        print(f"{i}. {team}, {points} {pts_str}")

if __name__ == "__main__":
    main()
