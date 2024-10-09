

start_info = '''
------------------------------
You enter a dark, abandoned mansion. There's a cracking sound in the distance.
What will you do?

::Valid commands: 
explore: Look around the mansion
hide: Find a place to hide
leave: Run away before it's too late
------------------------------
'''
explore_info = '''
------------------------------
You find an old staircase leading to the basement.
What will you do?
::Valid commands:
descend: Go down the stairs
retreat: Return to the entrance
------------------------------
'''
basement_info = '''
------------------------------
You enter the basement, and you see a shadowy figure in the corner!
What will you do?

::Valid Commands::
confront: Approach the figure
escape: Run back up the stairs
------------------------------
'''
hidden_room_info = '''
------------------------------
The hidden door reveals a mysterious room filled with ancient artifacts.
A cursed book is on the table. What will you do?

::Valid Commands::
read: Read the cursed book
take: Take an artifact and leave
------------------------------
'''
cursed_info = '''
------------------------------
You open the book and unleash a powerful curse. Your adventure ends here.

Press the Log Out button.
------------------------------
'''


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
    print(start_info)
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
    if state == 'Start':
        if message == 'explore':
            print(explore_info)
            return 'Explore'
        elif message == 'hide':
            return 'End'
        elif message == 'leave':
            return 'End'
        else:
            print('Invalid command')
            return 'Start'
    elif state == 'Explore':
        if message == 'descend':
            print(basement_info)
            return 'Basement'
        elif message == 'retreat':
            print(cursed_info)
            return 'Start'
        else:
            print("Invalid Command")
            return 'Explore'
    elif state == 'Basement':
        if message == 'confront':
            return 'End'
        elif message == 'escape':
            return 'Explore'
        else:
            print("Invalid Command")
            return 'Basement'
    elif state == 'Hidden Room':
        if message == "read":
            print(cursed_info)
            return 'End'
    else:
        print("Invalid State")
        return 'Start'