# import struct

x = 523 ** 23
print(x)
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))
