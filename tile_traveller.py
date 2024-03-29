import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")

def lever_check(coin):
    #question = input("Pull a lever (y/n): ")
    print("Pull a lever (y/n): ")

    choice = random.choice(valid_choices)
    print(choice)

    question = choice
    if question == 'y' or question == 'Y':
        coin = coin + 1
        print("You received 1 coin, your total is now", coin, end="")
        print(".")
    return coin

def find_directions(col, row, coin):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
        coin = lever_check(coin)
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
        coin = lever_check(coin)
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
        coin = lever_check(coin)
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
        coin = lever_check(coin)
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions, coin

def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''

    choice = random.choice(valid_choices)
    print(choice)
    victory = False
    #direction = input("Direction: ")
    print("Direction: ")
    direction = choice
    #direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row

# The main program starts here
victory = False
row = 1
col = 1
coin = 0

valid_choices = ('n','e','s','w','y')

what_seed = int(input("Input seed: "))

random.seed(what_seed)

#choice = random.choice(valid_choices)
#print(choice)

valid_directions = NORTH
print_directions(valid_directions)


while not victory:
    victory, col, row = play_one_move(col, row, valid_directions)
    if victory:
        print("Victory! Total coins", coin, end="")
        print(".")
        answer_again = input("Play again (y/n): ")
        if answer_again == "y" or answer_again == "Y":
            victory = False
            row = 1
            col = 1
            coin = 0
            valid_directions = NORTH
            print_directions(valid_directions)
    else:
        valid_directions, coin = find_directions(col, row, coin)
        print_directions(valid_directions)
