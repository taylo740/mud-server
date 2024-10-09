start_info = '''
------------------------------
You have completed your freshmen year at CSE and you 
still can not decide what your major is. You feel anxious
about your future. But don't give up, because I, Bot
Chuckles, will help you decide. Please, select what
subject you like the most in these three.

::Valid Commands::
Chemistry: You love to know how things are created
Mathematics: You love to think logically
Physics: You love to understand how things interact
------------------------------
'''

chem_info = '''
------------------------------
Wow, you sure love to know how those little elements
form this universe. Interesting! Now, do you like to
be an engineer or not?

::Valid Commands::
Yes: I love to create things!
No: I love the theory behind chemistry
------------------------------
'''

yes_chem_info = '''
------------------------------
I think I got the an idea of what you should major in!
Consider these three: Biomedical Engineering; Chemical
Engineering; Material Science and Engineering.
If you love helping people then choose the first
option. If you love chemistry experiments, choose the
second option. If you love create new things, choose
the last option.

I hope this help you, good luck on your journey!
------------------------------
'''

no_chem_info = '''
------------------------------
Really interesting! The perfect major for you
is definitely Chemistry. You might become a
professor in the future if you do research!

I hope this help you, good luck on your journey!
------------------------------
'''

math_info = '''
------------------------------
We have a math person right here! Now, tell
me, you like to explore math purely or apply
the math into practical situations.

::Valid Commands::
Think: You love math theorem, you read math book
for fun
Applied Math: You want to solve real world problem
------------------------------
'''

think_math_info = '''
------------------------------
Then your perfect major is simply Mathematics.
You don't have to think much, just follow your
heart!

I hope this help you, good luck on your journey!
------------------------------
'''

app_math_info = '''
------------------------------
Great! Now think about where do you want to
apply the math. Is it on the computer or real
life situations?

::Valid Commands::
Computer: You love solving problems on a computer
Use Math: You just want to use math everywhere in
daily life
------------------------------
'''

comp_app_math_info = '''
------------------------------
Then your perfect major is simply Computer Science
or Data Science. You don't have to think much, just
follow your heart!

I hope this help you, good luck on your journey!
------------------------------
'''

use_app_math_info = '''
------------------------------
Then your perfect major is simply Mathematics.
There are a lot of programs in the Math department
that allows you to learn applied math.

I hope this help you, good luck on your journey!
------------------------------
'''

phys_info = '''
------------------------------
Great! Now do you want to learn more about theories
or you love to create things.

::Valid Commands::
Theory: You just need to know more about Physics
theory
Applied Phys: I want to use physics fundementals
to create things or solve real world problem
------------------------------
'''

theo_phys_info = '''
------------------------------
Then your perfect major is simply Physics or Astrophysics.
You don't have to think much, just follow your
heart!

I hope this help you, good luck on your journey!
------------------------------
'''

app_phys_info = '''
------------------------------
Fantastic! Now do you want to work with a computer or
go out there work with the WORLDDDD?

::Valid Commands::
Computer: You love those electronics devices
Engineer: The world around you motivates you
------------------------------
'''

comp_app_phys_info = '''
------------------------------
Then your perfect major is simply Electrical Engineer
or Computer Engineer. A professor at UMN once said that
learning these two majors is like learning magic!

I hope this help you, good luck on your journey!
------------------------------
'''

eng_app_phys_info = '''
------------------------------
If you like construction, be a Civil Engineer
If you love how things move, be a Mechanical Engineer
If you love the environment, simply be a
Environmental Engineer

I hope this help you, good luck on your journey!
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
        if message == 'Chemistry':
            print(chem_info)
            return 'Chemistry'
        elif message == 'Mathematics':
            print(math_info)
            return 'Mathematics'
        elif message == 'Physics':
            print(phys_info)
            return 'Physics'
        else:
            print("Invalid Command")
            return 'Start'
    elif state == 'Chemistry':
        if message == 'Yes':
            print(yes_chem_info)
            return 'End'
        elif message == 'No':
            print(no_chem_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Chemistry'
    elif state == 'Mathematics':
        if message == 'Think':
            print(think_math_info)
            return 'End'
        elif message == 'Applied Math':
            print(app_math_info)
            return 'Applied Math'
        else:
            print("Invalid Command")
            return 'Mathematics'
    elif state == 'Applied Math':
        if message == 'Computer':
            print(comp_app_math_info)
            return 'End'
        elif message == 'Use Math':
            print(use_app_math_info)
            return 'End'
        else:
            print("Invalid Command")
            return 'Applied Math'
    elif state == 'Physics':
        if message == 'Theory':
            print(theo_phys_info)
            return 'End'
        elif message == 'Applied Phys':
            print(app_phys_info)
            return 'Applied Phys'
        else:
            print("Invalid Command")
            return 'Physics'
    elif state == 'Applied Phys':
        if message == "Computer":
            print(comp_app_phys_info)
            return 'End'
        elif message == "Engineer":
            print(eng_app_phys_info)
            return 'End'