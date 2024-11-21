from locust import HttpUser, task, between
import random


class BasicUser(HttpUser):
    """
    Get words list form `svnweb` and use that for creating random usernames and messages.
    """
    wait_time = between(1, 5)

    def on_start(self):
        headers = {'User-Agent': 'CMozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'}
        word_url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = self.client.get(word_url, headers=headers)
        self.words = response.text.splitlines()
        self.login()

    def login(self):
        self.client.post("login", {"username": self.words.pop(random.randrange(len(self.words)))})

    @task
    def post_message(self):
        self.client.post("send_message", {"message": random.choice(self.words)})
