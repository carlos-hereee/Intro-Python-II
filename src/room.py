# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room, description):
        self.room = room
        self.description = description

    def __str__(self):
        return self.room


# outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")

# print(f"\n{outside.room} the description would be {outside.description}")


# room = {
#     'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
# }
# print(f"\n{room['outside']} {room['outside'].description}")
