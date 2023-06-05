# Here, I prototyped the logic needed to implement
# the Fx33 (LD B, Vx) instruction

N = 0x1b
d2 = 0

# Lookup table for starting values
lut = [
    0x000, 0x016, 0x032, 0x048,
    0x064, 0x080, 0x096, 0x112,
    0x128, 0x144, 0x160, 0x176,
    0x192, 0x208, 0x224, 0x240]

# Starting value from lookup table
S = lut[N >> 4]

# Add low nibble of N and if carry, add 6
X1 = S + (0x0F & N)
if (0xF0 & S) != (0xF0 & X1):
    X1 += 6

# If addition results in invalid BCD, correct d0
X2 = X1
if X1 & 0xF > 0x9:
    X2 += 0x6
    
# If addition results in invalid BCD, correct d1
X3 = X2
if X2 & 0xF0 > 0x90:
    X3 += 0x60

print('Value (HEX)  : 0x%03X' % N)
print('Value (DEC)  :', N)
print('Starting     : 0x%03X' % S)
print('Plus nibble  : 0x%03X' % X1)
print('Corrected d0 : 0x%03X' % X2)
print('Corrected d1 : 0x%03X' % X3)