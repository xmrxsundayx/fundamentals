class Player:

    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]

    def print_player(self):
        print(f"Player name:{self.name}, Player age:{self.age}, Pos: {self.position}, Team: {self.team}")

    @classmethod
    def get_team(cls,players_data):
        players = []
        for player_info in players_data:
            if player_info["name"] and player_info["age"] and player_info["position"]and player_info["team"]:
                p = cls(player_info)
                players.append(p)
                for player in players:
                    # print(f"Player name:{player.name}, Player age:{player.age}, Pos: {player.position}, Team: {player.team}")
                    player.print_player()
        return players






# kevin = {
#     "name": "Kevin Durant",
#     "age": 34,
#     "position": "small forward",
#     "team": "Brooklyn Nets"
# }
# jason = {
#     "name": "Jason Tatum",
#     "age": 24,
#     "position": "small forward",
#     "team": "Boston Celtics"
# }
# kyrie = {
#     "name": "Kyrie Irving",
#     "age": 32, "position": "Point Guard",
#     "team": "Brooklyn Nets"
# }

# player_kevin = Player(kevin)
# # player_jason = Player(jason)
# # player_kyrie = Player(kyrie)

# player_kevin.print_player()
# print(Player.new_team)
# player_jason.print_player()
# player_kyrie.print_player()


# Given these variables, create Player instances
# for each of the following dictionaries. Be sure
# to instantiate these outside the class definition,
# in the outer scope.

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33, "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32, "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "",
        "age": 16,
        "position": "P",
        "team": "en"
    }
]

players = Player.get_team(players)

for player in players:
    print(player.name,player.age,player.position,player.team)