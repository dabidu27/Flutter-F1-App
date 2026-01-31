import fastf1 as f1
import pandas as pd
import asyncio

f1.Cache.enable_cache("fastf1_cache")


async def getStandingsData():

    return await asyncio.to_thread(_loadStandings)


def _loadStandings():

    session = f1.get_session(2025, "Abu Dhabi", "Race")
    session.load()

    top3 = session.results[:3][["FullName", "TeamName"]]
    driver1 = (top3.iloc[0, 0], top3.iloc[0, 1])
    driver2 = (top3.iloc[1, 0], top3.iloc[1, 1])
    driver3 = (top3.iloc[2, 0], top3.iloc[2, 1])

    return [driver1, driver2, driver3]
