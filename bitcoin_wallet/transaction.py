from bitcoinlib.transactions import Transaction as BtcTransaction
from bitcoinlib.wallets import HDWallet
from typing import List, Dict, Union
from database import Database


class Transaction:
    def __init__(self, db: Database, sender: str, receiver: str, amount: float):
        self.db = db
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def send_bitcoin(self) -> bool:
        sender_wallet = HDWallet(self.sender)
        receiver_wallet = HDWallet(self.receiver)
        if sender_wallet.balance() < self.amount:
            return False
        tx = sender_wallet.send_to(receiver_wallet.get_key().address, self.amount)
        if tx:
            self.db.insert_transaction(self.sender, self.receiver, self.amount)
            return True
        return False

    def get_transaction_history(self) -> List[Dict[str, Union[str, float]]]:
        return self.db.get_transactions(self.sender)
