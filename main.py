import sys
from game.room import Room
from game.character import Character

def _stats(player: Character, location: Room, next_move: str) -> None:
    """
            Displays the player's current status including name, room,
            move direction, and inventory.

            Args:
                player (Character): The player whose status is displayed.
                location (Room): The room where the player is currently located.
                next_move (str): The direction the player is moving or has chosen.

            Returns:
                None

            """
    print("==" * 30)
    print(f"{player.name}, of the Great Council")
    print("--" * 30)
    print(f"Current Room: {location.name.capitalize()} || Move's Direction: {next_move}")
    print(f"Inventory: {player.inventory}")
    print("==" * 30)
    return None

def _handle_dragon(player: Character, game_board: dict) -> tuple:
    """
            Takes the player object and game_board dict to handle dragon
            encounter win/lose conditions.

            Args:
                player (Character): The player whose direction shall be taken.
                game_board (dict): A dictionary mapping directions to rooms.

            Returns:
                 tuple: A tuple of (player, Room) where player is the
                        updated Character and Room is main hall if the player
                        has extra lives remaining.

            """
    print("You found the dragon.")
    if player.inventory["gold"] < 6:
        print(f"You have {player.lives} lives and {player.inventory['gold']} gold pieces.")
        print("You have not found all the gold. You die!")
        player.lives -= 1
        if player.lives == 0:
            sys.exit()
        else:
            print("It is a miracle! The potion you found in the secret passage has restored your life. Be careful and try again.")
            room = game_board["main hall"]
            return player, room
    else:
        print(f"You found all the gold, and then found the dragon. You win!")
        sys.exit()

def _handle_item(player: Character, entered_room: Room) -> tuple:
    """
            Takes the player and entered_room objects to present items upon entering the room.
            If item collected by player, player.inventory updated with item, and entered_room.item
            updated to remove from the room.

            Args:
                player (Character): The player whose direction shall be taken.
                entered_room (Room): The room where the player is currently located.

            Returns:
                tuple: A tuple of (player, entered_room) where player is the
                updated Character and entered_room is the updated Room.
            """
    print("**" * 30)
    print(f"You found an item! It appears to be {entered_room.item.upper()}.")
    print("**" * 30)
    print("**" * 30)
    print()
    print(f"Do you want to add {entered_room.item} to your inventory?")
    choice = input("Yes/No: ").lower().strip()
    while choice not in ["yes", "no"]:
        print(f"Invalid choice. Try again.")
        choice = input("Yes/No: ").lower().strip()
    if choice == "yes":
        print(f"You place the {entered_room.item} in to your inventory, and determined move on to the next room.")
        if entered_room.item == "potion":
            player.inventory["potion"] += 1
            player.lives += 1
            entered_room.item = None
        elif entered_room.item == "gold":
            player.inventory["gold"] += 1
            entered_room.item = None
    return player, entered_room

def _move_player(player: Character, location: Room, next_move: str, game_board: dict) -> Room:
    """
            Takes the player and location objects while using next_move to progress
            the player object to the next room.

            Args:
                player (Character): The player whose direction shall be taken.
                location (Room): The room where the player is currently located.
                next_move (str): The next direction shall be taken.
                game_board (dict): A dictionary mapping directions to rooms.

            Returns:
                Room: The new room if the move is valid, or the current room
                      if the direction has no exit.

            """
    _stats(player, location, next_move)
    if next_move not in location.exits:
        print(f"You look for a door or latch but find only a damp, mossy wall. Try again {player.name}.")
        input("Press Enter to continue...")
        return location
    entered_room = game_board[location.exits[next_move]]
    print(f"You've entered the {entered_room.name}")
    return entered_room

def intro(player: Character) -> Character:
    """
        Display the game introduction and backstory to the player. Collects user input
        for player.name.
        Args:
            player (Character): The player whose direction shall be taken.
        Returns:
            Character: Updated object with user-defined Name
    """
    print("""
                                                     DWARF GOLD HEIST !!!

          As a dwarf of the great council, you are tasked with infiltrating the dragon’s lair, a great castle underground.  
          The dragon has hidden piles of treasure throughout his castle.  Your task is to collect all the gold before the 
          dragon finds out.  Once you have all the gold you must face the dragon and defeat them to win. If you face the 
          dragon having not collected all the gold, your adventure ends!

          Your eyes are blurred from losing the sunlight upon entering in to the great mountain. The air is dank and 
          heavy with moisture.  It is dark and your torch light only glows the center of the room. You determine you are 
          in the main hall of the great castle. What happens next is up to you!

          """)
    player.name = input("What is your name brave Dwarf? ").capitalize().strip()
    return player

def player_input(player: Character, location: Room, next_move: str) -> tuple:
    """
        Prompt the player for a directional move and validate the input.
        'exit' as input is accepted to end the game.

        Args:
            player (Character): The player whose direction shall be taken.
            location (Room): The room where the player is currently located.
            next_move (str): The previous move direction to display in status.

        Returns:
            tuple: A tuple representing (player, next_move) where player is Character and next_move is a
            valid direction (north, south, east, or west).
        """
    _stats(player, location, next_move)
    print("""
    Which direction shall you take next? 
    - [north]
    - [south] 
    - [east] 
    - [west]
    Type 'exit' to end game.
    """)
    while True:
        next_move = input().lower().strip()
        if next_move == "exit":
            sys.exit("Thanks for playing!")
        if next_move in ["east", "north", "south", "west"]:
            return player, next_move
        print("Invalid move. Try again.")

def gameplay(player: Character, location: Room, move: str, game_board: dict) -> tuple:
    """
        Takes the player and location objects while using next_move to progress
        the player object to the next room. Handles item collection, potion effects,
        and dragon encounter win/lose conditions.

        Args:
            player (Character): The player whose direction shall be taken.
            location (Room): The room where the player is currently located.
            move (str): The next direction shall be taken.
            game_board (dict): A dictionary mapping directions to rooms.

        Returns:
            tuple: A tuple of (player, entered_room) where player is the
            updated Character and entered_room is the new Room location.

        """
    entered_room = _move_player(player, location, move, game_board)
    if entered_room == location:
        return player, entered_room
    if entered_room.name == "easter egg":
        print("==" * 30)
        print("You found a dusty scroll on the wall...")
        print("~~~" * 30)
        print("It reads: 'This game was crafted by: '")
        for c in ["conceived", "-","to", "-", "be", "-", "consumed"]:
            print(c)
        print("~~~" * 30)
        print("==" * 30)
        input("Press Enter to continue...")
    if entered_room.has_dragon:
        player, entered_room =_handle_dragon(player, game_board)
    elif entered_room.item:
        player, entered_room = _handle_item(player, entered_room)
        if player.inventory["gold"] == 6:
            game_board["west hall"].exits["west"] = "easter egg"
    return player, entered_room



if __name__ == "__main__":
    rooms = {
        "main hall": Room("main hall",{"north": "north hall", "south": "south hall", "east": "east hall", "west": "west hall"}),
        "north hall": Room("north hall", {"south": "main hall", "west": "dragon's lair"}, item= "gold"),
        "east hall": Room("east hall", {"north": "north east hall", "south": "south east hall", "west": "main hall"}, item= "gold"),
        "south hall": Room("south hall", {"north": "main hall"}, item= "gold"),
        "west hall": Room("west hall", {"east": "main hall"}, item= "gold"),
        "north east hall": Room("north east hall", {"south": "east hall", "west": "secret passage"}, item= "gold"),
        "south east hall": Room("south east hall", {"north": "east hall"}, item= "gold"),
        "secret passage": Room("secret passage", {"west": "dragon's lair", "east": "north east hall"}, item= "potion"),
        "dragon's lair": Room("dragon's lair", {}, has_dragon= True),
        "easter egg": Room("easter egg", {"north": "main hall", "south": "main hall", "east": "main hall", "west": "main hall"})
    }
    active_player = (Character("player1"))
    active_location = rooms["main hall"]
    active_player = intro(active_player)
    while True:
        active_player, players_move = player_input(active_player, active_location, next_move= "To be determined")
        active_player, active_location = gameplay(active_player, active_location, players_move, rooms)
