"""
Implementing an hash map/ hash table
"""

class HashMap:

    def __init__(self,size):
        self.size = size
        self.hash_map = self.create_bucket()

    def create_bucket(self):
        return [[] for i in range(self.size)]

    def set_val(self, key, val):
        