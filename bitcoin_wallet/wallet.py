from bitcoinlib.wallets import HDWallet
from bitcoinlib.keys import Key
from typing import Optional
from database import Database


class Wallet:
    def __init__(self, db: Database, address: Optional[str] = None, balance: Optional[float] = 0.0):
        self.db = db
        self.address = address
        self.balance = balance

    def create_wallet(self) -> str:
        wallet = HDWallet.create('MyWallet')
        self.address = wallet.get_key().address
        self.balance = 0.0
        self.db.insert_wallet(self.address, self.balance)
        return self.address

    def get_balance(self) -> float:
        wallet = self.db.get_wallet(self.address)
        if wallet:
            self.balance = wallet['balance']
        return self.balance

    def update_balance(self, balance: float):
        self.balance = balance
        self.db.update_wallet(self.address, self.balance)
