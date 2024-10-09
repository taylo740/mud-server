start_info = '''
------------------------------
On your travel you come across a group of bandits attacking a caravan.
The caravan seems packed to the brim with goods.

::Valid Commands::
attack: Take the intiative and attack the bandits
join: Try to join the bandits for a share of the caravan
guards: Try to get a guard patrol's attention
leave: It's none of your business
------------------------------
'''

attack_bandit_info = '''
------------------------------
The bandits weren't expecting outsiders.
You have the advantage of surprise.

::Valid Commands::
charge: Charge straight into battle
sneak: Take the bandits by surprise
magic: Use magic to take out the bandits
------------------------------
'''

join_bandits_info = '''
------------------------------
The bandits seemed surprise at your appearance
but glady accepts your help.

::Valid Commands::
intimidate: Try to force the caravan to surrender
backstab: Betray the bandits and help the caravan
attack: Just attack the caravan
------------------------------
'''

guards_info = '''
------------------------------
You quickly find a roaming patrol
and told them about the caravan

::Valid Commands::
join: Follow the guards into battle
leave: You did your part, time to leave
------------------------------
'''

leave_caravan_info = '''
------------------------------
You left the caravan to its fate,
how do you feel "Hero"

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

charge_info = '''
------------------------------
You recklessly charged into battle
leaving you open to attacks from all sides.
You Died.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

sneak_info = '''
------------------------------
You successfully manage to sneak
into the bandit's rank and took out
the leader. The rest of the bandits flee,
the caravan rewarded you with 20 gold.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

magic_info = '''
------------------------------
The surprise magic attack kill many of the
bandits and caused the rest to flee.
The caravan rewarded you with 20 gold.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

intimidate_info = '''
------------------------------
You intimidated the caravan into surrending.
You get 30 gold as part of your share of the loot.


Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

backstab_info = '''
------------------------------
You managed to kill the bandit leader,
but instead of fleeing, the bandits were enraged
by your betrayal.
You Died.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

attack_caravan_info = '''
------------------------------
You joined the bandit in their assault,
the battle took too long and patrols of guards
stumbled onto the battle.
You were arrested and thrown into a dungeon.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

join_guards_info = '''
------------------------------
You joined the guards in the fight.
You managed to defeat the bandits
and were rewarded the title of a knight
for your deeds.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

leave_guards_info = '''
------------------------------
You leave after sending guards to
the caravan. It's fate is unkown
to you.

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
        state - currently unused (string)
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
        if message == 'attack':
            print(attack_bandit_info)
            return 'Attack Bandits'
        elif message == 'join':
            print(join_bandits_info)
            return 'Join Bandits'
        elif message == 'guards':
            print(guards_info)
            return 'Get Guards'
        elif message == 'leave':
            print(leave_caravan_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == 'Attack Bandits':
        if message == 'charge':
            print(charge_info)
            return 'End'
        elif message == 'sneak':
            print(sneak_info)
            return 'End'
        elif message == 'magic':
            print(magic_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Attack Bandits'
    elif state == 'Join Bandits':
        if message == 'intimidate':
            print(intimidate_info)
            return 'End'
        elif message == 'backstab':
            print(backstab_info)
            return 'End'
        elif message == 'attack':
            print(attack_caravan_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Join Bandits'
    elif state == 'Get Guards':
        if message == 'join':
            print(join_guards_info)
            return 'End'
        elif message == 'leave':
            print(leave_guards_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Get Guards'