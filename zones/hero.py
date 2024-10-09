start_info = '''
------------------------------
As you walk to get an ice cream, you encounter a criminal about to attack an innocent civilian.

::Valid Commands::
ice cream: It isn't your problem. Go get the ice cream you've been dreaming of.
run: Run away! Nothing you can do about it!
fight: Muster up the courage and prepare to fight.
save: Violence is not the answer. But I'm a good person right?
------------------------------
'''

ice_cream_info = '''
------------------------------
You turn right into the ice scream shop. There are three options: Chocolate, Strawberry, Vanilla.
Which one will you get?

::Valid Commands::
chocolate: Pick the chocolate flavor because it's the best.
strawberry: Pick the strawberry flavor because today is the day I'll try a different flavor.
vanilla: Pick the vanilla flavor because no one can mess up vanilla.
------------------------------
'''

goodicecream_info = '''
------------------------------
Yummy.
Best Day EVER.

Press the Log Out button.
------------------------------
'''

strawberry_info = '''
------------------------------
Ewwww. This flavor wasn't good at all.

Press the Log Out button.
------------------------------
'''

run_info = '''
------------------------------
You turn the other away and start to sprint as fast as you can. Not my problem.

Press the Log Out button.
------------------------------
'''

fight_info = '''
------------------------------
You cannot let this poor civilian be harmed. You choose to approach the criminal.
What is your first instinct?

::Valid Commands::
item: Look around for anything useful against the criminal.
charge: Go brawl against the criminal, I myself can take him down.
------------------------------
'''

save_info = '''
------------------------------
You remembered that you're not a fighter but wait...heroes don't have to fight.
You get ready ready to take action, what will you do?

::Valid Commands::
grab&go: Try to grab the civilian and run out of there.
police: Call the police.
------------------------------
'''

grab_and_go_info = '''
------------------------------
You run and grab the civilian before the criminal could even react.
How are you so fast? Then you remembered your parents are track stars.
The criminal was so stunned and amazed by your speed, he chooses to change his life for the better.

Press the Log Out button.
------------------------------
'''

stall_info = '''
------------------------------
You've called the police. Now you have to stall for time until the police gets here.
How would you do it?

::Valid Commands::
sing: Sing to try and get the attention of the criminal.
dance: Dance to try and get the attention of the crminal, altough, you aren't as good as you think.
------------------------------
'''

sing_info = '''
------------------------------
The vocals of your singing surprised the criminal. He starts cheering and clapping for you.
Finally the police arrives.

Press the Log Out button.
------------------------------
'''

dance_info = '''
------------------------------
The criminal starts laughing at how goofy you look dancing.
He falls to the ground holding his stomach, dying of laugther.
Finally the police arrives.

Press the Log Out button.
------------------------------
'''

item_info = '''
------------------------------
You look around and see two things: Baseball Bat, Wooden Stick
Which will you take?

::Valid Commands::
bat: Grab a bat to fight, luckliy you've played baseball before.
stick: Grab a stick, it is more agile.
------------------------------
'''

physical_info = '''
------------------------------
You choose to fight with what you were born with.
Should I go kick him or punch him?

::Valid Commands::
kick: Kicking is stronger but slower.
punch: Punching is faster but weaker.
------------------------------
'''

lose_info = '''
------------------------------
You landed an attack but he seems to be unfazed. Oh no!

Press the Log Out button.
------------------------------
'''

bat_info = '''
------------------------------
I knew it. The bat worked best. The criminal ran away rethinking his life decisions.

Press the Log Out button.
------------------------------
'''

punch_info = '''
------------------------------
Punching was the way to go! The criminal was scared of the blazing punches so he chose to surrender.
You've motivated him to become a better person. Maybe he'll go own a karate buisness one day.

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
        state - the current user state in the story (string)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user, which determines what decision
        they will need to make next. (string)
    '''
    if state == 'Start':
        if message == 'ice cream' or message == 'Ice Cream' or message == 'Ice cream' or message == 'ice Cream':
            print(ice_cream_info)
            return 'Icecream'
        elif message == 'run' or message == 'Run':
            print(run_info)
            return 'End'
        elif message == 'fight' or message == 'Fight':
            print(fight_info)
            return 'Fight'
        elif message == 'save' or message == 'Save':
            print(save_info)
            return 'Save'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == 'Icecream':
        if message == 'chocolate' or message == 'vanilla' or message == 'Chocolate' or message == 'Vanilla':
            print(goodicecream_info)
            return 'End'
        elif message == 'strawberry' or message == 'Strawberry':
            print(strawberry_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Icecream'
    elif state == 'Fight':
        if message == 'item' or message == 'Item':
            print(item_info)
            return 'Item'
        elif message == 'charge' or message == 'Charge':
            print(physical_info)
            return 'Physical'
        else:
            print("Invalid Command")
            return 'Fight'
    elif state == 'Item':
        if message == 'bat' or message == 'Bat':
            print(bat_info)
            return 'End'
        elif message == 'stick' or message == 'Stick':
            print(lose_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Item'
    elif state == 'Physical':
        if message == 'kick' or message == 'Kick':
            print(lose_info)
            return 'End'
        elif message == 'punch' or message == 'Punch':
            print(punch_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Physical'
    elif state == 'Save':
        if message == 'grab&go' or message == 'Grab&Go' or message == 'Grab&go' or message == 'grab&Go':
            print(grab_and_go_info)
            return 'End'
        elif message == 'police' or message == 'Police':
            print(stall_info)
            return 'Stall'
        else:
            print("Invalid Command")
            return 'Save'
    elif state == 'Stall':
        if message == 'sing' or message == 'Sing':
            print(sing_info)
            return 'End'
        elif message == 'dance' or message == 'Dance':
            print(dance_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Stall'
    
