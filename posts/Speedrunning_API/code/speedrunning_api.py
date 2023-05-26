# %%
# https://www.speedrun.com/the_site/thread/rz4nv/1#di4rg
import srcomapi, srcomapi.datatypes as dt

api = srcomapi.SpeedrunCom()
api.debug = 1

# %%
# It's recommended to cache the game ID and use it for future requests.
# Data is cached for the current session by classname/id so future
# requests for the same game are instantaneous.
sms = api.search(srcomapi.datatypes.Game, {"name": "skyrim"})
sms

# %%
game = _[0]
game

# %%
game.categories

# %%
game.records

# %%
game.records[0].runs

# %%
# 'abbreviation', 'assets', 'boostDistinctDonors', 'boostReceived', 'categories', 'categories',
# 'created', 'data', 'derived_games', 'developers', 'discord', 'embeds', 'endpoint', 'engines',
# 'gametypes', 'genres', 'id', 'levels', 'links', 'moderators', 'moderators', 'name', 'names', 'platforms',
# 'publishers', 'records', 'records', 'regions', 'release_date', 'released', 'romhack', 'ruleset',
# 'variables', 'weblink'

game.categories[5]


# %%
# ['data', 'embeds', 'endpoint', 'id', 'links', 'miscellaneous', 'name',
# 'players', 'records', 'rules', 'type', 'variables', 'weblink']
any_rec = game.records[0]


# %%
# 'category', 'data', 'embeds', 'emulators', 'endpoint', 'game', 'level',
# 'links', 'platform', 'region', 'runs', 'runs', 'timing',
# 'values', 'video_only', 'weblink'

marriage_records_url = game.categories[5].data["links"][3]["uri"]
marriage_records_url


# %%

import requests
import json

api_response = requests.get("https://www.speedrun.com/api/v1/runs?category=xk9vl5vd&var-rn10jwd8=jq6k2o7l&var-onvj7gwn=21dr0e5q")
data = api_response.text
parse_json = json.loads(data)
parse_json
# %%
