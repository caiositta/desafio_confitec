from flask import request
import requests


class GeniusApi():
    def __init__(self, id):
        self.id = id
        self.access_token = {
            "access_token": "_7z-UML-_xiUQfu_rAhRrDf_VgP5xHKn4IGVs-nGVH6s8OhF6IbYXk8qWws9E_1N"}
        self.url = 'https://api.genius.com/'

    def top_ten_songs_of_them(self):
        result = requests.request(
            'GET', self.url+"artists/{}/songs?sort=popularity&per_page=10".format(self.id), json=self.access_token)

        if result.status_code == 200:
            result = result.json()

            music_list = []

            for song in result['response']['songs']:
                music_list.append(
                    {"music_name": song['full_title'], "popularity": song['stats']['pageviews']})

            return {"best_of_them": music_list}
        else:
            return {"status": str(result.status_code)}

    def artist_name(self):
        result = requests.request(
            'GET', self.url+"artists/{}".format(self.id), json=self.access_token)

        if result.status_code == 200:
            result = result.json()

            return result["response"]["artist"]["name"]
        else:
            return {"status": str(result.status_code)}
