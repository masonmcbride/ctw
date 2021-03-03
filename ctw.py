# Trying to compress 
from collections import defaultdict
import math
import numpy as np

def bitgen():
    with open('enwik4', 'rb') as f:
        while (byte := f.read(1)):
            for i in range(8):
                yield (ord(byte) >> i) & 1

def test(num_of_bits):
    bg = bitgen()
    frames = defaultdict(lambda: [1, 2])

    try:
        frame = [-1]*num_of_bits
        HH = 0
        for bit in bg:
            f = tuple(frame)

            p = frames[f][0] / frames[f][1]
            p = p if bit == 1 else 1 - p

            H = -math.log2(p)
            HH += H

            frames[f][0] += bit == 1
            frames[f][1] += 1
            frame.append(bit)
            frame = frame[-num_of_bits:]

    except StopIteration:
        pass

    print(len(frames.items()))

    return HH/8.0

HH = test(16)

print(HH)

"""
HH, ws = min([(test(ws), ws) for ws in range(1,33)])
print(f"HH {HH} for window size {ws}")
"""
