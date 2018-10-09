import hashlib
import time
import random
import string

class Block:
    prevhash = ""
    def __init__(self, prevhash1 = None):
        if(prevhash1 == None):
            self.prevhash = 0
        else:
            self.prevhash = prevhash1
    data = ""
    currhash = ""
    def compute_block(self,block_data):
        self.data = block_data;
        self.currhash = hashlib.sha256(block_data.encode()).hexdigest()
i=0
while(i<10):
    if(i==0):
        x = Block()
    else:
        x = Block(prev)
    x.compute_block(random.choice(string.letters))
    prev = x.currhash
    print(x.prevhash)
    print(x.data)
    print(x.currhash)
    print("------------------------------------------------------------------")
    time.sleep(1)
    i = i+1
