from menu import Menu
from coin_pouch import CoinPouch
from menu_machine import vMachine

class MenuMain(Menu): # MenuMain inheriting Menu
    coin_pouch = CoinPouch()
    def __init__(self) -> None:
        super().__init__(options=[
            { "description": "View coins in pouch", "action": self.viewCoin },
            { "description": "Go to vending machine", "action": self.goMachine },
        ])      
        return None

    def viewCoin(self) -> None:
        print(f"{self.coin_pouch.getPouchCoins()} coin(s) in coin pouchvvvv.")
        return None
    
    def goMachine(self) -> None:
        vending_machine_menu = vMachine()
        vending_machine_menu.start()
        return None


