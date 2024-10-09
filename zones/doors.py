start_info = '''
You fall into a room that has three different doors, and they are labeled 1-3. 
You are unable to climb your way out of this room and so you must choose a door
to try and find a different way out. Choose a door to enter.
Valid commands:
Door1: Open door one
Door2: Open door two 
Door3: Open door three
'''

door_one_info = '''
You have entered into a dark room. You can not tell what is in the room or how
large it is. What would you like to do?
Vaild commands:
Lights: turn on the lights to see what is in the room
Listen: keep listening in the dark to guess what is in the room safely 
Door: leave the room  
'''

door_two_info = '''
The room you enter has a mysterious box in the corner and a latch that opens
a cellar in the floor. You are unable to tell what is in the box until you
open it.
Would you like to open the latch, open the box, or leave the room and return to
the original room.
Valid commands:
Latch: Open the latch to the celler 
Box: Open the box 
Door: leave the room  
'''
door_three_info = '''
The room that you enter has a large chest in the corner and a large door to a 
dark room in the other corner that is being proped open by a large ladder.
Would you like to open the large chest or open the door to the room?
Chest: Open the chest 
Room: Open the room door 
Door: leave the room 
'''
lights_info = '''
The light that is turned on in the room is so bright that it makes it hard for
you to see. You hear a loud noise, and can feel your possesions being stolen 
from you and the light flickers off. You can now either choose to use your 
flashlight, which you had saved deep in your pocket, to investigate what took
your possesions, or you can turn around and go back out of the door without 
your possesions.
Valid commands:
Flashlight: turn on flashlight to investigate
Door: leave room 
'''
listen_info = '''
You stop and listen to see if there is anything else in the room and to assess
whether you are safe or not. You do not hear anything at first but you begin to
hear the sound of something walking toward you. You turn on your small
flashlight but it is too late. The beast attacks you. 
You were unable to escape the room. You have lost and the game is over. 
Click log out in order to start a new game.
'''
door_info = '''
You choose to exit the current room and return back to the room with the three
doors. Choose a new door to go into.
Valid commands:
Door1: Open door one
Door2: Open door two 
Door3: Open door three
'''
box_info = '''
Once you open the box, you find what seems to be a portal, maybe that could 
send you back to ground level? You notice there is a cord and an outlet and so 
you plug it in. However, the portal is not user friendly whatsoever and it 
causes you to get sucked into a black hole with no way to get out or to know
where you are headed. However there is an eject button. As a last resort you
press the button and are unfortunatly ejected into space. 
You have lost and the game is over. Click log out in order to start a new game.
'''
latch_info = '''
You open the latch to the cellar, which drops you into another room. However,
even though you are now even further under ground, you find a very large ladder
in the corner of this new room that is tall enough to escape out of the celler
and even out of the first room. You set up the ladder and are able to escape.
You have escaped the room and the game is over. You win! Click log out in order
to start a new game. 
'''
chest_info = '''
You open the chest and find three different tools: a mini trampoline, a 
cellphone and a trumpet. However, the chest begins to close before you are able
to pull all three items out of the chest. You must choose one item to take out
of the chest before it closes, and locks permanantly. 
Valid commands:
Trampoline: grab the trampoline 
Cellphone: grab the cellphone
Trumpet: grab the trumpet 
'''
room_info = '''
You enter the room through the door but accidentally kick the ladder that is
propping the door. The ladder gets pushed down to the floor and is pushed 
outside of the now locked room. Although the ladder could have been used to
escape, it is now unreachable. However, the room has a hallway that is
inclined. You follow the hallway around the many many corners until you
eventually make your way back to ground level. 
You have escaped the room and the game is over. You win! Click log out in order
to start a new game.
'''
trampoline_info = '''
You decide to grab the trampoline out of the chest. You test out the trampoline
and it seems to be bouncy enough to allow you to reach a ledge on the wall and
then attempt to rock climb out of the room. However, a spring falls out of the
trampoline and you are unsure how to fix it. However, the chest is now propped
open by a different part that fell off when you grabbed it. You may choose a 
different tool from the box.
Valid commands: 
Cellphone: grab the cellphone
Trumpet: grab the trumpet 
'''
trumpet_info = '''
You decide to grab the trumpet out of the chest. You blow into it and notice it
is really loud and could help attract a bystander to help you escape in some 
other way. You keep playing the trumpet until a person hears you. They approach
the original room with a large rope and pull you up to ground level. 
You have escaped the room and the game is over. You win! Click log out in order
to start a new game.
'''
cellphone_info = '''
You decide to grab the cellphone out of the chest. You turn on the cellphone
and notice it only has 2 percent of battery left. You attempt to call your 
friend for help but there is no service. You leave the room and attempt to pick
a different door. 
Valid commands:
Door1: Open door one
Door2: Open door two 


'''
flashlight_info = '''
You turn on the flashlight and it is very bright. You are now able to see what
else is in the room. You walk forward in order to continue investigating but
you never look down. There is a giant hole in the floor that seems to never end
and you accidentally fall through. You reach the bottom of the hole unharmed
but you have no way out. 
You were unable to escape the room. You have lost and the game is over. 
Click log out in order to start a new game. 
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
        if message == 'Door1':
            print(door_one_info)
            return 'Door1'
        elif message == 'Door2':
            print(door_two_info)
            return 'Door2'
        elif message == 'Door3':
            print(door_three_info)
            return 'Door3'
        else:
            print("Invalid command!")
            return 'Start'

    elif state == 'Door1':
        if message == 'Lights':
            print(lights_info)
            return 'Lights'
        elif message == 'Listen':
            print(listen_info)
            return 'Start'
        elif message == 'Door':
            print(door_info)
            return 'Start'
        else:
            print("Invalid command!")
            return 'Door1'

    elif state == 'Door2':
        if message == 'Box':
            print(box_info)
            return 'Start'
        elif message == 'Latch':
            print(latch_info)
            return 'Start'
        elif message == 'Door':
            print(door_info)
            return 'Start'
        else:
            print("Invalid command!")
            return 'Door2'

    elif state == 'Door3':
        if message == 'Chest':
            print(chest_info)
            return 'Chest'
        elif message == 'Room':
            print(room_info)
            return 'Start'
        elif message == 'Door':
            print(door_info)
            return 'Start'
        else:
            print("Invalid command!")
            return 'Door3'

    elif state == 'Chest':
        
        if message == 'Trampoline':
            print(trampoline_info)
            return 'Chest'
        elif message == 'Trumpet':
            print(trumpet_info)
            return 'Start'
        elif message == 'Cellphone':
            print(cellphone_info)
            return 'Start'
        else:
            print("Invalid command!")
            return 'Chest'
             
    elif state == 'Lights':
        if message == 'Flashlight':
            print(flashlight_info)
            return 'Start'
        elif message == "Door":
            print(door_info)
            return 'Start'
        else:
            print("Invalid command!")
            return 'Lights'
    
    
        
    
        

    
