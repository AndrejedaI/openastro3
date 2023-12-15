from pydantic import BaseModel


class PlanetsBaseSchema(BaseModel):
    sun: str
    waxingCrescent: str
    waningCrescent: str
    mercury: str
    venus: str
    mars: str
    jupiter: str
    saturn: str
    uranus: str
    neptune:str
    pluto:str