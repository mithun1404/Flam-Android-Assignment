class MyHashMap:
    def __init__(self):
        # Use a large prime number for bucket size to reduce collisions
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        
        for i in range(len(bucket)):
            k, v = bucket[i]
            if k == key:
                bucket[i] = (key, value)
                return
        
        
        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        
        return -1 

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return
