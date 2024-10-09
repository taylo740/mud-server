start_info = ''' --------------------------------------------
You are walking in a dark alley way and a suspicious man approaches you.

Suspicious Man: Hey there, stranger. Interested in something that will change your life?

He seems to be holding 2 vials: one with a green liquid and one with a black liquid

No: Decline his offerings
Run: You are scared and decide to flee
Green: Try the green liquid
Black: Try the black liquid
Both: Drink a mix of both of them
'''

green = '''--------------------------------------------
You drink the green liquid and find your heart pumping faster, body getting warmer, and muscles tightening
You have developed super strength

Suspicious Man: Come follow me and test out your new found powers

Follow: You are curious about your power and decide to test out your abilities
Kill: You don't trust the man any longer and decide to kill him
'''

kill = '''--------------------------------------------
You shove the man into the wall and he is completely flattened to death
You go on to live a life as the strongest man alive
'''

follow = '''--------------------------------------------
The Suspicious Man leads you to an arena with an audience of thousands
You are given 2 options on things to fight

Bear: A typical bear you could find in the forest
Demon: A terrifying creature with wings, claws, and bloodlust
'''

bear = '''--------------------------------------------
Your new profound strength destroys the bear instantly
The crowd cheers and encourages you to go fight another bear or the demon

Bear: A typical bear you could find in the forest
Demon: A terrifying creature with wings, claws, and bloodlust
'''


demon = '''--------------------------------------------
After a back and forth, you find yourself with a missing right arm
You decide to try to finish it with one final move

Punch: Hit it with your hand
Kick: Hit it with your legs
'''
punch = '''--------------------------------------------
Your muscle memory kicks in and you 'strike' the demon with your missing right hand
The demon laughs at you and kills you
'''

kick = '''--------------------------------------------
You do a spinning kick and knock out the demon
The crowd roars your name and you become a feared foe within the arena

'''
black = '''--------------------------------------------
You find yourself beginning to turn into a dark alley way
It seems oddly familiar 
You run into the same man

Suspicious Man: Hey there, stranger. Interested in something that will change your life?

He seems to be holding 2 vials: one with a green liquid and one with a black liquid

No: Decline his offerings
Run: You are scared and decide to flee
Green: Try the green liquid
Inform: Tell him what had happened after you took the black liquid
Both: Drink a mix of both of them
'''
inform = '''--------------------------------------------
Suspicious Man: Let's team up to prevent tragedies from occurring

Yes: Accept his offer
No: Decline his offer
'''

black_yes = '''--------------------------------------------
You and the Suspicious Man decide to change the world and stop future tragedies from occurring
'''
black_no = '''--------------------------------------------
The Suspicious Man knocks you out and kills you
He determines the power of time travel is far too great for someone like you to have it
'''

run = '''--------------------------------------------
Congratulations! You live, but with the lingering thought of what those vials could do
'''

no1 = '''--------------------------------------------
Suspicious man: C'mon, I know you want it. Think about all the possibilities.

No: Decline his offerings again
Run: You are scared and decide to flee
Green: Try the green liquid
Black: Try the black liquid
Both: Drink a mix of both of them
'''

no2 = '''--------------------------------------------
Suspicious Man: DRINK THE VIALS!!

No: You continue to refuse
Drink: You give into the man and drink up
'''

both_drinks = '''--------------------------------------------
You cannot handle both the drinks and explode
''' 

no_both = '''--------------------------------------------
Due to your continuous refusal, he forces you drink every single vial

You cannot handle the drink and you explode
'''

end = '''
Game is finished, logout for a rerun
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
        if message == 'No' or message == 'no':
            print(no1)
            return 'No'
        elif message == 'Run' or message == 'run':
            print(run)
            print(end)
            return 'end'
        elif message == 'Green' or message == 'green':
            print(green)   
            return 'green'  
        elif message == 'Black' or message == 'black':
            print(black)
            return 'black'
        elif message == 'Both' or message == 'both':
            print(both_drinks)
            print(end)
            return 'end'
        else:
            return 'Start'

    elif state == 'No':
        while message == 'No' or message == 'no':
            print(no2)
            return 'No'
        if message == 'Run' or message == 'run':
            print(run)
            print(end)
        elif message == 'drink' or message == 'Drink':
            print(no_both)
            print(end)
            return 'end'
        elif message == 'Green' or message == 'green':
            print(green)   
            return 'green'  
        elif message == 'Black' or message == 'black':
            print(black)
            return 'black'
        else:
            return 'No'
        

    elif state == 'green':
        if message == 'kill' or message == 'Kill':
            print(kill)
            print(end)
            return 'end'
        elif message == 'follow' or message == 'Follow':
            print(follow)
            return 'follow_options'
        else:
            return 'green'
    
    elif state == 'follow_options':
        while message == 'bear' or message == 'Bear':
            print(bear)
            return 'follow_options'
        if message =='demon' or message == 'Demon':
            print(demon)
            return 'attack'
        else:
            print(follow)
            return 'follow_options'

    elif state == 'attack':
        if message == 'punch' or message == 'Punch':
            print(punch)
            print(end)
            return 'end'
        elif message == 'kick' or message == 'Kick':
            print(kick)
            print(end)
            return 'end'
        else:
            return 'attack'
    
    elif state == 'black':
        
        if message == 'inform' or message == 'Inform':
            print(inform)
            return 'inform_options'
        elif message == 'No' or message == 'no':
            print(no1)
            return 'No'
        elif message == 'Run' or message == 'run':
            print(run)
            print(end)
            return 'end'
        elif message == 'Green' or message == 'green':
            print(green)   
            return 'green' 
        elif message == 'Black' or message == 'black':
            print(black)
            return 'black' 
        elif message == 'Both' or message == 'both':
            print(both_drinks)
            print(end)
            return 'end'
        else:
            return 'black'

    elif state == 'inform_options':
        if message == 'yes' or message == 'Yes':
            print(black_yes)
            print(end)
            return 'end'
        elif message == 'no' or message == 'No':
            print(black_no)
            print(end)
            return 'end'
        else:
            return 'inform_options'

        

            
        