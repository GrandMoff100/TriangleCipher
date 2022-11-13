# TriangleCipher
Uses a triangle to encrypt text.


## Description

The triangle refered to is constructed with the following rules:

1. The first row contains all the bytes (integers) of the message.
2. The second row is the differences between each number in the first row.
3. The third row is the differences between each number in the second row, and so on.

The last row contains only one element. Fead the first element of each row, from bottom to top, to get the encrypted message.
