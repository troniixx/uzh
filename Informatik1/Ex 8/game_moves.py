#!/usr/bin/env python3
# Implement this function
__author__ = "Mert Erol"
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def move(state, direction):

    def player_pos(gameworld):
        players = 0
        if len(gameworld) <= 0:
            raise Warning("Invalid game state")  # sensible size (both dim > 0 )
        for line in gameworld:
            if len(line) <= 0:
                raise Warning("Invalid game state")  # sensible size (both dim > 0 )
            elif not len(gameworld[0]) == len(line):  # each line same length
                raise Warning("Invalid game state")
            for char in line:
                if not char == " " and not char == "#" and not char == "o":  # only defined chars
                    raise Warning(f"invalid character: {char}")
                elif char == "o":
                    players += 1
                    if players > 1:
                        raise Warning("Too many players")  # exactly one player
                    horiz = line.index(char)
                    vert = gameworld.index(line)
        if players < 1:
            raise Warning("No player found")
        return (vert, horiz)


    def move_down(player_vert, player_horiz, world):
        changeable_down = list(world)
        if changeable_down[player_vert] == changeable_down[-1]:
            raise Warning("Invalid move")
        elif changeable_down[player_vert + 1][player_horiz] == "#":
            raise Warning("Invalid move")
        else:
            changeable_down[player_vert] = changeable_down[player_vert][:player_horiz] +" " + changeable_down[player_vert][player_horiz+1:]
            changeable_down[player_vert + 1]= changeable_down[player_vert+1][:player_horiz] +"o" + changeable_down[player_vert+1][player_horiz+1:]
        return tuple(changeable_down)

    def move_left(player_vert, player_horiz, world):
        changeable_left = list(world)
        if changeable_left[player_vert][player_horiz] == changeable_left[player_vert][0]:
            raise Warning("Invalid move")
        elif changeable_left[player_vert][player_horiz - 1] == "#":
            raise Warning("Invalid move")
        else:
            changeable_left[player_vert] = changeable_left[player_vert][:player_horiz - 1] + "o" + " " + changeable_left[player_vert][
                                                                                               player_horiz + 1:]
        return tuple(changeable_left)

    def move_right(player_vert, player_horiz, world):
        changeable_right= list(world)
        if changeable_right[player_vert][player_horiz] == changeable_right[player_vert][-1]:
            raise Warning("Invalid move")
        elif changeable_right[player_vert][player_horiz + 1] == "#":
            raise Warning("Invalid move")
        else:
            changeable_right[player_vert] = changeable_right[player_vert][:player_horiz]+ " "+ "o" + changeable_right[player_vert][
                                                                                             player_horiz + 2:]
        return tuple(changeable_right)

    def move_up(player_vert, player_horiz, world):
        changeable_down = list(world)
        if changeable_down[player_vert] == changeable_down[0]:
            raise Warning("Invalid move")
        elif changeable_down[player_vert -1][player_horiz] == "#":
            raise Warning("Invalid move")
        else:
            changeable_down[player_vert] = changeable_down[player_vert][:player_horiz] +" " + changeable_down[player_vert][player_horiz+1:]
            changeable_down[player_vert -1]= changeable_down[player_vert-1][:player_horiz] + "o" + changeable_down[player_vert-1][player_horiz+1:]
        return tuple(changeable_down)

    x, y = player_pos(state)

    if direction == "down":
        new_state = move_down(x,y,state)

    elif direction == "left":
        new_state = move_left(x,y,state)

    elif direction == "right":
        new_state = move_right(x,y,state)

    elif direction == "up":
        new_state = move_up(x,y,state)

    else:
        raise Warning("Invalid move type")

    def possible_direct():
        possible = []
        a,b= player_pos(new_state)
        try:
            move_down (a,b,new_state)
        except:
            pass
        else:
            possible.append("down")
        try:
            move_left (a,b,new_state)
        except:
            pass
        else:
            possible.append("left")
        try:
            move_right (a,b,new_state)
        except:
            pass
        else:
            possible.append("right")
        try:
            move_up (a,b,new_state)
        except:
            pass
        else:
            possible.append("up")

        if len(possible) >= 1:
            return tuple(possible)
        else:
            raise Warning("No possible further moves")
    #at least one possible move

    #get possible moves
    return (new_state, tuple(possible_direct())) #get new state


# The following line calls the function and prints the return
# value to the Console.
s1 = (
    "#####  o",
    "###    #",
    "#     ##",
    "   #####"
)

s2 = move(s1, "left")
print("= New State =")
print("\n".join(s2[0]))
print("\nPossible Moves: {}".format(s2[1]))

