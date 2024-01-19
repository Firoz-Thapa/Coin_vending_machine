from menu import Menu
import simpleaudio
from pathlib import Path
import pathlib
from coin_pouch import CoinPouch
from vending_machine import VendingMachine
FILEPATH_INSERT_COIN = Path("insert_coin.wav")

class vMachine(Menu): # MenuMain inheriting Menu
    INSERT_COIN = simpleaudio.WaveObject.from_wave_file(pathlib.Path("./insert_coin.wav").__str__())
    putcoins = CoinPouch()
    machinecoin = VendingMachine()
    def __init__(self) -> None:
        super().__init__(options=[
            { "description": "Insert coins", "action": self.insertCoins },
            { "description": "View inserted coins", "action": self.viewCoins },
            { "description": "Return coin", "action": self.returnCoin },
        ])
        return None
    
    def insertCoins(self) -> None:
        self.putcoins.remove_coin()
        self.machinecoin.insert_coin()
        return None
    
    def viewCoins(self) -> None:
        print(f"{self.machinecoin.getMachineCoins()} coin(s) in vending machine.")
        return None
    
    def returnCoin(self) -> None:
        
        return None