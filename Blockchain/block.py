import hashlib
from datetime import datetime
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        print(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Usage example
my_blockchain = Blockchain()
my_blockchain.add_block(Block(time.time(), {"amount": 5}, my_blockchain.get_latest_block().hash))
my_blockchain.add_block(Block(time.time(), {"amount": 10}, my_blockchain.get_latest_block().hash))

# After adding a new block
latest_block = my_blockchain.get_latest_block()
print("Timestamp:", latest_block.timestamp)
print("Data:", latest_block.data)
print("Previous Hash:", latest_block.previous_hash)
print("Hash:", latest_block.hash)


print("Blockchain is valid:", my_blockchain.is_chain_valid())

# Manipulate the blockchain to test validity
# my_blockchain.chain[1].data = {"amount": 100}

# print("Blockchain is valid:", my_blockchain.is_chain_valid())
