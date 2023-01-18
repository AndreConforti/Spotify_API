import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3


def check_if_valid_data(df: pd.DataFrame) -> bool:

    # Verifica se o dataframe está vazio
    if df.empty:
        print("No songs downloaded. Finish execution")
        return False

    # Verifica a chave primária
    if pd.Series(df["played_at"]).is_unique:
        pass
    else:
        raise Exception("Primary Key Check is violated")

    # Verifica valores nulos
    if df.isnull().values.any():
        raise Exception("Null valued found")

    # Verifica se os horários das músicas tocadas são da data de ontem
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    timestamps = df["timestamp"].tolist()
    for timestamp in timestamps:
        if datetime.datetime.strptime(timestamp, "%Y-%m-%d") != yesterday:
            raise Exception("At least one of the returned songs does not come from within the last 24 hours")

    return True

# API do Spotify = https://developer.spotify.com/console/get-recently-played/?limit=&after=&before=

DATABASE_LOCATION = "sqlite:///my_layed_tracks.sqlite"
USER_ID = "2274c5vzd3p4pvzwu7mkup33q"
TOKEN = "BQB-zBqa_eRyBFJAI2z1rNCNc1LGFnTWK1OD2xT0MeEZoxvgq0w6jfwF0Y4EJjvlYtCGf_QffOPN5ZAiXGtKm8hB_w89X037Nd_MA6fkmJWSVmqmqtG84Y9LDxYxqVwjYpNQSEdVK-QYbyreJJ0Aedo0fFGwnXh1X98nbbxIAuDGMx4pvVhBX5S5B086wO_QLoa7S-tu"

if __name__ == "__main__":

    headers = {
        "Accept"       : "application/json",
        "Content-Type" : "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    # Queremos o tempo em Unix com milisegundos
    # Para isso, precisamos converter a data de ontem
    # Por que ontem?
    # Porque queremos as informações diariamente, e todos os dias queremos ver as músicas que foram
    # tocadas nas últimas 24 horas 
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers=headers)

    data = r.json()

    song_names, artist_names, played_at_list, timestamps = [], [], [], []

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][:10])

    song_dict = {
        "song_name"   : song_names,
        "artist_name" : artist_names,
        "played_at"   : played_at_list,
        "timestamp"   : timestamps
    }

    song_df = pd.DataFrame(song_dict, columns=["song_name", "artist_name", "played_at", "timestamp"])

    print(song_df)