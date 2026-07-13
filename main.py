from app import *

while True:

    print("═════════════════════════ ♟️ 🏆 Chess Tournament Manager 🏆♟️ ═══════════════════════")
    print("1. Add Player♟️ :")
    print("2. View Players🔎:")
    print("3. Record Match👯:")
    print("4. Leaderboard🦾:")
    print("5. Show Winner🏅:")
    print("6. Remove Player📤:")
    print("7.Exit🕊️ :")

    choice = input("Enter your choice🫳 : ")
   
   
    if choice == "1":
        name = input("Enter ♟️⚡ Player Name: ")
        print(add_player(name))
 
    elif choice == "2":
        view_players()       
 
    elif choice == "3":
        player1 = input("Enter Player 1️⃣: ") 
        player2 = input("Enter Player 2️⃣: ") 
        print("\n1. Player1 Wins🏅")
        print("2. Player2 Wins🏅")
        print("3. Draw🤝")
   
        result = int(input("Enter Result:"))
        message = record_match(player1, player2, result)
        print(message)
    elif choice == "4":
        leaderboard()
  
    elif choice == "5":
        winner()   
    elif choice == "6":
        name = input("Enter player Name⚡:")
        print(Remove_Player(name))      
    elif choice == "7":
        print("♟️ Thank you for Using Chess Tournament Manager ♟️ ")
        break
   
    else:
        print("👀Invalid Option")