# %%
# CONSTANTS

import requests
import json
import urllib.parse  # encude urls

import numpy as np
import pandas as pd

base_url = "https://www.speedrun.com/api/v1/"

# %%
# Get all games with "Mario Kart 64" in the name (up to 200

game = "Mario Kart 64"

game = urllib.parse.quote_plus(game)

games_url = base_url + "games?name=" + game + "&max=20"
# GET /api/v1/games?name=Super%20Mario%20Bros

games_response = requests.get(games_url)
games_data = games_response.json()

for i in range(len(games_data["data"])):
    print(games_data["data"][i]["names"]["international"])

# %%
# get categories of game we want

categories_url = games_data["data"][0]["links"][3]["uri"]
categories_url

categories_response = requests.get(categories_url)
categories_data = categories_response.json()
categories_data

for i in range(len(categories_data["data"])):
    print(categories_data["data"][i]["name"])

categories_data
# %%
# get game + category

category_url = categories_data["data"][0]["links"][0]["uri"]
category_url

category_response = requests.get(category_url)
category_data = category_response.json()
category_data

# %%
# get records (top 3) for game + category
# https://github.com/speedruncomorg/api/blob/master/version1/games.md#get-gamesidrecords

records_url = category_data["data"]["links"][3]["uri"]
records_url

records_response = requests.get(records_url)
records_data = records_response.json()
records_data

for i in range(len(records_data["data"][0]["runs"])):
    print(records_data["data"][0]["runs"][i]["run"]["times"]["primary_t"])

# %%
# get leaderboard for game + category

leaderboard_url = category_data["data"]["links"][5]["uri"]
leaderboard_url

leaderboard_response = requests.get(leaderboard_url)
leaderboard_data = leaderboard_response.json()
leaderboard_data

for i in leaderboard_data["data"]["runs"]:
    print(i["run"]["times"]["primary_t"])

# %%
leaderboard_data["data"]["runs"]

# %%
# make leaderboard into dataframe
leader_temp = leaderboard_data["data"]["runs"]

leaderboard_df = pd.json_normalize(
    leader_temp,
    # leader_temp, record_path=["run", "players"],
    # meta=["run"]
)

leaderboard_df.columns

# %%
# put them in order submitted

leaderboard_df.sort_values(by=["run.date"], ascending=True, inplace=True)
leaderboard_df["run.date"]

leaderboard_df["run.category"].unique()

# %%
# https://github.com/speedruncomorg/api/blob/master/version1/runs.md

high = 0
leaderboard_df["calc_record"] = False

for index, row in leaderboard_df.iterrows():
    if row["run.times.primary_t"] > high:
        high = row["run.times.primary_t"]
        leaderboard_df.at[index, "calc_record"] = True

# %%
leaderboard_df[leaderboard_df["calc_record"] == True]

# %%
leaderboard_df[
    leaderboard_df["run.times.primary_t"] == leaderboard_df["run.times.primary_t"].min()
]
# %%
