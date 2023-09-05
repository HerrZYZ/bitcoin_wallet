## database.py
import sqlite3
from typing import List, Dict, Union

class Database:
    def __init__(self, db_name: str = 'wallet.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Wallets (
                address TEXT PRIMARY KEY,
                balance REAL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Transactions (
                sender TEXT,
                receiver TEXT,
                amount REAL,
                FOREIGN KEY(sender) REFERENCES Wallets(address),
                FOREIGN KEY(receiver) REFERENCES Wallets(address)
            )
        """)
        self.conn.commit()

    def insert_wallet(self, address: str, balance: float):
        self.cursor.execute("""
            INSERT INTO Wallets (address, balance)
            VALUES (?, ?)
        """, (address, balance))
        self.conn.commit()

    def update_wallet(self, address: str, balance: float):
        self.cursor.execute("""
            UPDATE Wallets
            SET balance = ?
            WHERE address = ?
        """, (balance, address))
        self.conn.commit()

    def get_wallet(self, address: str) -> Dict[str, Union[str, float]]:
        self.cursor.execute("""
            SELECT * FROM Wallets
            WHERE address = ?
        """, (address,))
        wallet = self.cursor.fetchone()
        return {'address': wallet[0], 'balance': wallet[1]} if wallet else None

    def insert_transaction(self, sender: str, receiver: str, amount: float):
        self.cursor.execute("""
            INSERT INTO Transactions (sender, receiver, amount)
            VALUES (?, ?, ?)
        """, (sender, receiver, amount))
        self.conn.commit()

    def get_transactions(self, address: str) -> List[Dict[str, Union[str, float]]]:
        self.cursor.execute("""
            SELECT * FROM Transactions
            WHERE sender = ? OR receiver = ?
        """, (address, address))
        transactions = self.cursor.fetchall()
        return [{'sender': t[0], 'receiver': t[1], 'amount': t[2]} for t in transactions]

    def close(self):
        self.conn.close()
