power = True
eaten = False
touching = False

def eat_ghost(power_pellet_active, touching_a_ghost):
    "The function should return True only if Pac-Man has a power pellet active and is touching a ghost."

    if power_pellet_active == True and touching_a_ghost == True:
        return True
    else:
        return False

def score(touching_a_power, touching_a_dot):
    "The function should return True if Pac_Man is touching a power pellet or a dot."

    return touching_a_power or touching_a_dot

def lose(power_pellet_active, touching_a_ghost):
    "The function should return True if Pac-Man dose not have a power pellet active and touching a ghost."

    return touching_a_ghost and power_pellet_active

def win(eaten_all_dots, power_pellet_active, touching_a_ghost):
    "The function should return True if Pac-Man has eaten all of the dots and has not lost based on the parameters defined in part 3"

    return lose(power_pellet_active, touching_a_ghost) or eaten_all_dots
    
print (win(eaten, power, touching))
