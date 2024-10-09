#Messages for decisions

start_info = '''
------------------------------
You launch your Wii and begin playing a Super Mario game. As Mario, you
end up in Boo's mansion. Since it is so dark, you cannot see a thing.
What do you do?

::Valid Commands::
jump: A leap of faith
forward: Go forward
back: Go backwards
------------------------------
'''


jump_info = '''
------------------------------
You successfully stomped a Goomba, keeping your life as Mario! You are 
still in Boo's mansion. What do you do?

::Valid Commands::
run: Make a run for it
back: Go backwards
------------------------------
'''

forward_info = '''
------------------------------
You ran into a Goomba, losing your life as Mario.

GAME OVER
Press the Log Out button.
------------------------------
'''

back_info = '''
------------------------------
You find that King Boo is right behind you, covering his face while
being completely still! What do you do?

::Valid Commands::
turnaround: Turn around
------------------------------
'''

turnaround_info = '''
------------------------------
As you turn Mario around to continue, your mom begins calling you for
dinner. You turn off the Wii.

Press the Log Out button.
------------------------------
'''

run_info = '''
------------------------------
You end up sprinting to the finish line, grabbing onto the goal pole.
Mario celebrates to the camera.

COURSE CLEAR!
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
    while state != 'End' and (message not in ['jump','forward','back','run',
    'turnaround']):
            print("Invalid Command")
            return state
    if state in ['Start', 'Jump'] and message == 'back':
            print(back_info)
            return 'Boo'
    if state == 'Start':
        if message == 'jump':
            print(jump_info)
            return 'Jump'
        elif message == 'forward':
            print(forward_info)
            return 'End'
    elif state == 'Jump':
        if message == 'run':
            print(run_info)
            return 'End'
    elif state == 'Boo':
        if message == 'turnaround':
            print(turnaround_info)
            return 'End'