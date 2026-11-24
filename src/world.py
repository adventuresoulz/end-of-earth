from room import Room

starting_room = Room("Where it all begins...", "A cold and eerily quiet room, no larger than a small shed")
school_gym = Room("School Gym", "Outside of the Gym supply closet you find a large yet empty modern school gymnasium")
starting_room.exits["north"] = school_gym
school_gym.exits["south"] = starting_room
