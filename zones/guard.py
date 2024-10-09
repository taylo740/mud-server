#Messages for each possible decision
import random
start_info = '''
------------------------------
You are faced down with a brutish guard carrying a meat cleaver in his left arm. 
You can sense a strong killing intent.

::Valid Commands::
talk: Try and talk the guard out of attacking you
attack: Attack the guard's right arm
run: Run away from the battle
------------------------------
'''

talk_info = '''
------------------------------
You try to de-escalate the situation.
However, the guard doesn't seem to care.
He takes another step forward.

::Valid Commands::
beg: Beg the guard for your life
run: Run away from the battle
------------------------------
'''

attack_info = '''
------------------------------
Which limb will you attack?

::Valid Commands::
right: Attack the guard's right arm
left: Attack the guard's cleaver arm
head: Go directly for the head
------------------------------
'''

right_info = '''
------------------------------
You attack the guard's right arm and cleave it clean off.
He uses the cleaver in his left arm to hack off your right leg.

::Valid Commands::
left: Attack the guard's cleaver arm
head: Go directly for the head
------------------------------
'''

right_left_info = '''
------------------------------
You attack the guard's left arm and cleave it clean off.
Unarmed, the guard screams in pain and runs off into the darkness.
Unable to continue your expedition, you decide to leave with your life.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

right_head_info = '''
------------------------------
Without your right leg, you cannot reach the guard's head.
The guard uses his remaining arm to brutally dismember you.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

beg_info = '''
------------------------------
The guard doesn't care about your whining.
You are brutally dismembered.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

run_info = '''
------------------------------
You attempt to run. Call the coin flip:

::Valid Commands::
heads
tails
------------------------------
'''

head_info = '''
------------------------------
You lunge to attack the guard's head. Call the coin flip:

::Valid Commands::
heads
tails
------------------------------
'''

head_success = '''
------------------------------
You perfectly cleave the guard's head from his shoulders.
He is dead before he hits the ground.
You take a mysterious artifact from his loincloth and decide to leave the dungeons and live another day.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

head_fail = '''
------------------------------
You leap to attack the guard's head, but you miscalculated your trajectory.
With his free hand he snatches your neck in midair.
You are brutally dismembered.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

run_success = '''
------------------------------
You manage to get away from the guard. You narrowly dodge a bear trap on the ground.
You escape the dungeon with your life.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

run_fail = '''
------------------------------
While attempting to run from the guard, you accidentally step into a bear trap.
You attempt to drag yourself forward, but in vain. The guard catches up and you are dismembered.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

left_info = '''
------------------------------
You attack the guard's left arm and cleave it clean off.
Unfortunately, he seems unfazed and grabs your neck with his massive free arm.
Your throat is brutally crushed.

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

def coin_flip():
    '''
    Purpose: to simulate the flip of a coin
    Return: returns a string 'heads' or 'tails' randomly
    '''
    coin = random.randint(0,1)
    if coin == 0:
        return 'heads'
    else:
        return 'tails'

def command(user, state, message):
    '''
    Purpose:
        Runs whenever the user types something into the command box.
        Determines if their command is valid and progresses the story if so.
    Parameters:
        user - the name of the user (string)
        state - which decision point the user is currently in (string) <- not sure what the google doc wants me to do here
        but it's the same in my version of the program as the original because I thought a string made sense
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user, which determines what decision
        they will need to make next. (string)
    '''
    if state == 'Start':
        if message == 'talk':
            print(talk_info)
            return 'Talk'
        elif message == 'attack':
            print(attack_info)
            return 'Attack'
        elif message == 'run':
            print(run_info)
            return 'Run'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == 'Talk':
        if message == 'beg':
            print(beg_info)
            return 'End'
        elif message == 'run':
            print(run_info)
            return 'Run'
        else:
            print("Invalid Command")
            return 'Talk'
    elif state == 'Run':
        coinflip_temp = coin_flip()
        if (message != 'heads') and (message != 'tails'):
            print("Invalid Command")
            return 'Run'
        elif message == coinflip_temp:
            print(run_success)
            return 'End'
        else:
            print(run_fail)
            return 'End'
    elif state == 'Attack':
        if message == 'right':
            print(right_info)
            return 'Right'
        elif message == 'left':
            print(left_info)
            return 'End'
        elif message == 'head':
            print(head_info)
            return 'Head'
        else:
            print("Invalid Command")
            return 'Attack'
    elif state == 'Head':
        coinflip_temp = coin_flip()
        if (message != 'heads') and (message != 'tails'):
            print("Invalid Command")
            return 'Head'
        elif message == coinflip_temp:
            print(head_success)
            return 'End'
        else:
            print(head_fail)
            return 'End'
    elif state == 'Right':
        if message == 'left':
            print(right_left_info)
            return 'End'
        elif message == 'head':
            print(right_head_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Right'


        
