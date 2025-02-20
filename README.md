# Quadb_Tech_Assignment

# Simple Blockchain Implementation in Python

This is a basic blockchain implementation in Python. It creates a simple chain of blocks, each containing a reference to the previous block, some data, a timestamp, and a unique hash.

## Features
- Generates a **genesis block** as the first block in the chain.
- Uses **SHA-256 double hashing** for security.
- Automatically adds new blocks to the chain.
- Each block stores:
  - Previous block's hash
  - Data
  - Timestamp
  - Its own unique hash

## How It Works
1. The first block (**Genesis Block**) is created manually.
2. New blocks are added to the chain with a reference to the previous block’s hash.
3. Each block's hash is calculated based on its data, timestamp, and previous hash.
4. The blockchain structure ensures data integrity since modifying any block would invalidate all subsequent blocks.

## Prerequisites
- Python 3.x installed

## How to Run
1. Clone this repository or copy the script.
2. Run the script using:

   python blockchain.py
The program will generate 10 new blocks and print their details.
 