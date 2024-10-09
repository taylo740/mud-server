# User Messages

information = '''
---------------------------------------------------------------
After waking up at 9am on a Saturday morning, you get ready for an adventure with your friends.
You are picking the location and bringing a variety of donuts to share. 
Where would you like to go?

Valid Commands:
Cafe: Ask your friends to wear cute casual clothes, to take your fall pictures together.
Park: Ask your friends to bring a water bottle and their dogs for a long walk.
'''

Cafe_info = '''
---------------------------------------------------------------
You have picked up the donuts and just arrived at the cafe with your friends. 
Some drinks at this cafe will give you superpowers. What will you order?

Valid Commands:
Pumpkin Spice Latte: a fall favorite
Hot Apple Cider: a warm comforting drink
Hot Chocolate: a cold weather classic
'''

Latte_info = '''
---------------------------------------------------------------
You have recieved your pumpkin spice latte. 
You're superpower is invisibilty. 
Unfortanately you do not know how to manage your new power and are invisible in the fall pictures.

It is now Saturday evening and your adventure has concluded. 
Press the log out button below.
'''

Cider_info = '''
---------------------------------------------------------------
You have recieved your hot apple cider.
You're superpower is teleportation.
After you take your fall pictures with your friends, you use your new superpower to explore the world.
You also use your superpower to reduce travel time to class, work, and fun activities every day.

It is now Saturday evening and your adventure has concluded. 
Press the log out button below.
'''

Chocolate_info = '''
---------------------------------------------------------------
You have recieved your hot chocolate.
This is the only drink on the menu that does not recieve a superpower.
So you take your fall photos and head back to the cafe alone to study for your approaching midterm.
Would you like to order another drink?

Valid Commands:
Yes: You would like to order another drink, get more donuts, and hang out with your friends again.
No: You would not like to order another drink and just want to study.
'''

no_drink_info = '''
---------------------------------------------------------------
You have not ordered a drink and just finished studying. 

It is now Saturday evening and your adventure has concluded. 
Press the log out button below.
'''

Park_info = '''
---------------------------------------------------------------
You have picked up the donuts and just arrived at the park with your new golden retreiver puppy. 
You assume it will be a challenging walk with your friends because your new puppy gets easliy distracted.
What does your puppy choose to do?

Valid Commands:
Walk: Your puppy has decided to follow instructions in return for a treat. 
Bark: Your puppy sees a squirrel and wants to chase it.
Sit: Your puppy wants to be pet and meet the kids on the playground. 
'''

walk_info = '''
---------------------------------------------------------------
Congrats! Your puppy is not causing trouble and is following instruction. 
Let's reward him with part of a donut.
How many donuts do you have left?

Valid Commands: any single integer value
'''

bark_info = '''
---------------------------------------------------------------
Oh no! Your puppy is being very noisy and waking up the baby sleeping across the street.
You better keep walking to try to distract your puppy.

It is now Saturday evening and your adventure has concluded. 
Press the log out button below.
'''

sit_info = '''
---------------------------------------------------------------
Your puppy is very stubborn and doesn't want to go for a walk today.
Ask your friends to sit on a bench with you and enjoy the beautiful fall day.

It is now Saturday evening and your adventure has concluded. 
Press the log out button below.
'''

not_enough_donuts = '''
---------------------------------------------------------------
You do not have enough donuts to share with your puppy and have a peaceful walk.
Prepare for a shorter walk to keep your puppy pleased.

It is now Saturday evening and your adventure has concluded. 
Press the log out button below.
'''

enough_donuts = '''
---------------------------------------------------------------
Good job! You bought enough donuts to share with your friends and your puppy.
Enjoy your long peaceful walk in the beautiful fall weather!

It is now Saturday evening and your adventure has concluded. 
Press the log out button below.
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

    print(information)
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
        The next state for the user (sting)
    '''
    if state == 'Start':
        if message == 'Cafe':
            print(Cafe_info)
            return 'Cafe'
        elif message == 'Park':
            print(Park_info)
            return 'Park'
        else:
            print('Invalid Command')
            return 'Start'
    elif state == 'Cafe':
        if message == 'Pumpkin Spice Latte':
            print(Latte_info)
            return 'End'
        elif message == 'Hot Apple Cider':
            print(Cider_info)
            return 'End'
        elif message == 'Hot Chocolate':
            print(Chocolate_info)
            return 'Chocolate'
        else:
            print('Invalid Command')
            return 'Cafe'
    elif state == 'Park':
        if message == 'Walk':
            print(walk_info)
            return 'Walk'
        elif message == 'Bark':
            print(bark_info)
            return 'End'
        elif message == 'Sit':
            print(sit_info)
            return 'End'
        else:
            print('Invalid Command')
            return 'Park'
    elif state == 'Walk':
        if message == '0':
            print(not_enough_donuts)
            return 'End'
        elif message == '1':
            print(not_enough_donuts)
            return 'End'
        elif message == '2':
            print(not_enough_donuts)
            return 'End'
        elif message == '3':
            print(not_enough_donuts)
            return 'End'
        elif message == '4':
            print(not_enough_donuts)
            return 'End'
        elif message == '5':
            print(not_enough_donuts)
            return 'End'
        elif message == '6':
            print(enough_donuts)
            return 'End'
        elif message == '7':
            print(enough_donuts)
            return 'End'
        elif message == '8':
            print(enough_donuts)
            return 'End'
        elif message == '9':
            print(enough_donuts)
            return 'End'
        else:
            print('Invalid Command')
            return 'Walk'
    elif state == 'Chocolate':
        if message == 'Yes':
            print(Cafe_info)
            return 'Cafe'
        elif message == 'No':
            print(no_drink_info)
            return 'End'
        else:
            print('Invalid Command')
            return 'Chocolate'

