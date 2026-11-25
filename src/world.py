from room import Room
## todo more rooms -- unique interacts in each room
##############################################################
##          Rooms located here                              ##
##############################################################
starting_room = Room("where it all begins...", "A cold and eerily quiet room, no larger than a small shed")
school_gym = Room("school gym", "...Outside of the gym supply closet you find a large yet empty modern school gymnasium")
school_courtyard = Room("school courtyard", "...a well kept courtyard looks to be recently renovated")
school_main_hall = Room("main hall of the school", "...a really elite looking school though it looks like classes are out today")
locker_rooms = Room("locker rooms", "...I probably shouldn't be here")







## web of rooms and how they are interconnected
starting_room.exits["north"] = school_gym

school_gym.exits["south"] = starting_room
school_gym.exits["north"] = school_courtyard
school_gym.exits["west"] = locker_rooms
school_gym.exits["east"] = school_main_hall

locker_rooms.exits["east"] = school_gym

school_main_hall.exits["west"] = school_gym

school_courtyard.exits["south"] = school_gym





