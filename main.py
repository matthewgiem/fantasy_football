from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

# Connect to yahoo api
sc = OAuth2(None, None, from_file='oauth2.json')

# Get game object
gm = yfa.Game(sc, 'nfl')

leauges = gm.league_ids()
# print(leauges)

# League ID 423.l.363495
# Get the league object
lg = gm.to_league("423.l.363495")

# Get the team key
teamkey = lg.team_key()

# Get the team object
team = lg.to_team(teamkey)

# Get the team roster
roster = team.roster()
# print(roster)

# for r in roster:
#     print(f"Name: {r['name']}\nPlayer ID: {r['player_id']}")

# fa = lg.free_agents("CB")

# for r in fa:
#     print(f"Name: {r['name']}\nPlayer ID: {r['player_id']}")

# for x in lg.free_agents("CB"):
#     if x["name"] == "DaRon Bland":
#         print(f"{x['name']} ID is {x['player_id']}")

# the player we want DaRon Bland's ID is 34123


# find a player to drop on my team
# for x in roster:
#     if x["name"] == "Marvin Mims Jr.":
#         print(f"{x['name']} ID is {x['player_id']}")

# the player I wanna drop is 40090 Marvin Mims Jr.

# Drop player Marvin Mims Jr.
team.drop_player(40090)
team.add_player(34123)

# check to see if it went through
for x in roster:
    if x["name"] == "DaRon Bland":
        print("Success")

# team.add_and_drop_players(40090, 34123)

