from flask import Flask, request
from genius import GeniusApi
from aws_api import AwsApi
from flask_redis import FlaskRedis
import redis
import ast

app = Flask("The best of them")

redis_client = FlaskRedis(app)

redis_cache = redis.Redis(host='localhost', port=6379, db=0)


@app.route("/artist/<int:id>", methods=["GET"])
def index(id):

    cache = True if request.args.get('cache') in [None, "True"] else False

    # Registra no Cache do Redis
    if redis_cache.exists(id) == 1 and cache == True:
        dict_str = redis_cache.get(str(id)).decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        return mydata
    else:
        # Requisições na API Genius
        genius_api = GeniusApi(id)
        artist_name = genius_api.artist_name()
        top10 = genius_api.top_ten_songs_of_them()

        # Registra no AWS DynamoDB o artista pesquisado
        aws_api = AwsApi(artist_name)
        aws_api.insert_db()

        # Registra o resultado no cache do Redis e coloca um tempo de expiração de 7 dias
        redis_cache.set(id, str(top10))
        redis_cache.expire(id, 60*60*24*7)

    return top10


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
