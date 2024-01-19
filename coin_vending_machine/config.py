import configparser


class Config:
    config = configparser.ConfigParser()

    def read(self, section, key) -> int:
        self.config.read('config.ini')
        return self.config.getint(section, key)

    def write(self, section, key, value) -> None:
        self.config.read('config.ini')
        self.config.set(section, key, str(value))
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
