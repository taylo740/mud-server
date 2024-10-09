guide_game = '''
------------------------------
This is an escape room game!
You and your friends are locked down in one room and you have to escape with in hour.
To escape, you have to solve the puzzle!
There two teams, pick the right team
understand the rules and be a consistent 
observe wisely

::Valid Commands::
listen: listen closely to the story 
look: look for hints 
escape: exist the room
------------------------------
'''

mystery_info = '''
------------------------------
groups attempt to find clubes
solve a series of puzzles to escape
time is limited

::Valid Commands::
organazie: collect and organize the hints you've found
communication: talk and discuss with your friends
------------------------------
'''

time_over = '''
------------------------------
on average it is between 60 - 90 mintues
you didn't escape the room on time, the game is considered over 

::Valid Commands::
timer: set a timer to stay on truck
rules: use the hints
------------------------------
'''

victory_info = '''
------------------------------
You and your friends solve the mysetious puzzle on time, and able to escape from the room. 
You and your friends gets an award!

::Valid Commands:: 
celebrate the moment!
------------------------------
'''

after_game = '''
------------------------------
You had fun with your friends!
Press the Log Out button to end. 
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
    print(guide_game)
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
            if message == 'listen':
                print(mystery_info)
                return 'mystery'
            elif message == 'escape':
                print('you did amazing work')
                return 'Start'
            else: 
                print('Invalid Command')
                return 'start'
    elif message == 'mystery':
            if message == 'organize':
                print(time_over)
                return 'end'
            elif message == 'communication':
                 print('discuss with your friends, the hints you have found')
                 return 'mystery'
            else:
                print("Yay, you win")
                return 'mysterious'
    elif state == 'group':
            print('take_prize')
            return mystery
    elif state == 'end':
            print(time_over)
            return 'end'
    elif state == 'victory':
            print(victory_info)
            return 'after_game'
    return 'Start'
