from pathlib import Path
import simpleaudio as sa
FILE_PATH_INSERT_COIN= Path("insert_coin.wav")


class CoinPouch:
    coins:int
    def __init__(self) -> None:
        self.coins = 10
        return None

    def remove_coin(self)-> None:
        self.coins = self.coins -1
        s_obj = sa.WaveObject.from_wave_file(FILE_PATH_INSERT_COIN.__str__())
        p_obj = s_obj.play()
        p_obj.wait_done()

    def getPouchCoins(self)->int:
        return self.coins

