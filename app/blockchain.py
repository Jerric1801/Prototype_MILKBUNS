import sys
import ast
import hashlib
import json
import pandas as pd


def getBlockchain():
    chain = pd.read_json("./static/get_chain.json")
    



class Blockchain:

    def __init__(self):
        self.chain = pd.read_json("./app/static/get_chain.json", orient='records')
        self.dict = self.chain.to_dict()
        self.items = self.dict["chain"]

    def create_blockchain(self, supplier, cargo, amount, destination, proof, previous_hash):
        block = {
            'index':len(self.dict["chain"]),
            'shipment': [supplier, cargo, amount, destination],
            'proof': self.proof_of_work( self.chain.iloc[-1]["chain"]["proof"]),
            'previous_hash': self.chain.iloc[-1]["chain"]["current_hash"],
            'current_hash': self.hash(self.chain.iloc[-1]["chain"])
        }

        return block

        # return new_chain
    
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


if __name__ == "__main__":
    getBlockchain()