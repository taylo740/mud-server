start_info ='''
------------------------------
It is a dark and stormy evening.
You hear a knock on your door. "I wonder who that is?" you think.
Looking through the peephole, you see a stranger. He looks suspicious.
What do you do?

::Valid Commands::
open: Open the door
close: Keep the door shut
------------------------------
'''

open_info = '''
------------------------------
You open the door and the stranger grins at you.
He takes something out of his pocket and offers it to you. It
is a wedge shape wrapped in paper.
Do you take it?

::Valid Commands::
accept: Take the package
refuse: Refuse it
------------------------------
'''

accept_info = '''
------------------------------
You take the package. Inside is a chunk of
cheddar cheese. You invite the stranger to share
it with you at your kitchen table, and you
become friends.

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

refuse_info = '''
------------------------------
You refuse the package. Who knows what could
be inside? Shutting the door in his face (and locking it),
you congratulate yourself for recognizing such an
obvious opportunity to be murdered. 

Your adventure is at an end.
Press the Log Out button.
------------------------------
'''

close_info = '''
------------------------------
You do not open the door. You don't know who this is.
It's getting late, though, and you're getting tired.
You decide to go to sleep. In the morning, you wake up
to a great surprise: the stranger is sitting at your kitchen
table!

What do you do?

::Valid Commands::
greet: Greet the stranger
kick: Kick the stranger out
------------------------------
'''

greet_info = '''
------------------------------
You say, "Good morning." He doesn't reply.
Instead, he takes a wedge shaped package out of his pocket and
offers it to you.

What do you do?

::Valid Commands::
accept: Take the package
refuse: Refuse it
------------------------------
'''

kick_info = '''
------------------------------
You say, "Get out of my house."
He quickly leaves. You shut the door as soon as he
steps out, and you remember to lock your door this time.
That was close!

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
        if message == 'open':
            print(open_info)
            return 'Open'
        elif message == 'close':
            print(close_info)
            return 'Close'
        else:
            print('Invalid Command')
            return 'Start'
        
    elif state == 'Open':
        if message == 'accept':
            print(accept_info)
            return 'End'
        elif message == 'refuse':
            print(refuse_info)
            return 'End'
        else:
            print('Invalid Command')
            return 'Open'
    
    elif state == 'Close':
        if message == 'greet':
            print(greet_info)
            return 'Greet'
        elif message == 'kick':
            print(kick_info)
            return 'End'
        else:
            print('Invalid Command')
            return 'Close'
        
    elif state == 'Greet':
        if message == 'accept':
            print(accept_info)
            return 'End'
        elif message == 'refuse':
            print(refuse_info)
            return 'End'
        else:
            print('Invalid Command')
            return 'Greet'
            
