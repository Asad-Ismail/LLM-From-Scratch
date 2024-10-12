

def get_stats(ids,counts=None):
    counts = counts if count else {} 
    for pair in zip(ids,ids[1:]):
        counts=counts.get(pair,0)+1
    return counts


class BaseTokenizer:

    def __init__(self):
        ## vocab dict to go from index to pairs
        self.vocab={}

    def train(self, text, vocab_size, verbose=False):
        ## UTF 8 encoding encodes a text to sequence of bytes. And each byte has max range of 255. or 256 numbers but this is the 
        # maximum limit of single byte after that multiple bytes represnetation we should merge with each other
        encoded=text.encode("UTF-8")
        vocab = {idx:bytes([idx]) for idx in range(256)} 
        merges= vocab_size-256
        assert merges>=0 ,"Vocab size should be larger than 256"
        for _ in range(merges):
            counts=get_stats(encoded)



        pass

    def encode(self, text):
        pass
    
    def decode(self, ids):
        pass


bt=BaseTokenizer()

test_string ='asad ismail 123'

bt.train(test_string,500)


