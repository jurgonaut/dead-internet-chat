
from flask import Blueprint, render_template, session, request, Response, redirect, jsonify, url_for
from src import db
from dataclasses import asdict

chat = Blueprint('chat', __name__)


@chat.route('/')
def index():
    """
    Homepage route
    """
    if session.get("username"):
        return redirect(url_for('chat.home'))
    return render_template('index.html')


@chat.route('/generate_chat', methods=["GET"])
def generate_chat():
    """
    Generate some dummy conversation
    """
    generated = [
        {"user": "John", "message": "Hey how are you doing?"},
        {"user": "Frank", "message": "I'm fine how are you?"},
        {"user": "John", "message": "I'm great, what's up?"},
        {"user": "Frank", "message": "Not much, just watching the Sopranos"},
        {"user": "John", "message": "Ah nice, I like that series too"},
        {"user": "Frank", "message": "Yeah it's one of the best"},
    ]

    for m in generated:
        db.add_message(m["user"], m["message"])

    return Response(status=200)


@chat.route('/fetch_chat', methods=['GET'])
def fetch_chat():
    """
    Fetch all the messages from Redis, used to load the conversation
    when the client joins.
    """
    messages = db.get_messages()
    return jsonify([asdict(message) for message in messages])


@chat.route('/send_message', methods=['POST'])
def message():
    """
    POST endpoint where the user sends the message
    """
    if not session.get("username"):
        return redirect(url_for('chat.index'))
    content = request.form['message']
    user = session['username']
    db.add_message(user, content)
    return Response(status=204)


@chat.route('/stream')
def stream():
    """
    Event stream connection that updates the user when a new message arrives
    """
    if not session.get("username"):
        return redirect(url_for('chat.index'))
    return Response(db.pub_listen(), mimetype="text/event-stream")


@chat.route('/chat')
def home():
    """
    The home rout that loads the chat template
    """
    if not session.get("username"):
        return redirect(url_for('chat.index'))
    return render_template('chat.html', name=session["username"])
