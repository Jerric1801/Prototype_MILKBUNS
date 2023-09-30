import hashlib
import json
from flask import Flask, jsonify, redirect, url_for

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_blockchain(supplier='', cargo='', destination='', proof=1, previous_hash='0')

    def create_blockchain(self, supplier, cargo, destination, proof, previous_hash):
        block = {
            'index': len(self.chain),
            'shipment': [supplier, cargo, destination],
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        last_block = self.chain[-1]
        return last_block
    
    def get_block(self, index):
        return self.chain[index]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    # generate a hash of an entire block
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            current_proof = block['proof']
            hash_operation = hashlib.sha256(str(current_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
app = Flask(__name__)

blockchain = Blockchain()

@app.route('/shipment1', methods=['GET'])
def shipment1():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    supplier = 'Company A'
    cargo = 'Oil'
    destination = 'Singapore Port'

    block = blockchain.create_blockchain(supplier, cargo, destination, proof, previous_hash)

    current_hash = blockchain.hash(block)

    response = {'index': block['index'],
                'shipment': [supplier, cargo, destination],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'hash': current_hash}
    return jsonify(response), 200

@app.route('/shipment2', methods=['GET'])
def shipment2():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    supplier = 'Company B'
    cargo = 'Burgers'
    destination = 'Singapore Port'

    block = blockchain.create_blockchain(supplier, cargo, destination, proof, previous_hash)

    current_hash = blockchain.hash(block)

    response = {'index': block['index'],
                'shipment': [supplier, cargo, destination],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'hash': current_hash}
    return jsonify(response), 200

@app.route('/shipment3', methods=['GET'])
def shipment3():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    supplier = 'Company C'
    cargo = 'Clothes'
    destination = 'Singapore Port'

    block = blockchain.create_blockchain(supplier, cargo, destination, proof, previous_hash)

    current_hash = blockchain.hash(block)

    response = {'index': block['index'],
                'shipment': [supplier, cargo, destination],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'hash': current_hash}
    return jsonify(response), 200

@app.route('/shipment4', methods=['GET'])
def shipment4():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    supplier = 'Company D'
    cargo = 'Chemicals'
    destination = 'Singapore Port'

    block = blockchain.create_blockchain(supplier, cargo, destination, proof, previous_hash)

    current_hash = blockchain.hash(block)

    response = {'index': block['index'],
                'shipment': [supplier, cargo, destination],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'hash': current_hash}
    return jsonify(response), 200

@app.route('/shipment5', methods=['GET'])
def shipment5():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    supplier = 'Company E'
    cargo = 'Beer'
    destination = 'Singapore Port'

    block = blockchain.create_blockchain(supplier, cargo, destination, proof, previous_hash)

    current_hash = blockchain.hash(block)

    response = {'index': block['index'],
                'shipment': [supplier, cargo, destination],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'hash': current_hash}
    return jsonify(response), 200

@app.route('/shipment6', methods=['GET'])
def shipment6():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    supplier = 'Company F'
    cargo = 'Apples'
    destination = 'Singapore Port'

    block = blockchain.create_blockchain(supplier, cargo, destination, proof, previous_hash)

    current_hash = blockchain.hash(block)

    response = {'index': block['index'],
                'shipment': [supplier, cargo, destination],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'hash': current_hash}
    return jsonify(response), 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

@app.route('/get_block', methods=['GET'])
def block():
    num = 1
    return blockchain.get_block(num)

app.run(host='0.0.0.0', port=5000)
