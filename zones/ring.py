start_info = '''
------------------------------
You are on a hike in the forest with your friends and you saw there is something shiny inside the woods.
But seems like you are the only one who notice that.

::Valid Commands::
Check: Go check what is that 
Ignore: Keep walking with your friends
Inform: Tell your friends that there is something inside the wood
------------------------------
'''
check_info = '''
------------------------------
You found out that there is a ring with a diamond! You can't blieve that! 

:: Valid Commands::
Inform: Tell your friends what you have found. 
Hide: pick up this ring into your pocket and keep walking with them. 
Ignore: you tell yourself "it's werid that someone lost this, I should just leave it here" and walk away.
------------------------------

'''
inform_info = '''
------------------------------
Everyone stop and walked back to see what is inside the wood, it is indeed a golden ring with diamond!
Your friends start to argue who should have that and they fall into a fight.
What you want to do?

::Valid Commands::
Flee: run away and get out of this situation.
Steal: get the diomond while everyone is fighting and run away.
Help: tryting to stop your friends fighting with each other and suggest we should have the ring together.
------------------------------
 '''

ignore_info = '''
------------------------------
You and your friends finished the hike near down and when you guys walk back, you didn't see the shiny item at the same spot. 
The adventure has ended. 

Press the Log Out button.
------------------------------
'''

hide_info = '''
------------------------------
You got the ring and none of your friends have found out.
You get back home and sell the ring and it turns out to be a vintage and it worth 100,000,000 dollars.
And you become super rich

That's the happinest end of this trip
Press the Log Out buttom.
------------------------------
'''

flee_info = '''
------------------------------
You get away the chaos and back home safely. 

That's the normal end of this trip
Press the Log Out buttom.
------------------------------
'''

help_info = '''
------------------------------
All your friends agree with this suggestion and you guys sold the ring together after the hike.
You got a good amount of money.

That's the general end of this story
Press the Log Out buttom.
------------------------------
'''

steal_info = '''
------------------------------
You get the ring and successfully, you run away from your friends while they are still fighting.
However, one of them shout out "He got the ring!" 
Everyone was looking at you right now
What you should do?

::Valid Commands::
Flee: Run away as fast as you can!
Throw: Throw away the ring and let the rest of your friend have it. 
Lie: Tell them there is actually no ring at all, and you didn't have it. 
------------------------------
'''

throw_info = '''
------------------------------
No one got the ring in the end, and everyone feel upset but that's probably for the best.

This is the end of this story,

Press the Log Out buttom.
------------------------------
'''

lie_info = '''
------------------------------
Everyone insist that you steal the ring and keep it yourself and they put the anger towards you, you have to confess
In the end, you lost all your friends.

This is the sad ending for this story.
Press the Log Out buttom.
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
        if message == 'Check':
            print(check_info)
            return 'Check'
        elif message == 'Ignore':
            print(ignore_info)
            return 'End'
        elif message == 'Inform':
            print(inform_info)
            return 'Inform'
        else:
            print("Not the right Command")
            return 'Start'
    
    elif state == 'Check':
        if message == 'Inform':
            print(inform_info)
            return 'Inform'
        if message == 'Hide':
            print(hide_info)
            return 'End'
        if message == 'Ignore':
            print(ignore_info)
            return 'End'
        else:
            print('Not the right command')
            return 'Check'
    
    elif state == 'Inform':
        if message == 'Flee':
            print(flee_info)
            return 'End'
        if message == 'Steal':
            print(steal_info)
            return 'Steal'
        if message == 'Help':
            print(help_info)
            return 'End'
        else:
            print('Not the right command')
            return 'Inform'
    
    elif state == 'Steal':
        if message == 'Flee':
            print(flee_info)
            return 'End'
        if message == 'Throw':
            print(throw_info)
            return 'End'
        if message == 'Lie':
            print(lie_info)
            return 'End'
        else:
            print('Not the right command')
            return 'Steal'
    
