# Messages for each possible decision in the Haunted Mansion adventure

start_info = '''
------------------------------
You stand at the entrance of the Haunted Mansion. The door creaks open slightly,
inviting you inside. A chill runs down your spine.

::Valid Commands::
enter: Step inside the mansion
leave: Turn back and leave
------------------------------
'''

foyer_info = '''
------------------------------
You find yourself in the mansion's grand foyer. Cobwebs cover the chandeliers,
and shadows move in the corners of your vision.

::Valid Commands::
library: Head towards the dusty old library
basement: Descend into the dark, ominous basement
attic: Climb up the creaky stairs to the attic
------------------------------
'''

library_info = '''
------------------------------
The library is filled with dusty books and strange artifacts. A ghostly figure
appears and gestures towards a peculiar book.

::Valid Commands::
book: Open the book the ghost is pointing to
run: Sprint back to the foyer in fear
------------------------------
'''

basement_info = '''
------------------------------
The basement is cold and damp. You hear chains rattling in the distance. 
Suddenly, a menacing growl echoes through the room.

::Valid Commands::
investigate: Walk towards the source of the growl
escape: Quickly retreat to the foyer
------------------------------
'''

attic_info = '''
------------------------------
The attic is cluttered with old furniture and paintings. You spot a locked chest 
in the corner, covered in dust.

::Valid Commands::
open: Try to open the chest
leave: Return to the foyer
------------------------------
'''

ghost_info = '''
------------------------------
You open the book, and a ghostly voice tells you the secrets of the mansion. 
You have uncovered the mansion's mysteries and can leave peacefully.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

growl_info = '''
------------------------------
You move closer to the growl and come face-to-face with a werewolf! 
It lunges at you, and you barely manage to escape.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

treasure_info = '''
------------------------------
Inside the chest, you find a hidden treasure. Gold coins spill out, and you realize 
you've found the long-lost fortune of the mansion.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

flee_info = '''
------------------------------
You panic and rush out of the mansion. The adventure was too much to handle!

Your adventure is at an end.
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
        The starting state value for the game (string)
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
        state - current user state (string)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user (string)
    '''
    if state == 'Start':
        if message == 'enter':
            print(foyer_info)
            return 'Foyer'
        elif message == 'leave':
            print(flee_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == 'Foyer':
        if message == 'library':
            print(library_info)
            return 'Library'
        elif message == 'basement':
            print(basement_info)
            return 'Basement'
        elif message == 'attic':
            print(attic_info)
            return 'Attic'
        else:
            print("Invalid Command")
            return 'Foyer'
    elif state == 'Library':
        if message == 'book':
            print(ghost_info)
            return 'End'
        elif message == 'run':
            print(foyer_info)
            return 'Foyer'
        else:
            print("Invalid Command")
            return 'Library'
    elif state == 'Basement':
        if message == 'investigate':
            print(growl_info)
            return 'End'
        elif message == 'escape':
            print(foyer_info)
            return 'Foyer'
        else:
            print("Invalid Command")
            return 'Basement'
    elif state == 'Attic':
        if message == 'open':
            print(treasure_info)
            return 'End'
        elif message == 'leave':
            print(foyer_info)
            return 'Foyer'
        else:
            print("Invalid Command")
            return 'Attic'
    else:
        print("Invalid Command")
        return state
