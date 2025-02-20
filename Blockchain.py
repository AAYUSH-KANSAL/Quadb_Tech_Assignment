import hashlib                                                                              # Used for hashing
import datetime                                                                             # Used for timestamps

class Block:                                                                                # Define a block class
    def __init__(self, previous_hash, data):                                                # Initialize a block
        self.previous_hash=previous_hash                                                  # Store the previous hash
        self.data=data                                                                    # Store the data
        self.timestamp=datetime.datetime.now()                                            # Store the timestamp
        self.hash=self.calculate_hash()                                                   # Calculate the hash

    
    def create_genesis_block():                                                             # Create the genesis block
        return Block("0", "Genesis Block")                                                  # Return the genesis block

    def calculate_hash(self):                                                               # Calculate the hash of the block
        content=f"{self.previous_hash}{self.data}{self.timestamp}".encode()               # Create the content
        return hashlib.sha256(hashlib.sha256(content).digest()).hexdigest()                 # Calculate the hash

# Initialize blockchain with the genesis block
blockchain=[Block.create_genesis_block()]                                                 # Initialize the blockchain
print("Genesis block created!")                                                             # Print the genesis block
print(f"Hash: {blockchain[0].hash}\n")                                                      # Print the hash of the genesis block

# Number of blocks to add
num_blocks=10

# Add new blocks to the blockchain
for i in range(1, num_blocks + 1):                                                          # Iterate from 1 to 10
    new_block=Block(blockchain[-1].hash, f"Block {i} Data")                               # Create a new block
    blockchain.append(new_block)                                                            # Add the new block to the blockchain

    print(f"Block #{i} created!")                                                           # Print the block
    print(f"Hash: {new_block.hash}\n")                                                      # Print the hash of the block
