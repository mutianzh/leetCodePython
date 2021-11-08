"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


class LRUCache:

    #     # Approach 1: orderd dict in python3
    #     def __init__(self, capacity: int):
    #         self.cap = capacity
    #         self.cache = collections.OrderedDict()

    #     def get(self, key: int) -> int:

    #         if key not in self.cache:
    #             return -1

    #         val = self.cache[key]
    #         self.cache.move_to_end(key)
    #         return val

    #     def put(self, key: int, value: int) -> None:
    #         if key in self.cache:
    #             self.cache.move_to_end(key)
    #         self.cache[key] = value

    #         if len(self.cache) > self.cap:
    #             self.cache.popitem(last = False)

    # Appraoch 2: dict + doubled linked list

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.next = {}
        self.prev = {}
        self.head = 'head'
        self.tail = 'tail'

        self.next[self.head] = self.tail
        self.prev[self.tail] = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # delete key from current list
        prev_key = self.prev[key]
        next_key = self.next[key]
        self.next[prev_key] = next_key
        self.prev[next_key] = prev_key

        del self.next[key]
        del self.prev[key]

        # append key after the last key
        val = self.cache[key]
        last_key = self.prev[self.tail]
        self.next[last_key] = key
        self.prev[key] = last_key
        self.next[key] = self.tail
        self.prev[self.tail] = key

        return val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            # delete key from list
            prev_key = self.prev[key]
            next_key = self.next[key]
            self.next[prev_key] = next_key
            self.prev[next_key] = prev_key

            del self.next[key]
            del self.prev[key]

        self.cache[key] = value
        # Append key
        val = self.cache[key]
        last_key = self.prev[self.tail]
        self.next[last_key] = key
        self.prev[key] = last_key
        self.next[key] = self.tail
        self.prev[self.tail] = key

        if len(self.cache) > self.size:
            # Delete the first key
            first_key = self.next[self.head]
            second_key = self.next[first_key]

            self.next[self.head] = second_key
            self.prev[second_key] = self.head

            del self.cache[first_key], self.next[first_key], self.prev[first_key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)