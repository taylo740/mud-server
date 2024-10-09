
start_info = '''
__________________________________________________________________
It is midnight and you've just arrived to the museum
from which you will attempt to steal the famous Lion's Eye Diamond.
How will you break in?

::Valid Commands::
vent: climb through the vents then repel down to grab the diamond from above
hallway: break through the front gate and sneak through the hallways
__________________________________________________________________
'''

vent_info = '''
__________________________________________________________________
You successfully find an entrance into the vents and 
navigate through them until you are direclty above the diamond. 
How will you steal it?

::Valid Commands::
replace: while grabbing the real diamond slide a fake one in its place
lasso: use your lasso to grab the diamond without leaving the vent
painting: lower yourself to the ground and take a less risky painting instead of the diamond
__________________________________________________________________
'''

hallway_info = '''
__________________________________________________________________
You successfully break into the museum and find the hallway with the diamond.
However, to your surprise, there is a web of lasers that will trigger an alarm.
How will you avoid the lasers?

::Valid Commands::
cut power: find the circuit box and cause a power outage in the museum
dodge: use your acrobatic skill to maneuver through the lasers 
painting: grab a painting to steal outside of the laser grid and give up on the diamond
__________________________________________________________________
'''

slip_info = ''' 
__________________________________________________________________
As you move to replace the real diamond, your hand slips and you drop 
the fake diamond. With no more weight, the pressure plate alarm alerts 
the security guard who catches you red-handed. 
__________________________________________________________________
''' 

lasso_info = '''
__________________________________________________________________
Suddenly all those years spent as a cowboy are paying off. You expertly 
snag the diamond with your lasso skills, and by the time the guard 
hears the alarm, you have already made your escape.
__________________________________________________________________
''' 

chase_info = '''
__________________________________________________________________
In a split second decision you decide taking a painting may be less risky.
As soon as you pry the painting off the wall you hear a loud "HEYY!!!" 
and the guard begins chasing you through the museum. You round the 
corner to the exit and see the exit gate being lowered.
What will you do?

::Valid Commands::
fight: turn around and fight the guard
throw: grab a nearby artifact at the gate
__________________________________________________________________
''' 

powerout_info = '''
__________________________________________________________________
You find the circuit box and manage to create a power outage!
With the diamond unprotected you stroll right throught the center of 
the room to grab it. But, when you go to leave you realize all the exits 
were electronic and you are now trapped in the museum. Atleast you're 
rich until the police find you in the morning!
__________________________________________________________________
''' 

acrobatic_info = '''
__________________________________________________________________
You channel the gymnastics classes you took years ago and after
2 cart-wheels, a great limbo performance, and some close calls,
you grab the diamond! With the diamond in hand you successfully 
do all your acrobatic moves backwards and find yourself exactly
one Lion's Eye Diamond richer!
__________________________________________________________________
''' 

fight_info = '''
__________________________________________________________________
You put the painting down and turn to face the guard. He laughs 
at your pitiful fighting stances as pepper sprays you. You feel
him slip handcuffs around your wrists through your own sobs.
__________________________________________________________________
''' 

escape_info = '''
__________________________________________________________________
Miraculously the artifact gets stuck under the closing gate, creating 
a gap just big enough for you to slide under. You hear the guard 
swearing in frustration from the other side of the gate as you 
make your getaway!
__________________________________________________________________
''' 








def enter_zone(user, state):
    '''
    Purpose: Sets up the initial state of the user when they 
        first enter the adventure.
    Parameters:
        user - the name of the user (string)
        state - currently unused (None)
    Return Value:
        The starting state value for the game (str)
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
        state - current user state (str)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user (str)
    '''
    if state == 'Start':
        if message == 'vent':
            print(vent_info)
            return 'Vent'
        elif message == 'hallway':
            print(hallway_info)
            return 'Hallway'
        else:
            print('Invalid command')
            return 'Start'
    elif state == 'Vent':
        
        if message == 'replace':
            print(slip_info) 
            return 'End'
        elif message == 'lasso':
            print(lasso_info) 
            return 'End'
        elif message == 'painting':
            print(chase_info)
            return 'Chase'
        else: 
            print('Invalid command')
            return 'Vent'
    elif state == 'Hallway':
        if message == 'cut power':
            print(powerout_info) 
            return 'End'
        elif message == 'dodge':
            print(acrobatic_info) 
            return 'End'
        elif message == 'painting':
            print(chase_info)
            return 'Chase'
        else:
            print('Invalid command')
            return 'Hallway'
    elif state == 'Chase':
        
        if message == 'fight':
            print(fight_info)
            return 'End'
        elif message == 'throw': 
            print(escape_info)
            return 'End'
        else:
            print('Invalid command') 
            return 'Chase'

    


    
