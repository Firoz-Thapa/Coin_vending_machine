from pathlib import Path
import simpleaudio as sa
FILE_PATH_INSERT_COIN= Path("insert_coin.wav")

class VendingMachine:
    coins:int
    def __init__(self) -> None:
        self.coins = 0
        return None

    def insert_coin(self) -> None:
        self.coins += 1
        s_obj = sa.WaveObject.from_wave_file(FILE_PATH_INSERT_COIN.__str__())
        p_obj = s_obj.play()
        p_obj.wait_done()
        return None

    def return_coins(self) -> None:
        self.coins = 0
        
        s_obj = sa.WaveObject.from_wave_file(FILE_PATH_INSERT_COIN.__str__())
        p_obj = s_obj.play()
        p_obj.wait_done()
    
        return None
    
    def getMachineCoins(self) -> int:
        return self.coins