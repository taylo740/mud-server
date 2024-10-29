
def attack_dragon(user, state):
    print("YOU ATTACKED THE DARGON RAWR")
    print("You deal 5 damage")
    state['zone_data']['dragon']['health'] -= 5

def use_fountain(user, state):
    print("You drink from the healing fountain and restore your health")
    state['stats']['Health'] = 100

def initialize_areas():
    print("TWO DRAGON")
    dragon = {'room':'lair', 'present':True, 'health':200, 'commands':{'attack': attack_dragon}}
    return {'dragon':dragon, }

def enter_zone(user, state):
    '''
    Purpose: Sets up the initial state of the user when they 
        first enter the adventure.
    Parameters:
        user - the name of the user (string)
        state - currently unused (None)
    Return Value:
        The starting state value for the game (string)
    '''
    state['room'] = 'Entrance'

    return state

def command(user, state, message):
    '''
    Purpose:
        Runs whenever the user types something into the command box.
        Determines if their command is valid and progresses the story if so.
    Parameters:
        user - the name of the user (string)
        state - which decision point the user is currently in (string)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user, which determines what decision
        they will need to make next. (string)
    '''
    print("message is", message)
    print("stats is", state['stats'])
    if 'heal' in message:
        state['stats']['Health'] += 5
    return state