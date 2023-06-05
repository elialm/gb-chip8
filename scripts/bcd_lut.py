# This script is for generating the LUT for
# the calculated BCD values.

# Lookup table for starting values
BCD_START_LUT = [
    0x000, 0x016, 0x032, 0x048,
    0x064, 0x080, 0x096, 0x112,
    0x128, 0x144, 0x160, 0x176,
    0x192, 0x208, 0x224, 0x240]

def to_bcd(val: int):
    # Starting value from lookup table
    s = BCD_START_LUT[val >> 4]

    # Add low nibble of N and if carry, add 6
    x = s + (0x0F & val)
    if (0xF0 & s) != (0xF0 & x):
        x += 6

    # If addition results in invalid BCD, correct d0
    if x & 0xF > 0x9:
        x += 0x6
        
    # If addition results in invalid BCD, correct d1
    if x & 0xF0 > 0x90:
        x += 0x60

    return x

for n in range(256):
    print('db $%02X' % (to_bcd(n) & 0xFF))