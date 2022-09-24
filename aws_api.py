from flask import request
import requests
import uuid


class AwsApi():
    def __init__(self, artist_name):
        self.id = uuid.uuid4()
        self.artist = artist_name
        self.url = 'https://r74hdqbtee.execute-api.sa-east-1.amazonaws.com/the_best_of_them'

    def insert_db(self):
        dados = {"id": str(self.id), "artist": self.artist}

        result = requests.request('POST', self.url, json=dados)

        if result.status_code == 200:
            result = result.json()

            return {"id": self.id}
        else:
            return {"status": str(result.status_code)}
