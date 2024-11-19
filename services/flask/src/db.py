from flask_redis import FlaskRedis
from dataclasses import dataclass, asdict
import pickle
import time
import datetime
import json


@dataclass
class User():
    name: str
    playing: bool
    login_timestamp: float


@dataclass
class Message:
    user: str
    content: str
    date: str


class RedisDB():
    """
    A DB interface using Redis
    """
    def __init__(self) -> None:
        self.redis = FlaskRedis()

    def get_user(self, name: str) -> User | None:
        """
        Get the `User` or none from Redis `users` list
        """
        users = self.redis.lrange("users", 0, -1)
        for user in users:
            user_deserialized = pickle.loads(user)
            if user_deserialized.name == name:
                return user_deserialized
        return None

    def set_user(self, name: str):
        """
        Set a new `User` in the Redis `users list
        """
        user = User(name=name, playing=True, login_timestamp=time.mktime(datetime.datetime.now().timetuple()))
        self.redis.lpush("users", pickle.dumps(user))

    def add_message(self, user: str, content: str):
        """
        Add a new `Message` in the Redis messages list and publish
        to the Redis `chat` channel
        """
        now = datetime.datetime.now().replace(microsecond=0).isoformat()
        message = Message(user=user, content=content, date=now)
        self.redis.rpush("messages", pickle.dumps(message))
        self.redis.publish("chat", pickle.dumps(message))

    def pub_listen(self):
        """
        Subscribe to the Redis `chat` channel
        """
        pubsub = self.redis.pubsub()
        pubsub.subscribe('chat')
        for message in pubsub.listen():
            if message['type'] == 'message':
                _message = pickle.loads(message["data"])
                yield f"data: {json.dumps(asdict(_message))}\n\n"

    def get_messages(self) -> list[Message]:
        """
        Get all the `Message`s from Redis
        """
        messages = self.redis.lrange("messages", 0, -1)
        return [pickle.loads(message) for message in messages]
