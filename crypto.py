# following https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
#uses python2

import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index=index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash=previous_hash
        self.hash=self.hash_block()

    def hash_block(self):
        sha=hasher.sha256()
        sha.update(str(self.index)+
                    str(self.timestamp)+
                    str(self.data)+
                    str(self.previous_hash))
        return sha.hexdigest()

# a genesis block is the first block
import datetime as date
def create_genesis_block():
    #constructing the first block of a blockchain

    #arbitrary previous hash, has an index of zero
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index=last_block.index+1
    this_timestamp = date.datetime.now()
    this_data = "Hey I'm a block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

#create the blockchain and add the first block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

#number of blocks to add after the genesis blocks
num_of_blocks_to_add=20

#function to add blocks to the blockchain
for i in range (0, num_of_blocks_to_add):
    block_to_add=next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block=block_to_add
    #print the block!)
    print "Block #{} has been added to the blockchain!".format(block_to_add.index)
    print "Hash: {}/n".format(block_to_add.hash)




#creating a new block will require a miner to use a number, if divisible by 9 and the proof number
# of the last block

"""


miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"

def proof_of_work(last_proof):
    #creating a proof of work variable
    incrementor = last_proof+1
    #keep incrementing the incrementor until it's divisible by 9 and previous
    # POW is in the blockchain
    while not (incrementor % 9 == 0 and incrementor % last_proof==0):
        incrementor += 1

@node.route('/mine', method = ['GET'])
def mine():
    # get previous POW
    last_block = blockchain[len(blockchain)-1]
    last_proof = last_block.data['proof-of-work']
    #finding POW for coin being mined
    proof = proof_of_work(last_proof)

    #adding a transaction
    this_nodes_transactions.append({
    "from": "network", "to": miner_address, "amount:" "1"
    })


    #getting data for making a new block
"""
