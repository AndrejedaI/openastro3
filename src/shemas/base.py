from pydantic import BaseModel
from planets import PlanetsBaseSchema
from zodiac import ZodiacBaseSchema


class PlanetsSchema(BaseModel):
    unicode:PlanetsBaseSchema
    images:PlanetsBaseSchema


class ZodiacSchema(BaseModel):
    unicode:ZodiacBaseSchema
    images:ZodiacBaseSchema


class ConfigSchema(BaseModel):
    planets:PlanetsSchema
    zodiacs:ZodiacSchema


class EventSchema(BaseModel):
    name: str
    location: str
    year: int
    month: int
    day: int
    hour: int = 0
    minutes: int = 0
    utc_minutes: int
    lat: float
    lon: float
