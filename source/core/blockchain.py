from enum import Enum

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'votes': []
}

blockchain = [genesis_block]

"""
open_votes[]:

Core feature of blockchain!

All open votes will be taken and added to a new block 
and then added to a blockchain whenever this block is mined

"""
open_votes = [] #outstandinf transactions
owner = 'Luiz'

candidates = set()


class CandidateEnum(Enum):
    none = 0
    Trump = 1
    Hillary = 2
    Darth = 3
    Putin = 4

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_vote_count():
    
    votes = dict()
    
    for block in blockchain:
        for vote in block['votes']:
            key = vote['candidate'] #dictionary key i.e: 1, 2, 3 or 4 (represents the candidate #)
            votes[key] = votes.get(key, 0) + 1 #votes.get check if the key/candidate has value otherwise sets the initial value to 0 (zero)

    votes = { candidate}
    for key, value in votes.items():
        votes[key]

    return votes


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_vote(vote_id, candidate):
    """ add vote
    
    Arguments:
        :vote_id: unique id per voter/student
        :candidate: candidate of a list of choices
     """
    
    vote = { 
        'vote_id': vote_id, 
        'candidate': candidate
    }
    open_votes.append(vote)
    return open_votes

#will append the vote to the blockchain
def mine_block():
    last_block = blockchain[-1] #retrieve the previous block of the blockchain
    hashed_block = hash_block(last_block) #hash the previous block

    print(hashed_block)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'votes': open_votes
    }
    #TODO: validate if the votes are valid to be added
    #TODO: broadcast the event of addind a block
    blockchain.append(block)
    return True


"""
creates a vote data:
Request input ID and candidate from user (Console input)
"""
def get_vote():
    """ Returns the input of the user (transaction amount in float format) """
    vote_id = input("Vote ID: ")
    candidate = int(input("Choose a number: \n [1] Donald \n [2] Hillary \n "))
    return (vote_id, candidate) #is gonna return a tuple


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    #print(blockchain)
    for (index, block) in enumerate(blockchain):
        print(f"output block [{index}]: ")
        print(block)
        print("\n")
    else:
        print("-" * 20)

def print_vote_count():
    votes = get_vote_count()
    for vote in votes:
        print(f"candidate - {vote}: {votes[vote]} votes")

def verify_chain():
    """ Compare the stored hash in a *given block 
        with the *recalculated hash with the *previous block """


    for (index, block) in enumerate(blockchain):
        #skips the genesis block because there's nothing before it.
        #Also not necessary to validate genesis block
        if index == 0:
            continue

        #every block holds the hash of the previous block
        previous_hash = block['previous_hash']
        recalc_previous_hash = hash_block(blockchain[index-1])
        
        if previous_hash != recalc_previous_hash: #compares the current block with the previous block (hash comparison)
            print(f"XXXXX\n prev_hash: {previous_hash} != {recalc_previous_hash} \nXXXXX")
            return False
    
    return True #if all the calculated hashes match then blockchain is valid 

#TODO: implement verify votes
def verify_votes():
    pass


waiting_for_input = True

while waiting_for_input:
    print("\nPlease choose")
    print("1: add a new vote")
    print("2: Mine block")
    print("3: output the blockchain blocks")
    print("4: output vote count")
    print("h: Manipulate blocks!")
    print("q: quit")
    user_choice = get_user_choice()

    if user_choice == "1":
        tx_data = get_vote()
        vote_id, candidate = tx_data #unpack the tuple 1st and 2nd value rescpetively

        #add vote to the blockchain
        add_vote(vote_id=vote_id, candidate=candidate)
        print(open_votes)
    elif user_choice == "2":
        if mine_block():
            open_votes = [] #empty outstanding votes after creating the block
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print_vote_count()
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'votes': [{'vote_id': '00000', 'candidate': '1'}]
            }
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("invalid input")

    if not verify_chain():
        print_blockchain_elements()
        print("Invalid blockchain")
        break

else:
    print("User left!")