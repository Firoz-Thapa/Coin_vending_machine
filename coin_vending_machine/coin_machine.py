import simpleaudio as sa
from config import Config


class CoinMachine:
    config = Config()

    def __init__(self) -> None:
        self.coins = self.config.read('Coins', 'inserted_coins')
        return None

    def minus_coin(self, value) -> None:
        self.coins -= value
        self.config.write('Coins', 'inserted_coins', self.coins)
        self.playSound('coin_land.wav')
        return None

    def plus_coin(self, value) -> None:
        self.coins += value
        self.config.write('Coins', 'inserted_coins', self.coins)
        self.playSound('insert_coin.wav')
        return None

    def view_coins(self) -> None:
        print(
            f"{self.config.read('Coins','inserted_coins')} coin(s) in vending machine.\n")
        return None

    def get_coins(self) -> int:
        return self.config.read('Coins', 'inserted_coins')

    def playSound(self, fileName):
        s_obj = sa.WaveObject.from_wave_file(fileName)
        p_obj = s_obj.play()
        p_obj.wait_done()
