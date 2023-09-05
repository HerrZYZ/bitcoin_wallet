from flask import Flask, request, jsonify
from wallet import Wallet
from transaction import Transaction
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/wallet', methods=['POST'])
def create_wallet():
    wallet = Wallet(db)
    address = wallet.create_wallet()
    return jsonify({'address': address}), 200

@app.route('/balance', methods=['GET'])
def get_balance():
    address = request.args.get('address')
    wallet = Wallet(db, address)
    balance = wallet.get_balance()
    return jsonify({'balance': balance}), 200

@app.route('/transaction', methods=['POST'])
def send_bitcoin():
    sender = request.json.get('sender')
    receiver = request.json.get('receiver')
    amount = request.json.get('amount')
    transaction = Transaction(db, sender, receiver, amount)
    if transaction.send_bitcoin():
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'failure', 'message': 'Insufficient balance'}), 400

@app.route('/history', methods=['GET'])
def get_transaction_history():
    address = request.args.get('address')
    transaction = Transaction(db, address, '', 0)
    history = transaction.get_transaction_history()
    return jsonify({'history': history}), 200

if __name__ == '__main__':
    app.run(debug=True)
