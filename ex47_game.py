class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)



start = Room("Start", "You can go west and down a hole.")
west = Room("Trees", "There are trees here, you can go east.")
down = Room("Dungeon", "It's dark down here, you can go up.")

# Define paths between rooms
start.add_paths({'west': west, 'down': down})
west.add_paths({'east': start})
down.add_paths({'up': start})

current_room = start

while True:
    print(f"You are in {current_room.name}. {current_room.description}")
    user_input = input("> ")

    if user_input.lower() == 'exit':
        break  

    next_room = current_room.go(user_input.lower())
    if next_room:
        current_room = next_room
    else:
        print("Invalid direction. Try again.")
