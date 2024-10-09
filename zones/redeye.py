start_info = '''
------------------------------
You and your friends enter Red Eye's cave, a dark and eerie place. One of your friends looks like an Oompa Loompa and can't help much, while another is suffering from brain rot. There's a stream of water beside you and a trail that leads deeper into the cave. You hold a torch.
What do you want to do?

Options:
1. Walk the Trail
2. Swim down the stream
------------------------------
'''

def enter_zone(user, state=None):
    '''
    Purpose: Sets up the initial state of the user when they 
        first enter the adventure.
    Parameters:
        user - the name of the user (string)
        state - unused here, will be an integer to track the game progression (int)
    Return Value:
        The starting state value for the game (int)
    '''
    print(f"Welcome, {user}! Your adventure begins now.")
    print(start_info)
    return 1  #Initial state

def command(user, state, message):
    '''
    Purpose:
        Runs whenever the user types something into the command box.
        Determines if their command is valid and progresses the story.
    Parameters:
        user - the name of the user (string)
        state - current user state (int)
        message - the text of the user's command (string)
    Return Value:
        The next state for the user (int)
    '''
    
    #Recognize commands and return new states based on both the state and message
    if state == 1:  #Initial state
        if message == "1":
            print("You walk along the narrow trail, the air growing colder. After some time, you see two doors. Do you: 1. Open the left door 2. Open the right door")
            return 2
        elif message == "2":
            print("You jump into the stream and are quickly swept away. The current is strong, and you see a waterfall ahead. Do you: 1. Swim to shore 2. Go over the waterfall")
            return 3
        else:
            print("Invalid choice, please type '1' or '2'.")
            return 1  #Stay in the same state

    #State 2: Choosing a door
    elif state == 2:
        if message == "1":
            print("You open the left door and find a room filled with gold and jewels. Suddenly, the door locks behind you. You are trapped, but the treasure is yours. Do you: 1. Search for another exit 2. Sit down and admire the treasure")
            return 4
        elif message == "2":
            print("You open the right door and find a deep, dark pit. Before you can react, you are pushed in by an unseen force. You fall into the abyss.")
            return -1  #End game
        else:
            print("Invalid choice, please select 1 or 2.")
            return 2

    #State 3: Swimming in the stream
    elif state == 3:
        if message == "1":
            print("You swim to the shore just in time, avoiding the waterfall. You find yourself at the mouth of a cave. Do you: 1. Enter the cave 2. Climb up a nearby hill")
            return 5
        elif message == "2":
            print("You go over the waterfall, crashing into the water below. You are disoriented but alive.")
            return -1  #End game
        else:
            print("Invalid choice, please select 1 or 2.")
            return 3

    #State 4: Trapped with treasure
    elif state == 4:
        if message == "1":
            print("You search the room for another exit and find a hidden door behind a tapestry. You push it open and escape!")
            return -1  #End game
        elif message == "2":
            print("You sit down to admire the treasure. Days pass, and you realize no one is coming for you. You are trapped forever.")
            return -1  #End game
        else:
            print("Invalid choice, please select 1 or 2.")
            return 4

    #State 5: Cave or hill
    elif state == 5:
        if message == "1":
            print("You enter the cave and find strange, glowing crystals. As you touch one, you are transported to another world.")
            return -1  #End game
        elif message == "2":
            print("You climb up the hill and enjoy the view. The journey is over for now, but you have survived.")
            return -1  #End game
        else:
            print("Invalid choice, please select 1 or 2.")
            return 5