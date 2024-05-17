# %%
# IMPORTS
import streamlit
import pandas as pd
import numpy as np

# http://ergast.com/mrd/
import requests
import json

# request from API

# %%

url = "http://ergast.com/api/f1/2021/results" + ".json"
r = requests.get(url)
json_data = r.json()
json_data

# #%%
# r.text
# #%%
# url = "http://ergast.com/api/f1/2008/results" + ".json"
# params = {"page": 1}

# while True:
#     response = requests.get(url, params=params)
#     data = response.json()
    
#     # Do something with the data
    
#     if "next" in data["links"]:
#         url = data["links"]["next"]
#         params = None
#     else:
#         break
# data

# %%
# json_data to pd dataframe

races_df = pd.json_normalize(
    json_data["MRData"]["RaceTable"]["Races"], meta=[["Circuit"], [""]]
)
races_df

# %%
# finishes_df = pd.json_normalize(json_data["MRData"]["RaceTable"]["Races"]["Results"][0])
# finishes_df
finishes_df = pd.json_normalize(json_data["MRData"]["RaceTable"]["Races"][0]["Results"], meta = ["MRData", "RaceTable", "season", "round"])
finishes_df

# %%

for index, row in races_df.iterrows():
    finishes_df = pd.json_normalize(row["Results"])
    finishes_df["season"] = row["season"]
    finishes_df["round"] = row["round"]
    finishes_df["raceName"] = row["raceName"]
    finishes_df["circuitId"] = row["Circuit.circuitId"]
    
finishes_df

# %%
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data_url = "https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/Seattle2014.csv"
data = pd.read_csv(data_url, index_col="date", parse_dates=True)

# Resample to daily frequency
daily = data.resample("D").mean()

# Create temperature blanket
fig, ax = plt.subplots(figsize=(8, 48))
ax.imshow([daily["temp"]], cmap="coolwarm", aspect="auto")
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Seattle 2014 Temperature Blanket")

# Display temperature blanket in Streamlit app
st.pyplot(fig)