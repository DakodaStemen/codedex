players = [
    {"name": "Patrick Mahomes", "position": "QB", "jersey": 15, "yards": 320, "touchdowns": 3},
    {"name": "Travis Kelce", "position": "TE", "jersey": 87, "yards": 98, "touchdowns": 1},
    {"name": "Isiah Pacheco", "position": "RB", "jersey": 10, "yards": 76, "touchdowns": 1},
    {"name": "Chris Jones", "position": "DT", "jersey": 95, "yards": 0, "touchdowns": 0}
]

positions = [player["position"] for player in players]
print(positions)


for player in players:
    if player["name"] == "Patrick Mahomes":
        player["yards"] += 50
        player["touchdowns"] += 1

total_yards = sum(player["yards"] for player in players)
total_touchdowns = sum(player["touchdowns"] for player in players)
num_players = len(players)

avg_yards = total_yards / num_players
avg_touchdowns = total_touchdowns / num_players

print(f"Average Yards: {avg_yards:.2f}")
print(f"Average Touchdowns: {avg_touchdowns:.2f}")
