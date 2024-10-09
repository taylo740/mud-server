start_info = '''
------------------------------
You have been entered into a baking competition with two friends, average Joe, and Peppermint Patty. 
As a team, you have to pick something to bake.

::Valid Commands::
Bake cookies: Tell team to bake cookies
Bake cake: Tell team to bake cake. 
Bake pastries: Tell team to bake pastries
Bake cupcakes: Tell team to bake cupcakes
------------------------------
'''

cookies_info = '''
------------------------------
You and your team can either make chewy or crispy cookies.
Which do you want to make?

::Valid Commands::
chewy: Add extra molasses to your cookie and bake for 15 minutes. 
crispy: Bake for an extra five minutes to achieve a crispier finish. 
------------------------------
'''
cookies_winner = '''
------------------------------
The cookies were perfection with just the right amount of chewiness.

You have won the competition. 
Please press the Log Out button. 
------------------------------
'''
cookies_loser = '''
------------------------------
The cookies turned out rock solid and the judges coudn't even bite into them. 
You and your team have been asked to leave.

Your team lost.  
Please press the Log Out button. 
------------------------------
'''
cake_info = '''
------------------------------
You chose to make a cake, but have limited time. 
You have to split the task between you and your friends.
Which person has the essential task to make the best cake?

::Valid Commands::
Me: You are in charge of the frosting.
Joe: Joe is in charge of the sponge cake.
Patty: Patty is in charge of the decorations.
'''

cake_winner = '''
------------------------------
The final result was a masterpiece. 
The judges ended up eating half of it. 
Your team wins. 

You have won the competition. 
Please press the Log Out button. 
------------------------------
'''

cake_loser = '''
------------------------------
The final result was horrendous. 
Your abomination made the judges cry bitter tears. 

Please exit the building and never bake again. 
Press the Log Out button. 
------------------------------
'''

pastries_info = '''
------------------------------
The judges are Danish and your teams creations reminded them of home. 
They go to Google Flights and purchase a ticket home while handing you the trophy.  

In case you did not realize, you won. 
Press the Log Out button. 
------------------------------
'''

cupcakes_info = '''
------------------------------
Your team chooses to make cupcakes and must decide on the toppings. 
Which toppings should they use?

::Valid Commands::
Berries: You are in charge of the frosting.
Chocolate sprinkles: Joe is in charge of the sponge cake.
'''

cupcake_winner = '''
------------------------------
The judges love berries and think that they work perfectly with the rest of the cupcake. 

You win!
Press the Log Out button. 
------------------------------
'''

cupcake_loser = '''
------------------------------
A judge is allergic to chocolate. 
The emergency medical team escorts him out. 
Why he is a baking comeptition judge is a very good question. 

Unfortunately, because of this, your team loses. 
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
        The starting state value for the game (???)
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
        state - the current user state (string)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user which determines 
        what decision they need to make next (string)
    '''
    if state == 'Start':
        if message == 'Bake cookies':
            print(cookies_info)
            return 'Bake cookies'
        elif message == 'Bake cake':
            print(cake_info)
            return 'Bake cake'
        elif message == 'Bake pastries':
            print(pastries_info)
            return 'Win'
        elif message == 'Bake cupcakes':
            print(cupcakes_info)
            return 'Bake cupcakes'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == 'Bake cookies':
        if message == 'chewy':
            print(cookies_winner)
            return 'End'
        elif message == 'crispy':
            print(cookies_loser)
            return 'End'
        else:
            print("Invalid Command")
            return 'Bake cake'
    elif state == 'Bake cake':
        if message == 'Me' or message == 'Joe':
            print(cake_winner)
            return 'End'
        elif message == 'Patty':
            print(cake_loser)
            return 'End'
        else:
            print("Invalid Command")
            return 'Bake cake'
    elif state == 'Bake cupcakes':
        if message == 'Berries':
            print(cupcake_winner)
            return 'End'
        elif message == 'Chocolate sprinkles':
            print(cupcake_loser)
            return 'End'
        else:
            print("Invalid Command")
            return 'Bake cupcakes'
