from flask import Blueprint, Response
from src import db
from src import openai_client

bot = Blueprint('bot', __name__)


@bot.route("/bot-response", methods=["GET"])
def gpt_response():
    """
    Trigger a ChatGPT response
    """

    conversation = ""
    for message in db.get_messages():
        conversation += f"{message.user}: {message.content}"

    messages = []
    system_content = '''You are a member of an online chat board.
    You only respond in a few words.
    You act as an average redditor.
    Respond to the conversation between users'''

    messages.append({"role": "system", "content": system_content})
    messages.append({"role": "user", "content": conversation})

    response = openai_client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=messages,
                            max_tokens=1000,
                            temperature=0.5)

    db.add_message("bot", response.choices[0].message.content)
    return Response(status=200)
