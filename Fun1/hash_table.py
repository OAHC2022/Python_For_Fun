"""
python assign int dynamically: from -5 to 2^8 it has fixed memory location
outside this range, oython will treat it as string which the memory location will be allocated dynamically
string/float is allocated dynamically
hash() function gives the hashed value of a hashable object
__hash__ redefine hash function for an object
id gives the memory location
ord gives the ascii translation of a string

Hashtable:
basically it is realized through an array by searching the index
Use the hash function to convert an immutable type object to an integer and then mod by the size of the array(prime number)
Then always use this hash function to translate the key and find the value using index
time complexity O(1)
However, the array could have collisions when hashing, two ways to solve:
1. linked list in the same index
2. probing/open addressing: linear, quadratic, rehashing
there could be more but that's all I know so far
"""


class Hash:
    def __init__(self):
        self.size = 3
        self.key = [None] * self.size
        self.value = [None] * self.size

    def hash_function(self, key):
        val = id(key)
        print(val%self.size)
        return val % self.size

    def push(self, key, val):
        # linear probing
        index = self.hash_function(key)
        origin = index
        while self.key[index] is not None:
            if self.key[index] == key:
                return
            index = (index + 1) % self.size
            if index == origin:
                return
        self.key[index] = key
        self.value[index] = val

    def get(self, key):
        index = self.hash_function(key)
        origin = index
        while self.key[index] is not None:
            if self.key[index] == key:
                return self.value[index]
            index = (index + 1) % self.size
            if index == origin:
                return
        return None
if __name__ == "__main__":
    hash = Hash()
    hash.push("a",1)
    hash.push("b",4)
    hash.push("c",6)
    hash.push("d",2)
    print(hash.get("d"))
    print(hash.key)