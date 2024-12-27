class HashMap:
    def __init__(self, max_length = 100):
        self.max = max_length
        self.map = [None for i in range(self.max)]

    def hash(self, key):
        value = 0
        for c in key:
            value += ord(c)
        return value % self.max
    
    def __getitem__(self, key): # Operator Overloading
        h = self.hash(key)
        return self.map[h]

    def __setitem__(self, key, val):
        h = self.hash(key)
        self.map[h] = val
        return h
    
    def __delitem__(self, key):
        h = self.hash(key)
        self.map[h] = None
        return h

    def print(self):
        print(self.map)

if __name__ =='__main__':
    hp = HashMap()
    hp['Name'] = 'Ravi'
    hp.print()
    del(hp['Name'])
    hp.print()
