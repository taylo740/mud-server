#Messages

start_info = '''
------------------------------
Welcome to the dungeon.
The dungeon is infested with monsters, and it's your job
to defeat them all to keep the world safe.
Will you succeed in killing them all, die trying, or run away
and live as a coward?

::Valid Commands::
enter: Enter the dungeon
------------------------------
'''

enter_info = '''
------------------------------
You enter the dungeon.
How will you start your attack?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
'''

sword_slash_success_info = '''
------------------------------
Your attack was a success!
You sliced right through the monster's thick armor.
What is your next move?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
'''

sword_slash_failure_info = '''
------------------------------
Your attack was a failure.
Your sword failed to piece the monster's hard shell and
the monster pounced back at you.
What is your next move?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
''' 

poison_blast_success_info = '''
------------------------------
Your attack was a success!
The potion was a direct hit and the monster
staggers back in weakness.
What is your next move?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
'''

poison_blast_failure_info = '''
------------------------------
Your attack was a failure.
The monster deflected the potion with its
tail and hit it right back at you.
What is your next move?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
'''

triple_arrow_crossbow_success_info = '''
------------------------------
Your attack was a success!
Your arrows pieced the monster right in
its heart with incredible force.
What is your next move?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
'''

triple_arrow_crossbow_failure_info = '''
------------------------------
Your attack was a failure.
All three arrows missed their mark and the monster took
the opporunity to take a massive bite in your side.
What is your next move?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
'''

lightning_strike_success_info = '''
------------------------------
Your attack was a success!
Luck is on your side and the gods listened to
your plea. The monster is struck down.
What is your next move?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
'''

lightning_strike_failure_info = '''
------------------------------
Your attack was a failure.
Luck is not on your side and the gods decided
to smite you instead for your insolence.
What is your next move?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
'''

monster_defeated_info = '''
------------------------------
You defeated the monster!
Will you continue through the dungeon
or flee while you're still alive?

::Valid Commands::
continue: Progess through the dungeon and fight for your city
exit: Leave and risk the monsters escaping and destroying your city
------------------------------
'''

player_defeated_info = '''
------------------------------
The monster has defeated you.
You died with honor, fighting for your city
until the very end. The people will forever remember your valiance.

Click log out to end.
------------------------------
'''

continue_info = '''
------------------------------
You progress deeper into the dungeon.
You turn the corner and are faced with another
harrowing monster.
How will you start your attack?

::Valid Commands::
sword_slash: Strike the monster with your iron sword (Risk 1)
poison_blast: Weaken the monster with a splash potion (Risk 3)
triple-arrow_crossbow: Aim for the heart of the monster (Risk 5)
lightning_strike: Summon the gods to strike down the monster (Risk 10)
run_away: Shrink in your cowardice and exit the fight
------------------------------
'''

exit_info = '''
------------------------------
You leave the cave with your life intact.
Because of your inability to continue none of
the citizens show you any respect, and you
are forced into exile.

Click log out to end.
------------------------------
'''

run_away_info = '''
------------------------------
Like a coward, you selfishly flee the cave, leaving countless
monsters still in the dungeon ready to overrun the city. You don't
even bother returning to your home and seek refuge in a far
away valley to live a life of shameful solitude for the rest of
your days.

Click log out to end.
------------------------------
'''

continue_end_info = '''
------------------------------
Due to your valiance, courage, and strength, all of the monsters
have been felled at your hand. The city is now safe and you
may leave the dungeon. You earn the eternal respect of all
the citizens and are regarded as a hero for the rest of history.

Click log out to end.
------------------------------
'''

exit_end_info = '''
------------------------------
You flee the dungeon with your life intact, but it turns out
that you had already defeated all of the monsters. The citizens
praise your courage and strength for keeping the city safe, but
you know in your heart that you are still a coward.

Click log out to end.
------------------------------
'''


#Commands

import random

def enter_zone(user, state):
    '''
    Purpose: Sets up the initial state of the user when they 
        first enter the adventure.
    Parameters:
        user - the name of the user (string)
        state - currently unused (list: stage, hp, xp, monster hp, monster lvl)
    Return Value:
        The starting state value for the game (stage, player hp, player xp, monster hp, monster lvl, lvl 5 monsters defeated)
    '''
    print(start_info)
    local = ['Start', 100, 0, 50, 1, 0]
    return local

def print_stats(state): #Prints current player and monster statistics
    stats = f'''
    Player HP: {state[1]}
    Player XP: {state[2]}
    Monster HP: {state[3]}
    Monster LVL: {state[4]}
    '''
    print(stats, end= "")

def command(user, state, message):
    '''
    Purpose:
        Runs whenever the user types something into the command box.
        Determines if their command is valid and progresses the story if so.
    Parameters:
        user - the name of the user (string)
        state - current user state (list)
        message - the text of the user's command (string)        
    Return Value:
        The next state for the user (stage, player hp, player xp, monster hp, monster lvl, lvl 5 monsters defeated)
    '''
    
    if state[0] == 'Start':
        if message == 'enter':
            print(enter_info, end= "")
            local = ['Fight', 100, 0, 50, 1, 0]
            print_stats(local)
            return local
        else:
            print("Invalid command")
            local = ['Start', state[1], state[2], state[3], state[4], state[5]]
            return local

    if state[0] == 'Fight':
        if message == 'sword_slash':
            if  random.randint(1, 10) >= 2: #Attack success
                local = ['Fight', state[1], state[2], (state[3] - 10), state[4], state[5]] #Sets new monster hp
                if local[3] <= 0: #Checks if monster hp is 0 or less
                    local[0] = "Monster Defeated"
                    print(monster_defeated_info, end= "")
                    return local
                else:
                    print(sword_slash_success_info, end= "")
                    print_stats(local)
                    return local
            else: #Attack failure
                local = ['Fight', (state[1] - 10), state[2], state[3], state[4], state[5]] #Sets new player hp
                if local[1] <= 0: #Checks if player hp is 0 or less
                    local[0] = "Player Defeated"
                    local[1] = 0
                    print(player_defeated_info, end= "")
                    print_stats(local)
                    return local
                else:
                    print(sword_slash_failure_info, end= "")
                    print_stats(local)
                    return local

        elif message == 'poison_blast':
            if  random.randint(1, 10) >= 4: #Attack success
                local = ['Fight', state[1], state[2], (state[3] - 20), state[4], state[5]] #Sets new monster hp
                if local[3] <= 0: #Checks if monster hp is 0 or less
                    local[0] = "Monster Defeated"
                    print(monster_defeated_info, end= "")
                    return local
                else:
                    print(poison_blast_success_info, end= "")
                    print_stats(local)
                    return local
            else: #Attack failure
                local = ['Fight', (state[1] - 20), state[2], state[3], state[4], state[5]] #Sets new player hp
                if local[1] <= 0: #Checks if player hp is 0 or less
                    local[0] = "Player Defeated"
                    local[1] = 0
                    print(player_defeated_info, end= "")
                    print_stats(local)
                    return local
                else:
                    print(poison_blast_failure_info, end= "")
                    print_stats(local)
                    return local

        elif message == 'triple-arrow_crossbow':
            if  random.randint(1, 10) >= 6: #Attack success
                local = ['Fight', state[1], state[2], (state[3] - 50), state[4], state[5]] #Sets new monster hp
                if local[3] <= 0: #Checks if monster hp is 0 or less
                    local[0] = "Monster Defeated"
                    print(monster_defeated_info, end= "")
                    return local
                else:
                    print(triple_arrow_crossbow_success_info, end= "")
                    print_stats(local)
                    return local
            else: #Attack failure
                local = ['Fight', (state[1] - 35), state[2], state[3], state[4], state[5]] #Sets new player hp
                if local[1] <= 0: #Checks if player hp is 0 or less
                    local[0] = "Player Defeated"
                    local[1] = 0
                    print(player_defeated_info, end= "")
                    print_stats(local)
                    return local
                else:
                    print(triple_arrow_crossbow_failure_info, end= "")
                    print_stats(local)
                    return local

        elif message == 'lightning_strike':
            if  random.randint(1, 10) == 10: #Attack success
                local = ['Fight', state[1], state[2], (state[3] - 100), state[4], state[5]] #Sets new monster hp
                if local[3] <= 0: #Checks if monster hp is 0 or less
                    local[0] = "Monster Defeated"
                    print(monster_defeated_info, end= "")
                    return local
                else:
                    print(lightning_strike_success_info, end= "")
                    print_stats(local)
                    return local
            else: #Attack failure
                local = ['Fight', (state[1] - 60), state[2], state[3], state[4], state[5]] #Sets new player hp
                if local[1] <= 0: #Checks if player hp is 0 or less
                    local[0] = "Player Defeated"
                    local[1] = 0
                    print(player_defeated_info, end= "")
                    print_stats(local)
                    return local
                else:
                    print(lightning_strike_failure_info, end= "")
                    print_stats(local)
                    return local
        
        elif message == 'run_away':
            print(run_away_info, end= "")
            local = ["Player Defeated", state[1], state[2], state[3], state[4], state[5]]
            print_stats(local)
            return local
            
        else:
            print("Invalid command")
            local = ['Fight', state[1], state[2], state[3], state[4], state[5]]
            return local

    if state[0] == 'Monster Defeated':
        if (message != 'continue') and (message != 'exit'):
            print("Invalid Command")
            return state
        
        local = ["Fight", (state[1] + 20), state[2], state[3], state[4], (state[5])]
        #Checking monster level to set appropriate xp and monster hp
        if local[4] == 1: 
            local[2] += 5
            local[3] = 50
        elif local[4] == 2:
            local[2] += 20
            local[3] = 75
        elif local[4] == 3:
            local[2] += 50
            local[3] = 150
        elif local[4] == 4:
            local[2] += 100
            local[3] = 300
        elif local[4] == 5:
            local[2] += 200
            local[3] = 500
            
        #Checking player xp to set appropriate monster level
        if local[2] >= 500:
            local[4] = 5
            local[5] += 1 #If level 5 monster was defeated add 1 to counter
        elif local[2] >= 200:
            local[4] = 4
        elif local[2] >= 50:
            local[4] = 3
        elif local[2] >= 15:
            local[4] = 2
        elif local[2] >= 5:
            local[4] = 1

        #Making sure player hp is no more than 200
        if local[1] > 200:
            local[1] = 200

        if message == 'continue':
            if local[5] >= 4: #If 3 level 5 monsters were killed
                print(continue_end_info, end= "")
                print_stats(local)
                local[0] = "Player Defeated"
                return local
            else:
                print(continue_info, end= "")
                print_stats(local)
                return local
        elif message == 'exit':
            if local[5] >= 4: #If 3 level 5 monsters were killed
                print(exit_end_info, end= "")
                print_stats(local)
                local[0] = "Player Defeated"
                return local
            else:
                print(exit_info, end= "")
                local[0] = 'Player Defeated'
                print_stats(local)
                return local


    if state [0] == 'Player Defeated':
        print("Invalid Command. Click log out to end.")
        local = [state[0], state[1], state[2], state[3], state[4], state[5]]
        return local

        
                
            

