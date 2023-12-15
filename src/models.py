from pydantic import BaseModel


class SettingsModel(BaseModel):
    PATH_iconAspects: str = "icons"
    PATH_config:str = "config.json"
