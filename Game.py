from flask_socketio import SocketIO, emit, join_room, leave_room
import zones.hub, zones.zone1, zones.zone2

class Game:
    def __init__(self):
        self.active_users = {}
        self.modules = {'Hub':zones.hub, 'Zone 1':zones.zone1,
                        'Zone 2':zones.zone2}
        self.zone_users = {}
        for key in self.modules:
            self.zone_users[key] = []
        
        

    def user_login(self, user, zone):
        self.active_users[user] = True
        self.zone_users[zone].append(user)
        user_list = self.zone_users[zone]
        self.send_to_users(user_list, user + f" has entered {zone}.")
        for user in user_list:
            emit("update_userlist", '\n'.join(user_list), to=user)

    def user_leave(self, user, zone):
        del self.active_users[user]
        try:
            self.zone_users[zone].remove(user)
        except:
            pass
        user_list = self.zone_users[zone]
        self.send_to_users(user_list, user + f" has left {zone}.")
        for user in user_list:
            emit("update_userlist", '\n'.join(user_list), to=user)

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


    
