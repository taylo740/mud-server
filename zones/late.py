open_dialogue = '''
------------------------------
Oh no!! Your class starts at 9:00 AM this morning, but your alarms didn't go off!
It's 8:45 now, what are you going to do?

::Valid Commands::
Brush: Brush your teeth and get ready for class
Ready: Just get dressed and rush out the door
------------------------------
'''

brush_dialogue = '''
------------------------------
After brushing your teeth and getting ready, you're even later for class!
How are you going to get to class?

::Valid Commands::
Bus: Try to catch the bus
Run: Sprint to class
------------------------------
'''

ready_dialogue = '''
------------------------------
You throw some clothes on and you're ready for the day!
How are you going to get to class

::Valid Commands::
Bus: Try to catch the bus
Run: Sprint to class
------------------------------
'''

run_dialogue = '''
------------------------------
As you're running, you spy your bike and remember that you can bike to class!
What do you do?

::Valid Commands::
KeepRun: Continue trying to run to class
Bike: Grab your bike and cycle to class
------------------------------
'''

bus_dialogue = '''
------------------------------
You rush to the bus stop and barely get on before the doors close!
Phew, you made it!

::Valid Commands::
Ride: Ride the bus to class
------------------------------
'''

keep_run_dialogue = '''
------------------------------
As you race to class, you are forced to dodge people on the sidewalk, weaving left and right.
You get to the door, finally, and walk into class; sweaty, disheveled, and late

::Valid Commands::
Enter: Walk into class
------------------------------
'''

bike_dialogue = '''
------------------------------
You pedal faster and faster, speeding past the crowds of people.
You make it to class in record time and get to the bike rack just as the clock hits 8:58
Do you lock up your bike or rush into class?

::Valid Commands::
Lock: Lock up your bike
Leave: Walk into class
------------------------------
'''

ride_dialogue = '''
------------------------------
You calmly step off the bus, having taken a moment to breathe while you ride
You walk into class at 8:59; just barely on time, but present

Your journey to class is over
Press the Log Out button
------------------------------
'''

enter_dialogue = '''
------------------------------
You walk into class, looking like a mess but just barely on time


Your journey to class is over
Press the Log Out button
------------------------------
'''

leave_dialogue = '''
------------------------------
You leave your bike and walk into class, just barely on time


Your journey to class is over
Press the Log Out button
------------------------------
'''

lock_dialogue = '''
------------------------------
You spent a moment fumbling with your bike lock before finally wrapping it around the wheel
Your bike is secure, but you are now officially late for class

Your journey to class is over
Press the Log Out button
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
    print(open_dialogue)
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
    if state=="Start":
        if message=="Brush":
            print(brush_dialogue)
            return "Brush"
        elif message=="Ready":
            print(ready_dialogue)
            return "Ready"
        else:
            print("Invalid Command")
            return 'Start'
    elif ((state=="Brush") or (state=="Ready")):
        if message=="Bus":
            print(bus_dialogue)
            return "Bus"
        elif message=="Run":
            print(run_dialogue)
            return "Run"
        else:
            print("Invalid Command")
            return state
    elif state=="Bus":
        if message=="Ride":
            print(ride_dialogue)
            return "End"
        else:
            print("Invalid Command")
            return 'Bus'
    elif state=="Run":
        if message=="KeepRun":
            print(keep_run_dialogue)
            return("KeepRun")
        elif message=="Bike":
            print(bike_dialogue)
            return "Bike"
        else:
            print("Invalid Command")
            return 'Run'
    elif state=="KeepRun":
        if message=="Enter":
            print(enter_dialogue)
            return "End"
        else:
            print("Invalid Command")
            return 'KeepRun'
    elif state=="Bike":
        if message=="Lock":
            print(lock_dialogue)
            return "End"
        if message=="Leave":
            print (leave_dialogue)
            return "End"
        else:
            print("Invalid Command")
            return 'Bike'