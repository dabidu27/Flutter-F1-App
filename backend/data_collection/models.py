from pydantic import BaseModel


class Drivers(BaseModel):

    name: str
    team: str
    pos: str


class DriversWithPoints(BaseModel):

    name: str
    team: str
    pos: str
    points: str


class RaceData(BaseModel):

    name: str
    date: str
