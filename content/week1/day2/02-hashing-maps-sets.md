# algo academy - week 1 - day 2

## hashing, maps, and sets

### hash sets / maps

- hash sets and maps are probably the most common data structures you're ever going to use, whether we're talking about interviews or practical use
- set: a set of _unique_ values

  - methods
    - new_set = set()
    - len(new_set)
    - new_set.add()
    - new_set.remove(), new_set.discard()
      - .remove() will throw error if thing to remove doesnt exist, .discard will not
      - in js, .remove() will not throw the error
  - unlike an array, does not have indices
  - useful when we need to keep track of unique pieces of data that should only appear once
    - eg, coordinates on a matrix
  - example: {5,7,9,3,30}

- maps and objects
  - store data in key-value pairs
    - python dictionary methods
      - dictionary["key"], dictionary.get("key", default_value)
      - dictionary.keys()
      - dictionary.values()
      - dictionary.items()
      - del dictionary["key"]
    - python default dictionary
      - from collections import defaultdict
      - defaultdict_demo = defaultdict(int)
      - other values for parameter
        - set
        - list

### runtime complexities

- maps, objects, and sets
- operation || bigO time
  - insert value || O(1)
  - remove value || O(1)
  - search value || O(1)
- as we can see, hash data structures are extremely efficient, which why it's so commonly used

### hash map implementation

- use a hashing function to convert key into an integer, then use that integer as the index
- minimize collisions
  - we cannot actually completely get rid of collisions! however, we can make it extremely unlikely using different strategies:
  - rehashing: resize an array when half full (similar to dynamic arrays)
    - recompute the hash
    - may need to move elements to new indices
  - chaining: store linked lists of pairs instead of just key-value pairs
  - open addressing
    - try the next open position
- demo:
  - hashmap["Alice"] = "NYC";
  - hashmap["Brad"] = "Chicago";
  - hashmap["Collin"] = "Seattle";

### demos

- two sum
- matrix set zeros
- group anagrams
