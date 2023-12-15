from pydantic import BaseModel


class ZodiacBaseSchema(BaseModel):
    ram: str
    bull: str
    twinned: str
    crab: str
    lion: str
    maiden: str
    scales: str
    scorpion: str
    archer: str
    goat_horned: str
    water_carrier: str
    fishes: str