def enter_zone(user, state):
    '''
    Purpose: Sets up the initial state of the user when they 
        first enter the adventure.
    Parameters:
        user - the name of the user (string)
        state - currently unused (None)
    Return Value:
        The starting state value for the game (???)
    '''
     # The starting state is "Start"
    print(f"Welcome, {user}, to the adventure!")
    print("You find yourself standing at the edge of a mysterious cave.")
    print("Type 'explore' to investigate the cave.")
    return 'Start'

def command(user, state, message):
    '''
    Purpose:
        Runs whenever the user types something into the command box.
        Determines if their command is valid and progresses the story if so.
    Parameters:
        user - the name of the user (string)
        state - current user state (???)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user (???)
    '''
    message = message.lower()

    # State: Start
    if state == 'Start':
        if message == 'explore':
            print("You walk toward the cave entrance.")
            print("It's dark and cold inside. Type 'enter' to go inside or 'leave' to turn back.")
            return 'Cave Entrance'
        else:
            print("Invalid command. Type 'explore' to begin your adventure.")
            return state

    # State: Cave Entrance
    elif state == 'Cave Entrance':
        if message == 'enter':
            print("You enter the cave. The air is damp, and you hear distant growls.")
            print("Type 'fight' to face the creature or 'flee' to escape.")
            return 'Inside Cave'
        elif message == 'leave':
            print("You decide it's too dangerous and leave the cave.")
            print("The adventure ends here. Better luck next time!")
            return 'End'
        else:
            print("Invalid command. Type 'enter' to go inside or 'leave' to turn back.")
            return state

    # State: Inside Cave
    elif state == 'Inside Cave':
        if message == 'fight':
            print("You bravely face the creature. After a fierce battle, you emerge victorious!")
            print("Congratulations, you completed the adventure!")
            return 'End'
        elif message == 'flee':
            print("You decide to flee, running out of the cave to safety.")
            print("The adventure ends with you escaping unharmed.")
            return 'End'
        else:
            print("Invalid command. Type 'fight' to confront the creature or 'flee' to escape.")
            return state

    # State: End
    elif state == 'End':
        print("The adventure is over. Thank you for playing!")
        return state
    
