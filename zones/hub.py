#Messages for each possible decision

start_info = '''
------------------------------
You sneak into the dragon's lair, with your comrades Wizard McBlastyFace 
and Stella the Bard.  The dragon is fast asleep.

::Valid Commands::
steal: Tell your team to start stealing things
tickle: Try to tickle the dragon on the nose
battle: Tell your team to prepare for battle
------------------------------
'''

steal_info = '''
------------------------------
You can't carry the entire hoard of loot.
What do you want to steal?

::Valid Commands::
gold: Take as much gold as you can carry
silk: Take the pile of fine silk in the corner
diamond: Take the huge diamond curled under the dragon's claw
------------------------------
'''

awake_info = '''
------------------------------
You trip over a rock and the dragon wakes up.
What do you do?

::Valid Commands::
sing: Direct Stella to sing for the dragon
charge: Charge directly at the dragon with your sword
flee: Run away down the hall
------------------------------
'''

battle_info = '''
------------------------------
Who will lead the attack?

::Valid Commands::
me: You will lead the way personally
mcblastyface: Direct your wizard friend to blast it from afar
stella: Have Stella distract it with a lullaby
------------------------------
'''

victory_info = '''
------------------------------
The dragon is so shocked by the stupidity of your attack that
it dies laughing.  You go home victorious!

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

getaway_info = '''
------------------------------
You successfully abscond with your loot.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

escape_info = '''
------------------------------
You leave the cave, terrified but unscathed.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

stella_info = '''
------------------------------
The dragon is impressed by Stella's performance and lets 
you each pick your favorite shiny thing to take home as a souvenir.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

wizard_info = '''
------------------------------
Wizard McBlastyFace aims a spell and misses horribly, hitting the ceiling.  
Rocks fall, everyone dies.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

sneeze_info = '''
------------------------------
The dragon sneezes out a fireball and incinerates you instantly.

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
        state - which decision point the user is currently in (string)
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
        state - which decision point the user is currently in (string)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user, which determines what decision
        they will need to make next. (string)
    '''
    if state == 'Start':
        if message == 'steal':
            print(steal_info)
            return 'Steal'
        elif message == 'tickle':
            print(sneeze_info)
            return 'End'
        elif message == 'battle':
            print(battle_info)
            return 'Battle'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == 'Steal':
        if message == 'gold' or message == 'silk':
            print(getaway_info)
            return 'End'
        elif message == 'diamond':
            print(awake_info)
            return 'Awake'
        else:
            print("Invalid Command")
            return 'Steal'
    elif state == 'Awake':
        if message == 'sing':
            print(stella_info)
            return 'End'
        elif message == 'charge':
            print(victory_info)
            return 'End'
        elif message == 'flee':
            print(escape_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Awake'
    elif state == 'Battle':
        if message == 'me':
            print(victory_info)
            return 'End'
        elif message == 'stella':
            print(stella_info)
            return 'End'
        elif message == 'mcblastyface':
            print(wizard_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Battle'


        
