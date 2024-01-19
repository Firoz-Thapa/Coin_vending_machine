from pathlib import Path
import configparser

FILEPATH_CONFIG = Path("config.ini")


class Config:


    def __init__(self) -> None:
        self.config = configparser()

        self.save()
        self.config.read()
    def get_value(self, section, key):
        return self.config[section][key]
    
    def set_value(self, section, key, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config[section][key] = value

    def save(self):
        with open[FILEPATH_CONFIG, "w"] as configfile:
            self.config.write(configfile)


