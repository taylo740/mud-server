from flask_socketio import SocketIO, emit, join_room, leave_room
import zones.dragon, zones.hw04

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
        self.modules = {"Dragon's Lair":zones.dragon,
                        'Homework 04':zones.hw04}
        self.zone_users = {}
        self.user_data = {}
        for key in self.modules:
            self.zone_users[key] = set()
        
        

    def user_login(self, user, zone):
        self.active_users[user] = True
        self.zone_users[zone].add(user)
        user_list = self.zone_users[zone]
        self.send_to_users(user_list, user + f" has entered {zone}.")
        if zone in self.modules:
            try:
                with Capturing() as output:
                    self.user_data[user] = self.modules[zone].enter_zone(user, None)
                captured = '\n'.join(output)
                emit("status", {'msg': captured}, to=user)
            except:
                self.user_data[user] = None
        

        

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
            try:
                with Capturing() as output:
                    self.user_data[user] = self.modules[zone].command(user, self.user_data[user], text)
                captured = '\n'.join(output)
                emit("status", {'msg': captured}, to=user)
            except:
                self.user_data[user] = None
        
        print("command by", user, text)


    
