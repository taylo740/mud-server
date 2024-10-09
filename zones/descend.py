import random

start_info = '''
You enter the cave in the appalachian mountains! 🏔️
You're goal is to descend to the bottom of the mountain
As you enter the cave you notice a ledge that leads down a dim lit path!
You also notice a deep pond that could lead to another opening deeper in the mountain

You're Choices are:
Exit: Leave the cave and try to climb back down with the climbing gear you left there
Ledge: Slide across the ledge to reach the path on the other side 
Pond: Dive into the pond to see if theres something below it!
'''

exit_info = '''
You exit the cave to notice that all your 
climbing gear has mysteriously vanished!

You enter back into the cave!

'''

ledge_break_info = '''
The ledge broke on the way over!!!
You've fallen down and can no longer continue! 💀

GAME OVER!!!!!

'''

ledge_pass_info = '''
You successfully make it over the ledge
As you continue down the tunnel you notice 
a sack piece of gold and a sack of bread!

You can only carry one which will you choose:
Bread: You choose to carry the sack of bread with you 🍞
Gold: You choose to carry the sack of gold with you 🏆
'''

bread_info = '''
You chose to carry the bread with you,
as you wander down the cave you bump into a strange man.
At first the man begins to get into a fighting stance, 
but when he smells the bread he reaches for it and
proceeds to hug you tightly!

He is now your friend and takes you out of the cave!
'''

gold_info = '''
You chose to carry the gold with you,
as you wander down the cave you bump into a strange man.
The man begins to get into a fighting stance,
you try to bargain by giving him the bag of 
gold but he seems to not understand!

You are now fighting the main, what do you do:
Run: You try to run away from the man
Swing: You try swing the bag of gold at the man
Punch: You try to punch the man
'''

run_info = '''
You begin to run down the closest path,
eventually you lost the strange man,
but you are now at a cross roads:
The left path seems to have water, but you cant tell the depth once again!
The right path seems to be a tight and curved crevice with small ray of sun peaking through!

What do you do:
Left: Go left and try to go into the water
Right: Try to sneak through the crevice and escape!
'''

left_info = '''
You chose to go left, as you submerge into the water,
in an instnace you fall very fast down and our drowned by the water

GAME OVER!!!!
'''

right_info = '''
You manage to sneak through the cracks of the cave
and have succesfully escaped the cave!!

GAME OVER!!!!

'''
swing_info = '''
You chose to try and swing the bag of gold,
but forgot that you gave the bag away already!
In confusion you are knocked out and can no longer continue!

GAME OVER!!!!
'''

punch_info = '''
You punch the strange man, but he's super strong.
He starts fighting back, and you can no longer continue!

GAME OVER!!!!
'''

pond_info = '''
You dive deep into the pond, you notice nothing, just darkness
But! As you continue swimming you notice an opening!
And suddenly a hand pulls you out of the water!

He notices your desperation and decides to help you on your journey
Luckily for you, he's an expert in these caves and you make it out!
'''


def enter_zone(user, state):
    '''
    Purpose: Sets up the initial state of the user when they 
        first enter the adventure.s
    Parameters:
        user - the name of the user (string)
        state - currently unused (None)
    Return Value:
        The starting state value for the game (String)
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
        state - current user state (???)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user (String)
    '''
    if state == "Start":
        if message == "Exit":
            print(exit_info)
            return "Start"
        elif message == "Ledge":
            break_chance = random.randint(0,10)
            if(break_chance == 0):
                print(ledge_break_info)
                return "End"
            else:
                print(ledge_pass_info)
                return "Ledge Pass"
        elif message == "Pond":
            print(pond_info)
            return "End"
        else:
            print("Invalid Command")
            return 'Start'
    elif state == "Ledge Pass":
        if message == "Bread":
            print(bread_info)
            return "End"
        elif message == "Gold":
            print(gold_info)
            return "Fight"
        else:
            print("Invalid Command")
            return 'Ledge Pass'
    elif state == "Fight":
        if message == "Punch":
            print(punch_info)
            return "End"

        elif message == "Run":
            print(run_info)
            return "Run"

        elif message == "Swing":
            print(swing_info)
            return "End"

        else:
            print("Invalid Command")
            return "Fight"
            
    elif state == "Run":
        if message == "Left":
            print(left_info)
            return "End"
        
        elif message == "Right":
            print(right_info)
            return "End"
        
        else:
            print("Invalid Command")
            return "Run"
