# Reverse the order of the bits in a given integer.

# Example

# For a = 97, the output should be
# mirrorBits(a) = 67.

# 97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.

# For a = 8, the output should be
# mirrorBits(a) = 1.

def mirrorBits(a):
    # Convert to binary
    binary = bin(a)[2:]
    # Reverse the order of the bits
    binary = binary[::-1]
    # Convert back to integer
    return int(binary, 2)
