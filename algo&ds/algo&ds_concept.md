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