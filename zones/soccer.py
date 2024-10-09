
start_info = '''
------------------------------
You are playing a socer match and the score is tied 1-1 with only 
one minute left. You are running up the field with the ball when 
suddenly a defender gets in your way.

::Valid Commands::
dribble: Try to get around the defender yourself
pass: Try to pass the ball to a teammate
------------------------------
'''

dribble_info = '''
------------------------------
You attempt to fake out the defender but he bumps into you and steals
the ball. 

::Valid Commands::
chase: Try to catch up and steal the ball back
stay: Try to stay in good position and hope 
a teammate can get the ball back to you
------------------------------
'''

chase_info ='''
------------------------------
You managed to kock the ball away from the defender 
and it ends up with a teammate.

::Valid Commands::
space: Try to run into open space closer to the goal
call: Try to call for the ball back
------------------------------
'''

stay_info ='''
------------------------------
Your team failed to defend and the oppsoing team scored.

The game ended 2-1 in a loss.
Press the Log Out button.
------------------------------
'''

pass_info = '''
------------------------------
You pass the ball to your teammate as you run past the defender. 

::Valid Commands::
space: Try to run into open space closer to the goal
call: Try to call for the ball back
------------------------------
'''

space_info ='''
------------------------------
Your teammate passes the ball between two defenders into the open 
space you ran to. You have an opprotunity to shoot at the goalie.

::Valid Commands::
left: Try to shoot for the left of the goalie
right: Try to shoot for the right of the goalie
middle: Try to shoot over the goalie
------------------------------
'''

call_info ='''
------------------------------
The pass is wide and neither team can start an attack.

The game ends in a tie 1-1!
Press the Log Out Butoon
------------------------------
'''

tie_info ='''
------------------------------
The goalie dives to the right and blocks your shot!

The game ends 1-1 in a tie!
Press the Log Out button.
------------------------------
'''
score_info ='''
------------------------------
The goalie dived to the right as your ball sailed into the goal.

The game ends 2-1 in a win!
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
        if message == 'dribble':
            print(dribble_info)
            return 'Dribble'
        elif message == 'pass':
            print(pass_info)
            return 'Pass'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == 'Pass':
        if message == 'call':
            print(call_info)
            return 'Call'
        elif message == 'space':
            print(space_info)
            return 'Space'
        else:
            print("Invalid Command")
            return 'Pass'
    elif state == 'Space':
        if message == 'left':
            print(score_info)
            return 'Score'
        elif message == 'right':
            print(tie_info)
            return 'Tie'
        elif message == 'middle':
            print(score_info)
            return 'Score'
        else:
            print("Invalid Command")
            return 'Space'
    elif state == 'Dribble':
        if message == 'chase':
            print(chase_info)
            return 'Chase'
        elif message == 'stay':
            print(stay_info)
            return 'Stay'
        else:
            print("Invalid Command")
            return 'Dribble'
    elif state == 'Chase':
        if message == 'space':
            print(space_info)
            return 'Space'
        elif message == 'call':
            print(call_info)
            return 'Call'
        else:
            print("Invalid Command")
            return 'Chase'


        
