
start_info = '''
------------------------------
You're a security guard at a museum that houses dozens of priceless objects. 
You hear a group of thieves breaking into the museum! 
What do you do?

::Valid Commands::
Help: Run and try to find someone to help!
Confront: Confront the thieves on your own and try to stop them!
Alarm: Sound the museum's alarm!
------------------------------
'''

help_info = '''
------------------------------
You've created enough distance between yourself and the thieves.
What now?

::Valid Commands::
Police: Call the police so that they can come catch the thieves!
Guard: Look for another guard so that you can confront the thieves together!
------------------------------
'''

alarm_info = '''
------------------------------
You sounded the alarm and the thieves panic.
The thieves gather everything they have and start to escape!
What do you do now?

::Valid Commands::
Chase: Chase after the thieves!
Hide: Stay hidden and let someone else deal with them. They could be dangerous!
------------------------------
'''

chase_info = '''
------------------------------
You begin to chase after the thieves!
You see the thieves about to get in a car!
What do you do?

::Valid Commands::
Stop: Try to stop the thieves from getting to the getaway car!
Identify: Write down the thieves license plate info!
------------------------------
'''

confront_info = '''
------------------------------
You go to confront the thieves but realize they way outnumber you!
What do you do?

::Valid Commands::
Run: Run away from the thieves and look for help!
Fight: Fight the thieves! You're confident you can win!
------------------------------
'''

police_info = '''
------------------------------
You called the police and they arrived and arrested the thieves!
Problem solved!

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

guard_info = '''
------------------------------
You find another guard and together confront the thieves!
You're still outnumbered and the thieves escape with the priceless objects.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

hide_info = '''
------------------------------
You hide and the thieves get away!
Your boss isn't very happy with you...

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

identify_info = '''
------------------------------
You write down the thieves license plate info and the police are able to track them down!
All the stolen objects are returned to the museum!
Your boss is very proud of your work!

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

stop_info = '''
------------------------------
You try to stop the thieves car but don't make it in time!
The thieves escaped.
Your boss is disappointed, but at least you tried.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

fight_info = '''
------------------------------
You try to fight the thieves but lose horribly because you're outnumbered.
The thieves escape.

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
        state - current user state (string)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user (string)
    '''
    if state == 'Start':
        if message == 'Help':
            print(help_info)
            return 'Help'
        elif message == 'Confront':
            print(confront_info)
            return 'Confront'
        elif message == 'Alarm':
            print(alarm_info)
            return 'Alarm'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == "Confront":
        if message == "Run":
            print(help_info)
            return 'Help'
        elif message == "Fight":
            print(fight_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Confront'
    elif state == 'Help':
        if message == 'Police':
            print(police_info)
            return 'End'
        elif message == 'Guard':
            print(guard_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Help'
    elif state == 'Alarm':
        if message == 'Chase':
            print(chase_info)
            return 'Chase'
        elif message == 'Hide':
            print(hide_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Alarm'
    elif state == 'Chase':
        if message == 'Identify':
            print(identify_info)
            return 'End'
        elif message == 'Stop':
            print(stop_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Chase'
