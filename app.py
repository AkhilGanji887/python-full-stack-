# ============================
# Chess Tournament Manager
# ============================

# Players Database
players = {}


# Add Player Function
def add_player(name: str):
    if name in players:
        return "Player already exists."

    players[name] = {
        "points": 0,
        "matches": 0
    }
    return f"{name} added successfully."

def Remove_Player(name: str):
    if name not in players: 
        return "player not found."
    del players[name]
    return f"{name} removed successfully."


# View Players Function
def view_players():
    if not players:
        print("No Players available.")
        return

    print("\n------ Players ------")
    for i, player in enumerate(players, start=1):
        print(f"{i}. {player}")


# Record Match Function
def record_match(player1: str, player2: str, result: int):

    if player1 not in players or player2 not in players:
        return "Player not found."

    players[player1]["matches"] += 1
    players[player2]["matches"] += 1

    if result == 1:
        players[player1]["points"] += 1

    elif result == 2:
        players[player2]["points"] += 1

    elif result == 3:
        players[player1]["points"] += 0.5
        players[player2]["points"] += 0.5

    return "Match recorded successfully."


# Leaderboard Function
def leaderboard():

    print("------ Leaderboard ------")

    rank = sorted(players.items(),
                  key=lambda x: x[1]["points"],
                  reverse=True)

    for i, player in enumerate(rank, start=1):
        print(f"{i}. {player[0]} - {player[1]['points']} Points")


# Winner Function
def winner():

    if not players:
        print("No players found.")
        return

    highest_points = max(player["points"] for player in players.values())

    winners = []

    for name, details in players.items():
        if details["points"] == highest_points:
            winners.append(name)

    if len(winners) == 1:
        print("\n🏆 Tournament Winner 🏆")
        print(f"{winners[0]} - {highest_points} Points")

    else:
        print("\n🤝 Tournament Draw")
        print("Players:")

        for player in winners:
            print(player)

        print(f"Points : {highest_points}")# ============================

