#  Data Structures Fundamentals

### Memory
- 1 byte = 8 bits, single byte can represent up to 256 (2^8)
- fixed width integer
    - integer represented by a fixed amount of bits
        - 32-bit integer (int type) or 64-bit integer (long type) represented by 4bytes or 8bytes respectively
        - regardless of how large an integer is, an operation performed on its fixed-width-integer representation consists of constant number of bit manipulations, since the integer is made up of a fixed number of bits
- memory
    - data stored in memory is stored in bytes
    - bytes in memory can point to other bytes in memory; concept of storing references
    - amount of memory a machine has is limited
    - accessing a byte or a fixed number of bytes is an elementary operation; can be loosely treated as a single unit of operation work

---
### Hash Tables
- under the hood, hash tables uses a dynamic array of linked lists to efficiently store key-value pairs
    - when inserting a key-value pair, hash function first maps the key to an integer value and by extension, to an index in the underlying dynamic array
        - dynamic array means it can be resized to fit different sizes
    - then, the value of the associated key is added to the linked list stored at that index in the dynamic array, and a reference to the key is also stored with the value of the associated
- hash tables relies heavily on optimized hash functions to minimize the number of collisions that occur when storing values; cases where 2 key maps to the same index
- complexities
    - inserting: O(1) on average, O(n) in worse case
    - removing: O(1) on average, O(n) in worse case
    - looking up a key: O(1) on average, O(n) in worse case
    - worst-case linear time operations occur when a hash table experiences a lot of collisions, leading to long linked lists internally which takes O(n) time to traverse
- in context of interviews can typically assume hash functions employed by hash tables are so optimized that colisions are extremely rare and constant-time operations are guaranteed

---
### Stacks and Queues
- stack is a array-like data structure that follows LIFO
- typically implemented with a dynamic array
- complexities
    - pushing an element onto the stack: O(1)
    - popping an element off the stack: O(1)
    - peeking at the element on the top of the stack: O(1)
    - searching for an element on the stack: O(n)
- queue is an array-like data structure that follows FIFO
- typically implemented with a doubly linked list
- complexities
    - enqueuing an element into the queue: O(1)
    - dequeuing an element out the queue: O(1)
    - peeking at the element at the front of the queue: O(1)
    - searching for an element in the queue: O(n)

---
### Graphs
- collection of nodes or values called vertices that might be related; relation between vertices are called edges
- cycle
    - a cycle occurs in a graph when three or more vertices in the graph are connected so as to form a closed loop
    - sometimes include cycles of length of two or one
- acyclic graph vs cyclic graph
    acyclic: graph with no cycles
    cyclic graph: graph with at least one cycle
- directed graph vs undirected graph
    - directed: edges are directed
    - undirected: edges are undirected - can be traversed in both directions
- connected graph
    - graph is connected if for every pair of vertices in the graph theres a path of one or more edges connecting the given vertices
    - in case of directed graph
        - strongly connected if there are bidirectional connections between the vertices of every pair of vertices
        - weakly connected if there are connections (but not necessarily bidirectional ones) between the vertices of every pair of vertices
    - graph that isnt connected is said to be disconnected
- space complexity: O(v+e), can be stored in hashmaps