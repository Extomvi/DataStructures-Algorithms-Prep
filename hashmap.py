"""
Implementing an hash map/ hash table
"""

from multiprocessing.pool import RUN


class HashMap:

    def __init__(self,size):
        self.size = size
        self.hash_map = self.create_bucket()

    def create_bucket(self):
        return [[] for i in range(self.size)]

    def set_val(self, key, val):
        hash_key = hash(key) % self.size

        bucket = self.hash_map[hash_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key,val))

    def get_val(self, key):
        hash_key = hash(key) % self.size

        bucket = self.hash_map[hash_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_val
        else:
            return "No record found"


    def delete_val(self, key):
        hash_key = hash(key) % self.size

        bucket = self.hash_map[hash_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket.pop(index)
        return

    def __str__(self):
        return "".join(str(item) for item in self.hash_map)

hash_map = HashMap(5)

hash_map.set_val('run@gmail.com', 'RUN')
print(hash_map)
hash_map.set_val('wing@gmail.com', 'WING')
print(hash_map)
print(hash_map.get_val('wing@gmail.com'))
hash_map.delete_val('run@gmail.com')
print(hash_map)

