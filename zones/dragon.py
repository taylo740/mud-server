#Messages for each possible decision




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
    return 'End'