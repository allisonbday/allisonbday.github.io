#%%
import numpy as np
import pandas as pd
import fastf1
import time
import logging

logging.getLogger("fastf1").setLevel(logging.ERROR)
logging.getLogger("fastf1.core").setLevel(logging.ERROR)
logging.getLogger("fastf1.logger").setLevel(logging.ERROR)


def pull_session_results(
    season, round_number, country, location, event_name, event_date, session_type
):  # in class 'self' is first arg ;)
    """Pull the results for a specific season, location, and session type
    Args:
        season (int): Season year (e.g. 1950, 2025)
        location (str): Location (e.g. "Singapore", "Monza", "Silverstone")
        session_type (str, optional): Session type (e.g., "Race", "Sprint", "Qualifying")
    Returns:
        pd.DataFrame: DataFrame containing session results
    """
    session = fastf1.get_session(season, location, session_type)

    # Only Pull Data We Want
    session.load(telemetry=False, weather=False, messages=False)
    session_results = session.results.reset_index(drop=True)

    # Direct Assign Columns
    session_results["Season"] = season
    session_results["RoundNumber"] = round_number
    session_results["Country"] = country
    session_results["Location"] = location
    session_results["EventName"] = event_name
    session_results["EventDate"] = event_date
    session_results["SessionType"] = session_type

    # Fastest lap calculation (minimal lines, no extra DataFrame copies)
    try:
        fastest_driver = session.laps.pick_fastest()["Driver"]
        session_results["got_fastest_lap"] = (
            session_results["Abbreviation"] == fastest_driver
        )
    except Exception as e:
        print(f"Error occurred while processing laps: {e}")
        session_results["got_fastest_lap"] = (
            np.nan
        )  # Default to NaN if there's an error

    return session_results


sessions_2023 = [[2023,
  1,
  'Bahrain',
  'Sakhir',
  'Bahrain Grand Prix',
  pd.Timestamp('2023-03-05 00:00:00'),
  'Race',
  True],
 [2023,
  2,
  'Saudi Arabia',
  'Jeddah',
  'Saudi Arabian Grand Prix',
  pd.Timestamp('2023-03-19 00:00:00'),
  'Race',
  True],
 [2023,
  3,
  'Australia',
  'Melbourne',
  'Australian Grand Prix',
  pd.Timestamp('2023-04-02 00:00:00'),
  'Race',
  True],
 [2023,
  4,
  'Azerbaijan',
  'Baku',
  'Azerbaijan Grand Prix',
  pd.Timestamp('2023-04-30 00:00:00'),
  'Sprint',
  True],
 [2023,
  4,
  'Azerbaijan',
  'Baku',
  'Azerbaijan Grand Prix',
  pd.Timestamp('2023-04-30 00:00:00'),
  'Race',
  True],
 [2023,
  5,
  'United States',
  'Miami',
  'Miami Grand Prix',
  pd.Timestamp('2023-05-07 00:00:00'),
  'Race',
  True],
 [2023,
  6,
  'Monaco',
  'Monaco',
  'Monaco Grand Prix',
  pd.Timestamp('2023-05-28 00:00:00'),
  'Race',
  True],
 [2023,
  7,
  'Spain',
  'Barcelona',
  'Spanish Grand Prix',
  pd.Timestamp('2023-06-04 00:00:00'),
  'Race',
  True],
 [2023,
  8,
  'Canada',
  'Montréal',
  'Canadian Grand Prix',
  pd.Timestamp('2023-06-18 00:00:00'),
  'Race',
  True],
 [2023,
  9,
  'Austria',
  'Spielberg',
  'Austrian Grand Prix',
  pd.Timestamp('2023-07-02 00:00:00'),
  'Race',
  True],
 [2023,
  9,
  'Austria',
  'Spielberg',
  'Austrian Grand Prix',
  pd.Timestamp('2023-07-02 00:00:00'),
  'Sprint',
  True],
 [2023,
  10,
  'Great Britain',
  'Silverstone',
  'British Grand Prix',
  pd.Timestamp('2023-07-09 00:00:00'),
  'Race',
  True],
 [2023,
  11,
  'Hungary',
  'Budapest',
  'Hungarian Grand Prix',
  pd.Timestamp('2023-07-23 00:00:00'),
  'Race',
  True],
 [2023,
  12,
  'Belgium',
  'Spa-Francorchamps',
  'Belgian Grand Prix',
  pd.Timestamp('2023-07-30 00:00:00'),
  'Sprint',
  True],
 [2023,
  12,
  'Belgium',
  'Spa-Francorchamps',
  'Belgian Grand Prix',
  pd.Timestamp('2023-07-30 00:00:00'),
  'Race',
  True],
 [2023,
  13,
  'Netherlands',
  'Zandvoort',
  'Dutch Grand Prix',
  pd.Timestamp('2023-08-27 00:00:00'),
  'Race',
  True],
 [2023,
  14,
  'Italy',
  'Monza',
  'Italian Grand Prix',
  pd.Timestamp('2023-09-03 00:00:00'),
  'Race',
  True],
 [2023,
  15,
  'Singapore',
  'Marina Bay',
  'Singapore Grand Prix',
  pd.Timestamp('2023-09-17 00:00:00'),
  'Race',
  True],
 [2023,
  16,
  'Japan',
  'Suzuka',
  'Japanese Grand Prix',
  pd.Timestamp('2023-09-24 00:00:00'),
  'Race',
  True],
 [2023,
  17,
  'Qatar',
  'Lusail',
  'Qatar Grand Prix',
  pd.Timestamp('2023-10-08 00:00:00'),
  'Race',
  True],
 [2023,
  17,
  'Qatar',
  'Lusail',
  'Qatar Grand Prix',
  pd.Timestamp('2023-10-08 00:00:00'),
  'Sprint',
  True],
 [2023,
  18,
  'United States',
  'Austin',
  'United States Grand Prix',
  pd.Timestamp('2023-10-22 00:00:00'),
  'Sprint',
  True],
 [2023,
  18,
  'United States',
  'Austin',
  'United States Grand Prix',
  pd.Timestamp('2023-10-22 00:00:00'),
  'Race',
  True],
 [2023,
  19,
  'Mexico',
  'Mexico City',
  'Mexico City Grand Prix',
  pd.Timestamp('2023-10-29 00:00:00'),
  'Race',
  True],
 [2023,
  20,
  'Brazil',
  'São Paulo',
  'São Paulo Grand Prix',
  pd.Timestamp('2023-11-05 00:00:00'),
  'Sprint',
  True],
 [2023,
  20,
  'Brazil',
  'São Paulo',
  'São Paulo Grand Prix',
  pd.Timestamp('2023-11-05 00:00:00'),
  'Race',
  True],
 [2023,
  21,
  'United States',
  'Las Vegas',
  'Las Vegas Grand Prix',
  pd.Timestamp('2023-11-18 00:00:00'),
  'Race',
  True],
 [2023,
  22,
  'Abu Dhabi',
  'Yas Island',
  'Abu Dhabi Grand Prix',
  pd.Timestamp('2023-11-26 00:00:00'),
  'Race',
  True]]

all_results = []

start_time = time.time()
for sess in sessions_2023:
    season, round_number, country, location, event_name, event_date, session_type, has_occurred = sess
    print(f"Processing: {season} {event_name} {session_type} ({len(all_results)+1}/{len(sessions_2023)})")
    results = pull_session_results(season, round_number, country, location, event_name, event_date, session_type)
    all_results.append(results)

elapsed_time = time.time() - start_time
final_results_df = pd.concat(all_results, ignore_index=True)
final_results_df.to_parquet("f1_session_results_2023.parquet", index=False)

print(f"Elapsed time: {elapsed_time:.2f} seconds")

#%%
import pandas as pd
import plotly.express as px

final_results_df = pd.read_parquet(r"C:\Users\User\OneDrive\Desktop\Blog\allisonbday.github.io\posts\Projects\F1Streamlit\1_optimize_code\data\f1_session_results_2023.parquet")


session_order_df = (
    final_results_df
    .sort_values(["RoundNumber", "SessionType"], ascending=[True, False])
    .drop_duplicates(subset=["Location", "SessionType"])
    .reset_index(drop=True)
)
session_order_df["session_order"] = session_order_df.index + 1
session_order_df[["RoundNumber", "Country", "EventName", "SessionType", "session_order"]].drop_duplicates()

# Merge back to main DataFrame
final_results_df = final_results_df.merge(
    session_order_df[["Location", "SessionType", "session_order"]],
    on=["Location", "SessionType"],
    how="left"
).sort_values(["session_order", "Position"])

final_results_df["TeamColor"] = "#" + final_results_df["TeamColor"]

final_results_df["points_earned"] = final_results_df.groupby("Abbreviation")["Points"].cumsum()
final_results_df[["RoundNumber", "Country", "EventName", "SessionType", "session_order"]].drop_duplicates().sort_values("session_order")

fig = px.line(
    final_results_df,
    x="session_order",
    y="points_earned",
    color="Abbreviation",
    line_group="Season",
    title="2023 F1 Season Points Progression by Driver",
    markers=True,
    labels={"points_earned": "Cumulative Points", "SessionType": "Session Type"},
)

abbr_color = final_results_df.set_index("Abbreviation")["TeamColor"].to_dict()

fig.update_traces(marker=dict(size=6), line=dict(width=2))
fig.update_layout(legend_title_text='Driver', legend=dict(itemsizing='constant'))
fig.update_traces(line=dict(color=abbr_color)) # Use the color mapping

fig.show()
# %%
abbr_color