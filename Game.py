from flask_socketio import SocketIO, emit, join_room, leave_room
import zones.dragon
import zones.bloomers_backrooms
import zones.descend
import zones.omar
import zones.soccer
import zones.guard
import zones.security
import zones.cave
import zones.conquest
import zones.alley
import zones.redeye
import zones.fool
import zones.major
import zones.caravan
import zones.baking
import zones.barbie
import zones.house
import zones.fall
import zones.doors
import zones.diamond
import zones.escape
import zones.hero
import zones.boo
import zones.escape2
import zones.ring
import zones.late

from io import StringIO 
import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

class Game:
    def __init__(self):
        self.active_users = {}
        self.legacy = ["Alley",
                        "Baking Competition",
                        "barbie dream house yasss (Sophie)",
                        "Bloomer's Backrooms (Noah)",
                        "Boo's Mansion",
                        "Caravan Encounter",
                        "Cave Zone"
                        "Diamond Heist",
                        "Descend the Mountain",
                        "Dungeon Conquest (Cristina)",
                        "Escape room",
                        "Escape room (Gia)",
                        "Fall Adventure",
                        "find a ring in the forest (Liv)",
                        "Fool's Lair (Jose)",
                        "Guard attack (Bailey)",
                        "Hero (maybe) (Mike)",
                        "House (Daniel)",
                        "Late for Class! An Adventure",
                        "Major Help Bot",
                        "Omar's Adventure (Omar)",
                        "RedEye's Cave",
                        "Soccer game",
                        "Security Guard",
                        "Three Doors Adventure (Nolan)"]
        self.modules = {"Alley":zones.alley,
                        "Baking Competition":zones.baking,
                        "barbie dream house yasss (Sophie)":zones.barbie,
                        "Bloomer's Backrooms (Noah)":zones.bloomers_backrooms,
                        "Boo's Mansion":zones.boo,
                        "Caravan Encounter":zones.caravan,
                        "Cave Zone":zones.cave,
                        "Diamond Heist":zones.diamond,
                        "Descend the Mountain":zones.descend,
                        "Dragon's Lair":zones.dragon,
                        "Dungeon Conquest (Cristina)":zones.conquest,
                        "Escape room":zones.escape,
                        "Escape room (Gia)":zones.escape2,
                        "Fall Adventure":zones.fall,
                        "find a ring in the forest (Liv)":zones.ring,
                        "Fool's Lair (Jose)":zones.fool,
                        "Guard attack (Bailey)":zones.guard,
                        "Hero (maybe) (Mike)":zones.hero,
                        "House (Daniel)":zones.house,
                        "Late for Class! An Adventure":zones.late,
                        "Major Help Bot":zones.major,
                        "Omar's Adventure (Omar)":zones.omar,
                        "RedEye's Cave":zones.redeye,
                        "Soccer game":zones.soccer,
                        "Security Guard":zones.security,
                        "Three Doors Adventure (Nolan)":zones.doors,
                        }
        self.zone_users = {}
        self.zone_data = {}
        self.user_data = {}
        for key in self.modules:
            self.zone_users[key] = set()
            try:
                self.zone_data[key] = self.modules[key].initialize_areas()
            except Exception as e:
                #print("Exception when initializing", key, e)
                self.zone_data[key] = {}
        
        

    def user_login(self, user, zone):
        if user not in self.user_data:
            stats = {'Health':100, 'Strength':5, 'Magic':0, 'Gold':50, 'Happiness':12}
            self.user_data[user] = {'inventory':{}, 'stats':stats, 'legacy':None}
            
        self.active_users[user] = True
        self.zone_users[zone].add(user)
        user_list = self.zone_users[zone]
        self.send_to_users(user_list, user + f" has entered {zone}.")
        if zone in self.modules:
            #try:
                with Capturing() as output:
                    if zone in self.legacy:
                        self.user_data[user]['legacy'] = self.modules[zone].enter_zone(user, None)
                    else:
                        state = self.modules[zone].enter_zone(user, self.user_data[user])
                        if isinstance(state, dict) and 'inventory' in state and 'stats' in state:
                            self.user_data[user]['inventory'] = state['inventory']
                            self.user_data[user]['stats'] = state['stats']
                            self.update_stats(user, state['stats'])
                        else:
                            print("Invalid state returned from enter_zone", state)
                    
                captured = '\n'.join(output)
                emit("status", {'msg': captured}, to=user)
            #except Exception as e:
                #self.user_data[user]['legacy'] = False
        

        

    def user_leave(self, user, zone):
        del self.active_users[user]
        try:
            self.zone_users[zone].remove(user)
        except:
            pass
        user_list = self.zone_users[zone]
        self.send_to_users(user_list, user + f" has left {zone}.")

    def get_active_users(self):
        return list(self.active_users.keys())
    
    def update_stats(self, user, stats):
        emit("stats_change", {"msg": stats}, to=user)

    def send_to_users(self, users, text):
        for user in users:
            emit("message", {"msg": text}, to=user)
            print("user", user, text)

    def on_message(self, user, text: str):
        if text.startswith("/w"):
            w, who, what = text.split(" ", 2)
            self.send_to_users([who, user], user + ' whispers: "' + what + '"')
        else:
            self.send_to_users(self.get_active_users(), user + ": " + text)

    def on_command(self, user, zone, text: str):
        if zone in self.modules:
            #try:
                with Capturing() as output:
                    if zone in self.legacy:
                        self.user_data[user]['legacy'] = self.modules[zone].command(user, self.user_data[user]['legacy'], text)
                    else:
                        state = self.modules[zone].command(user, self.user_data[user], text)
                        if isinstance(state, dict) and 'inventory' in state and 'stats' in state:
                            self.user_data[user]['inventory'] = state['inventory']
                            self.user_data[user]['stats'] = state['stats']
                            self.update_stats(user, state['stats'])
                        else:
                            print("Invalid state returned from command", state)

                captured = '\n'.join(output)
                emit("status", {'msg': captured}, to=user)
            #except Exception as e:
                #print("Exception occurred during command function", e)
                #self.user_data[user]['legacy'] = None
        
        print("command by", user, text)


    
