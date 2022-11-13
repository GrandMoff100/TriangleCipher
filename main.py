import numpy as np


def serialize(content: bytes , alphabet: bytes) -> np.ndarray:
    """Return an array of the indices of each byte in :code:`content`."""
    return np.array([alphabet.index(byte) for byte in content])

def deserialize(indices: np.ndarray, alphabet: bytes) -> bytes:
    """Return a bytestring of :code:`alphabet` indexed by each integer in :code:`indicies`"""
    return bytes(list(np.array(list(alphabet))[indices]))


def encrypt(numbers: np.ndarray) -> np.ndarray:
    """Encrypt a message using the Triangle Cipher."""
    converted = []
    for _ in range(numbers.shape[0]):
        print(numbers)
        converted.append(numbers[0])
        numbers = np.diff(numbers)
    return np.flip(np.array(converted))

def decrypt(numbers: np.ndarray) -> np.ndarray:
    """Decrypt a message using the Triangle Cipher."""
    buffer = np.array([])
    for diff in numbers:
        buffer = np.cumsum(np.insert(buffer, 0, diff), dtype=np.int64)
    return buffer

if __name__ == "__main__":
    utf_alphabet = bytes("".join(list(map(chr, range(256)))), "utf-8")
    n = serialize(b"Hello World!", utf_alphabet)
    n = encrypt(n)
    print(deserialize(decrypt(n), utf_alphabet))
