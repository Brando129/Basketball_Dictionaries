# List of Dictionaries
players = [
    {
    	"name": "Kevin Durant",
    	"age":34,
    	"position": "Small Forward",
    	"team": "Phoenix Suns"
    },
    {
    	"name": "Jayson Tatum",
    	"age":24,
    	"position": "Small Forward",
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving",
    	"age":32, "position": "Point Guard",
    	"team": "Dallas Mavericks"
    },
    {
    	"name": "Damian Lillard",
    	"age":33, "position": "Point Guard",
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid",
    	"age":32, "position": "Power Foward",
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "",
    	"age":16,
    	"position": "P",
    	"team": "en"
    }
]


"""Create a constructor to accept a dictionary with a single player's
information instead of individual arguments for the attributes."""

"""Add an @class method called get_team(cls, team_list) that, given a
list of dictionaries populates and returns a new list of Player objects."""

class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    # def player_info(self):
    #     print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Tean: {self.team}")

    def __repr__(self):
        return "Player: {}, Age: {}, Position: {}, Team: {}".format(
            self.name, self.age, self.position, self.team)


    @classmethod
    def get_team(cls, team_list):
        pass


"""Given these variables, create Player instances for each of the following
dictionaries. Be sure to instantiate these outside the class definition, in
the outer scope."""

kevin = {
    	"name": "Kevin Durant",
    	"age":34,
    	"position": "small forward",
    	"team": "Phoenix Suns"
}
jayson = {
    	"name": "Jayson Tatum",
    	"age":24,
    	"position": "small forward",
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving",
    	"age":32, "position": "Point Guard",
    	"team": "Dallas Mavericks"
}


player_kevin = Player(kevin)
print(player_kevin)
player_jayson = Player(jayson)
print(player_jayson)
player_kyrie = Player(kyrie)
print(player_kyrie)


"""Write a for loop that will populate an empty list with Player objects
from the original list of dictionaries."""

new_team = []

for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)