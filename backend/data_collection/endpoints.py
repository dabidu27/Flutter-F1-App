from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from models import Drivers, DriversWithPoints, RaceData, ConstructorsStandings
from get_data import (
    getStandingsData,
    getChampionshipStandings,
    getLastRace,
    getNextRace,
    getConstructorsChampionshipStandings,
)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/last_race/standings", status_code=status.HTTP_200_OK, response_model=list[Drivers]
)
async def getStandings():

    drivers = await getStandingsData()
    driversResponse = []
    pos = 1
    for driver in drivers:
        driversResponse.append(Drivers(name=driver[0], team=driver[1], pos=str(pos)))
        pos += 1

    return driversResponse


@app.get(
    "/championship/standings",
    status_code=status.HTTP_200_OK,
    response_model=list[DriversWithPoints],
)
async def getChampionship():

    drivers = await getChampionshipStandings()
    driversResponse = []
    pos = 1
    for driver in drivers:
        driversResponse.append(
            DriversWithPoints(
                name=driver[0], team=driver[1], pos=str(pos), points=str(int(driver[2]))
            )
        )
        pos += 1

    return driversResponse


@app.get(
    "/championship/constructors/standings",
    response_model=list[ConstructorsStandings],
    status_code=status.HTTP_200_OK,
)
async def getConstructorsChampionship():

    constructors = await getConstructorsChampionshipStandings()
    constructorsResponse = []
    pos = 1
    for constructor in constructors:
        constructorsResponse.append(
            ConstructorsStandings(
                name=constructor[0], points=str(constructor[1]), pos=str(pos)
            )
        )
        pos += 1
    return constructorsResponse


@app.get("/last_race/data", response_model=RaceData, status_code=status.HTTP_200_OK)
async def fetchLastRaceData():

    lastRaceData = await getLastRace()
    return RaceData(
        name=lastRaceData[0],
        datePretty=lastRaceData[1],
        dateComputations=lastRaceData[2],
        timeComputations=lastRaceData[3],
    )


@app.get("/next_race/data", status_code=status.HTTP_200_OK, response_model=RaceData)
async def fetchNextRaceData():

    nextRaceData = await getNextRace()
    return RaceData(
        name=nextRaceData[0],
        datePretty=nextRaceData[1],
        dateComputations=nextRaceData[2],
        timeComputations=nextRaceData[3],
    )
