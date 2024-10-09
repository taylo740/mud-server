start_info = '''
------------------------------
You arrive at the Barbie Dreamhouse. Okay Gurl!! 
What should we explore first?

::Valid Commands::
upstairs: Hop up those steps in search of something fashionable.
main: Go snooping on the main floor.
pool: Go out the back door for a splash.
------------------------------
'''

upstairs_info = '''
------------------------------
Woah you stumbled into Barbie's ginormous closet! 
What do you try on?

::Valid Commands::
sneakers: Slip on those rad Jordans.
heels: Christian Louboutins. What else is there to say.
------------------------------
'''

main_info = '''
------------------------------
Oh Em Gee what does Barbie have going on around here?
Which room should we head into?

::Valid Commands::
left: Some delicious smells are coming from this way.
right: There's some wild music playing from that direction.
------------------------------
'''

pool_info = '''
------------------------------
WOOOO PARTY AT BARBIE'S POOL!!
First you have to select a swimsuit.

::Valid Commands::
patterned: Get crazy with that cheetah print girlie!
black: Simple, yet elegant. 
------------------------------
'''

kitchen_info = '''
------------------------------
Ayo you made it to Barbie's kitchen!
What are we cookin' up?

::Valid Commands::
coffee: Pulling out the cold brew and creamer.
mac: Tossing that easy mac into the microwave.
popcorn: Frying up the perfect movie snack.
------------------------------
'''

Ken_info = '''
------------------------------
OH NOOOO!!!! You walked right into Ken's room!!!
He's literally just playing an air guitar to music
coming from a speaker. He's so freaking embarrassed
and yells at you to get out!!!


Press the log out button you creep.
------------------------------
'''

coffee_info = '''
------------------------------
Girllllll I know that drink is fantastic.

Press the log out button because you deserve it queen.
------------------------------
'''

mac_info = '''
------------------------------
Ohhh heck nahhhh!!! You forgot to add water!!
You set your eyebrows on fire you weirdo!

Press the log out button because you look insane.
------------------------------
'''

popcorn_info = '''
------------------------------
Okay that was delicious, but what's that???
You've got kernels all stuck in your teeth

Press the log out button because nobody wants
to talk to you when you look like that.
------------------------------
'''

patterned_info = '''
------------------------------
Girl that is so last year!!
You offended every fashionista in attendance
at the party

Press the log out button because you're a loser.
------------------------------
'''

black_info = '''
------------------------------
Ugh what a classic look. Everyone is obsessed with you.

Press the log out button because you're perfect.
------------------------------
'''

sneakers_info = '''
------------------------------
Looking so fresh right now.

Press the log out button and go show off your new kicks.
------------------------------
'''

heels_info = '''
------------------------------
Okay they were hot at first but you're so clumsy
you fell over in those stilletos and broke your ankle.

Press the log out button and get in the ambulance.
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
        if message == 'upstairs':
            print(upstairs_info)
            return 'Upstairs'
        elif message == 'main':
            print(main_info)
            return 'Main'
        elif message == 'pool':
            print(pool_info)
            return 'Pool'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == 'Upstairs':
        if message == 'sneakers':
            print(sneakers_info)
            return 'End'
        elif message == 'heels':
            print(heels_info)
            return 'End'
        else:
            print('Invalid Command')
            return 'Upstairs'
    elif state == 'Pool':
        if message == 'patterned':
            print(patterned_info)
            return 'End'
        elif message == 'black':
            print(black_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Pool'
    elif state == 'Main':
        if message == 'left':
            print(kitchen_info)
            return 'Kitchen'
        elif message == 'right':
            print(Ken_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Main'
    elif state == 'Kitchen':
        if message == 'coffee':
            print(coffee_info)
            return 'End'
        elif message == 'mac':
            print(mac_info)
            return 'End'
        elif message == 'popcorn':
            print(popcorn_info)
            return 'End'
        else:
            print('Invalid Command')
            return 'Kitchen'
        
