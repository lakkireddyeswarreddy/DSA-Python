"""

Huffman coding is an aglorithm used for data compression by assigning shorter binary codes to more frequent characters and longer binary codes to less frequent characters.

It ensures no code is a prefix of another code.

It compresses the size of data for storing or transmission.
It is used in ZIP, MP3 etc.

How It Works (Step-by-Step)

Count Frequencies of each character in the input.
Build a Min-Heap (priority queue) of nodes based on frequency.
Combine Two Lowest Frequency Nodes into a new node.
Repeat until one node remains — this becomes the root of the Huffman Tree.
Assign Binary Codes by traversing the tree:

Left edge → 0
Right edge → 1
"""
