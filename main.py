from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

# Connect to yahoo api
sc = OAuth2(None, None, from_file='oauth2.json')

# Get game object
gm = yfa.Game(sc, 'nfl')

leauges = gm.league_ids()
print(leauges)

# League ID 423.l.363495
# Get the league object
lg = gm.to_league("423.l.363495")

# Get the team key
teamkey = lg.team_key()

# Get the team object
team = lg.to_team(teamkey)

# Get the team roster
roster = team.roster()
print(roster)