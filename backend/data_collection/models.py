from pydantic import BaseModel


class Drivers(BaseModel):

    name: str
    team: str
    pos: str
