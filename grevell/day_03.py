
#
# I must give credit to Roippi - https://stackoverflow.com/users/2581969/roippi
# for their excellent example here : https://stackoverflow.com/questions/23706690/how-do-i-make-make-spiral-in-python
#
# This was used as the base idea for my solution.
#

#
# Define up/down & left/right step functions
#
def move_right(x,y):
    return x+1, y

def move_down(x,y):
    return x,y-1

def move_left(x,y):
    return x-1,y

def move_up(x,y):
    return x,y+1

#
# List of step movement functions that will be cycled
#
moves = [move_right, move_down, move_left, move_up]

def gen_points(end):
    """
    Generator function to return the spiral number and it's relative position (x,y) to the origin (0,0)
    :param end: Maximum spiral value
    :return : Yields spiral number and (x,y) pos
    """
    from itertools import cycle
    _moves = cycle(moves)
    n = 1
    pos = 0,0
    times_to_move = 1

    yield n,pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= end:
                    return
                pos = move(*pos)
                n+=1
                yield n,pos

        times_to_move+=1

def get_steps(end):
    """
    Get the number of steps to return from the position "end" to the origin
    :param end: Start spiral number to use
    :return: Spiral number, its (x,y) pos and the abs(x)+abs(y) number of steps needed to return to (0,0)
    """
    from itertools import cycle
    _moves = cycle(moves)
    n = 1
    pos = 0,0
    times_to_move = 1

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= end:
                    #
                    # Return the spiral number, the relative (x,y) pos and abs total steps
                    #
                    return n,pos,abs(pos[0])+abs(pos[1])
                pos = move(*pos)
                n+=1

        times_to_move+=1


if __name__ == "__main__":
    test = False
    if test:
        maxNo = int(input("Enter max spiral number: "))
        x = dict(gen_points(maxNo+1))
        y = x[maxNo]
        print("It will take {} steps to get the portal".format(abs(x[maxNo][0])+abs(x[maxNo][1])))

    for s in [1,12,23,1024]:
        r = get_steps(s)
        print("Spiral {} , (x,y) = {} , steps = {}".format(r[0],r[1],r[2]))

