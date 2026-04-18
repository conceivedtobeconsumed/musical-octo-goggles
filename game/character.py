


class Character:
    """Represents the games primary character a name, an inventory, and a current location ."""
    def __init__(self, name, lives=1, inventory=None, location="main hall"):
        """
               Initialize a Character instance.

               Args:
                   name (str): The name of the character.
                   inventory (str, optional): Items stored in inventory. Defaults to None.
                   location (str): The location of the character on the board. Defaults to Main Hall.
                   lives (int, optional): How many lives there are. Defaults to 1.
               """
        self.name = name
        self.inventory = inventory if inventory else {"gold": 0, "potion": 0}
        self.location = location
        self.lives = lives

if __name__ == "__main__":
    print(f"You found the class Character.")