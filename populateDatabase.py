import json
from www.models import Player, Country, Match

data_file = open('./www/data/players.json')
players_json = json.load(data_file)

# Have to add team foreign key after the countries are populated
results = players_json["results"]
for _player in results["players"] :
    player_object = Player(player=_player["player"], position=_player["position"], dob=_player["dob"], goals=_player["goals"], club=_player["club"])
    player_object.save()

#-------------------
# Populate Countries
#-------------------
data_file = open('./www/data/countries.json')
countries_json = json.load(data_file)

results = countries_json["results"] # countries_json[8] is the results dictionary
for _country in results["countries"] : # for each country in countries list
    country_object = Country(country=_country["country"], goals=_country["goals"])
    country_object.save()


#--------------------------
# Finish Players Population
#--------------------------
# Add foreign key for team now that countries have been populared
results = players_json["results"]
for _player in results["players"] :
    player_object = Player.objects.get(player=_player["player"])
    player_object.team = Country.objects.get(country=_player["team"])
    player_object.save()

#--------------------------
# Finish Country Population
#--------------------------
# Need to add scorers and players now that the Players have been populated
results = countries_json["results"] # countries_json[8] is the results dictionary
for _country in results["countries"] : # for each country in countries list
    country_object.captain = Player.objects.get(player=_country["captain"], team=_country["country"])
    if _country["top_scorer"] :
        country_object.top_scorer = Player.objects.get(player=_country["top_scorer"], team=_country["country"])
    if _country["scorers"] :
        for _scorer in _country["scorers"] :
            country_object.scorers.add(Player.objects.get(player=_scorer["player"]))
    for _player in _country["players"] :
        country_object.players.add(Player.objects.get(player=_player["player"]))
    country_object.save()


#-----------------
# Populate Matches
#-----------------
data_file = open('./www/data/matches.json')
matches_json = json.load(data_file)

results = matches_json["results"] # countries_json[8] is the results dictionary
for _match in results["collection1"] : # for each country in countries list
    match_object = Match(match=_match["match"], country_one=Country.objects.get(country=_match["country_one"]), country_two =Country.objects.get(country=_match["country_two"]), scores=_match["scores"], penalties=_match["penalties"], man_of_the_match=Player.objects.get(player=_match["man_of_the_match"]), match_date=_match["match_date"], match_location=_match["match_location"])
    match_object.save()


