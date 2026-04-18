


class Room:
    """Represents a room in the castle with exits, optional items, and dragon presence."""
    def __init__(self, name, exits, item=0, has_dragon=False):
        """
               Initialize a Room instance.

               Args:
                   name (str): The name of the room.
                   exits (dict): A dictionary mapping directions to connected room names.
                   item (str, optional): The item found in the room. Defaults to None.
                   has_dragon (bool, optional): Whether the room contains a dragon. Defaults to False.
               """
        self.name = name # name of the room, received as the parameter 'name'
        self.exits = exits # 'exits' parameter will accept a dictionary of possible exits as an argument
        self.item = item # Represents a dictionary of items and their count
        self.has_dragon = has_dragon


if __name__ == "__main__":
    print(f"You made it into the class Room.")





