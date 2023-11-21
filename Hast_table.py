class HastTable():
    def __init__(self) -> None:
        self.size = 10
        self.table = [None] * self.size
    def _hast_function(self,key):
        return hash(key)%self.size
    def insert(self,key,value):
        index = self._hast_function(key)
        self.table[index] = value
    def get(self,key):
        index = self._hast_function(key)
        return self.table[index]
    def remove(self,key):
        index = self._hast_function(key)
        self.table[index] = None
