

from flask import Flask, session, redirect, url_for, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room

from Game import Game

socketio = SocketIO()

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "gjr39dkjn344_!67#"

game = Game()


@socketio.on("joined", namespace="/world")
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    join_room(session.get("name"))
    game.user_login(session.get("name"), session.get("zone"))


@socketio.on("text", namespace="/world")
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    game.on_message(session.get("name"), message["msg"])


@socketio.on("left", namespace="/world")
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    leave_room(session.get("name"))
    game.user_leave(session.get("name"), session.get("zone"))


@app.route("/", methods=["GET", "POST"])
def index():
    """Login form to enter a zone."""
    if "name" in request.form:
        session["name"] = request.form["name"]
        session["zone"] = request.form["zone"]
        return redirect(url_for("world"))
    elif request.method == "GET":
        name = session.get("name", "")
        return render_template("index.html", name=name)


@app.route("/world")
def world():
    """Chat room. The user's name and zone must be stored in
    the session."""
    name = session.get("name", "")
    zone = session.get("zone", "")
    if name == "":
        return redirect(url_for("index"))
    return render_template("world.html", name=name, zone=zone)


socketio.init_app(app)

if __name__ == "__main__":
    socketio.run(app)

