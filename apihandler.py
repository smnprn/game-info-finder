import os

from requests import *
from datetime import datetime

games_endpoint = "https://api.igdb.com/v4/games?"
genres_endpoint = "https://api.igdb.com/v4/genres"
platforms_endpoint = "https://api.igdb.com/v4/platforms"
headers = {
    "Client-ID": os.environ['CLIENT_ID'],
    "Authorization": f"Bearer {os.environ['IGDB_AUTH']}"
}


class ApiHandler:
    def search_game(self, game_name):
        response = post(games_endpoint, headers=headers, data=f"fields *; where name = \"{game_name}\";")

        response_dictionary = response.json()[0]

        game_info = [response_dictionary['name'],
                     response_dictionary['summary'],
                     response_dictionary['first_release_date'],
                     response_dictionary['genres'],
                     response_dictionary['platforms'],
                     response_dictionary['total_rating']
                     ]

        return game_info

    def search_genre_name(self, genre):
        response = post(genres_endpoint, headers=headers, data=f"fields name; where id = {genre};")

        response_dictionary = response.json()[0]

        genre = response_dictionary['name']

        return genre

    def convert_genres_list(self, genres):
        genres_list = []

        for i in genres:
            genres_list.append(self.search_genre_name(int(i)))

        return genres_list

    def search_platform_name(self, platform):
        response = post(platforms_endpoint, headers=headers, data=f"fields name; where id = {platform};")

        response_dictionary = response.json()[0]

        platform = response_dictionary['name']

        return platform

    def convert_platforms_list(self, platforms):
        platforms_list = []

        for i in platforms:
            platforms_list.append(self.search_platform_name(i))

        return platforms_list
    def print_game_info(self, game_name):
        game_info = self.search_game(game_name)

        print(f"""
        Name: {game_info[0]}
        Summary: {game_info[1]}
        Release Date: {datetime.utcfromtimestamp(game_info[2]).strftime('%Y-%m-%d')}
        Genres: {self.convert_genres_list(game_info[3])}
        Platforms: {self.convert_platforms_list(game_info[4])}
        Rating: {round(game_info[5], 2)}
        """)
