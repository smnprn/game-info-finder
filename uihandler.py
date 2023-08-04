from apihandler import *

api_handler = ApiHandler()


class UiHandler:
    def start_main_loop(self):
        while True:
            game_name = self.ask_game_name()

            if game_name == "":
                break

            api_handler.print_game_info(game_name)

    def ask_game_name(self):
        game_name = input("Search a game: ")
        return game_name
