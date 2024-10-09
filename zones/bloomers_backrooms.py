start_exposition = '''
------------------------------
Hello. As a member of the Backrooms Investigation Foundation 
(B.I.F.), you and your squadmates Jimbo, Billybob, Patrick and
Jeff are sent on a daily mission to patrol the endless expanses of 
The Backrooms. Crossing through the portal, your team is presented with 
3 hallways to choose from. Seeing this, your team splits up into groups, 
with you going by yourself. Decisions decisions...

::Valid Commands::
hallway 1: Go down hallway 1.
hallway 2: Go down hallway 2.
hallway 3: Go down hallway 3.
peace out: Turn around and call it a day.
------------------------------
'''

hallway_1 = '''
------------------------------
With your journey down the first hallway underway, all seems 
right at first. Just as you start to become comfortable with the endless 
recess lighting, however, a bloodcurdling scream is heard down a turn in 
the hallway to the left. What to do?

::Valid Commands::
investigate: Your curiosity gets the better of you as you 
decide to investigate the noise.
walk by: Knowing the dangers that lurk around, 
you decide to continue on your journey, ignoring the noise.
------------------------------
'''

hallway_2 = '''
------------------------------
After walking for only a few minutes, you come 
into a giant room containg an endless pit.  The gap is only about 10 feet
wide you figure, but there is also a thin strip of ground on one side you 
could try to crawl along.  Jump or crawl?

::Valid Commands::
jump:  Risk your luck and jump the gap. 
crawl along side: Play the safe route and crawl along the side.
------------------------------
'''

hallway_3 = '''
------------------------------
A strange sense of dread looms over you as you continue your journey
in the third hallway.  Entering the first room of this hallway, your suspicions
are correct as you see the body of your...
wait for it...
dramatic suspense...
hold it...
SQUADMATE JIMBO NOOOOOOOOO!
Overcome with grief, you decide to search his body to see if you can recover
anything usefulf for your journey ahead.

PRESS ENTER
------------------------------
'''

jump_option = '''
------------------------------
Deciding to test your athletic skills, you take the risk and jump the gap.
That Double Cheddar Chalupa you had this morning chose to work against
you, however, and you plunge to your death in the dark depth. 

PRESS ENTER
------------------------------
'''

crawl_the_side_option = '''
------------------------------
Though crawling seemed like the safer option, halfway through your butter 
fingers couldn't have afflicted you at a worse time. Your death
is a quick one as the darkness takes you.

PRESS ENTER
------------------------------
'''

investigate_option = '''
------------------------------
Peering around a corner of the room infront of you, a tall spindly 
figure disformed beyond recognition is stood over your squadmates 
Patrick and Jimbob. You let out a large gasp, alerting the creature.  
Faster than you can blink, the creature turns around, stares into your 
soul, and rips you to pieces.

PRESS ENTER
------------------------------
'''

walk_by_option = '''
------------------------------
From your years of experience, you realize its better to not become 
distracted in an environment like this. You push forward, yet something feels
off. After a few moments, you turn around to see a creature on all fours 
with razor sharp teeth sprint towards you. What do you do?

::Valid Commands::
hide: Find a corner room with a closet to hide from the monster.
run: Sprint as fast as you can away the creature.
------------------------------
'''

find_body_option = '''
------------------------------
Looking through the pockets and contents of Jimbo, you discover a few 
items which could be of use. They are as follows: an airhorn, a flare gun,
and some Peanut M&M's. You realize the script writer will only allow you
to take one item, so which one will it be?

::Valid Commands::
take airhorn: Who knows, maybe it'll come in handy if you get lost.
take flare: Looks useful as a defensive weapon.
take candy: You're kind of hungry not gonna lie.
------------------------------
'''

take_airhorn_option = '''
------------------------------
With your airhorn in hand, you continue on through the maze of rooms.
As a time passes by, you spot a creature attacking the rest of your 
squad, you press the airhorn and thankfully ward off the creature. The 
rest of you report back to base through the portal, ever somber as you 
morn Jimbo. 

PRESS ENTER
------------------------------
'''

take_flare_option = '''
------------------------------
Almost as soon as you take the flare, a giant dark figure springs upon
you and claws at your face. You kick it off just in time to make some
distance. As you shoot the flare at the creature, it shrieks in pain and
retreats back into The Backrooms. Realizing your team is in danger, you 
retreat back to the portal entrance and radio your team to come back.
Sadly, Jeff isn't so fourtunate to make it back either, adding to the death 
total.

PRESS ENTER
------------------------------
'''

take_candy_option = '''
------------------------------
I'm not even bother to write this part.  What did you expect how do you think
candy is gonna help you survive.  Candy = death.

PRESS ENTER
------------------------------
'''

hide_option = '''
------------------------------
Finding a locker in the room adjacent to you, you decide to hunker down 
for a time as you hear the creature run past you. Once a while has passed, 
you return to base and radio for your team to come back. Thankfully, everyone
is okay and you all celebrate a job well done.

PRESS ENTER
------------------------------
'''

run_option = '''
------------------------------
Though you make a valorant attempt, the beast is just too fast for you. Its 
teeth sink into your neck, killing you.

PRESS ENTER
------------------------------
'''

death_option = '''
------------------------------
HAHA U DEAD

PRESS LOG OUT
------------------------------
'''

escape_option = '''
------------------------------
CONGRATS YOU ESCAPED THE BACKROOMS

PRESS LOG OUT
------------------------------
'''

peace_out_option = '''
------------------------------
What come on that's so lame don't be like that.

Reconsider???
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
    print(start_exposition)
    return 'The story begins'

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
    if state == 'The story begins':
        if message == 'hallway 1':
            print(hallway_1)
            return 'Hallway 1'
        if message == 'hallway 2':
            print(hallway_2)
            return 'Hallway 2'
        if message == 'hallway 3':
            print(hallway_3)
            return 'Hallway 3'
        if message == 'peace out':
            print(peace_out_option)
            print('Select yes to reverse choice, no to continue with choice')
            return 'The story begins'
        if message == 'yes':
            print('Good choice')
            print(start_exposition)
            return 'The story begins'
        if message == 'no':
            print(':(')
            print('PRESS LOG OUT')
        else:
            print('Not an answer')
            return 'The story begins'
    elif state == 'Hallway 1':
        if message == 'investigate':
            print(investigate_option)
            return 'Death'
        if message == 'walk by':
            print(walk_by_option)
            return 'Walk by'
        else:
            print('Not an answer')
            return 'Hallway 1'
    elif state == 'Hallway 2':
        if message == 'jump':
            print(jump_option)
            return 'Death'
        if message == 'crawl along side':
            print(crawl_the_side_option)
            return 'Death'
        else:
            print('Not an answer')
            return 'Hallway 2'
    elif state == 'Hallway 3':
            print(find_body_option)
            return 'Find body'
    elif state == 'Find body':
        if message == 'take air horn':
            print(take_airhorn_option)
            return 'Escape'
        if message == 'take flare':
            print(take_flare_option)
            return 'Escape'
        if message == 'take candy':
            print(take_candy_option)
            return 'Death'
        else:
            print('Not an answer')
            return 'Find body'
    elif state == 'Walk by':
        if message == 'hide':
            print(hide_option)
            return 'Escape'
        if message == 'run':
            print(run_option)
            return 'Death'
        else:
            print('Not an answer')
            return 'Walk by'
    elif state == 'Death':
        print(death_option)
    elif state == 'Escape':
        print(escape_option)