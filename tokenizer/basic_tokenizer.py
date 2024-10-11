class BaseTokenizer:

    def __init__(self):
        pass

    def train(self, text, vocab_size, verbose=False):
        pass

    def encode(self, text):
        pass
    
    def decode(self, ids):
        pass


bt=BaseTokenizer()


