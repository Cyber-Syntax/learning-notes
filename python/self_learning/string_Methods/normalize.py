# normalize example
# NFC (Canonical Decomposition, followed by Canonical Composition)
# NFD (Canonical Decomposition)
# NFKC (Compatibility Decomposition, followed by Canonical Composition)
# NFKD (Compatibility Decomposition)

from unicodedata import normalize

# NFC
s1 = '\u1E9B\u0323'
print(normalize('NFC', s1))  # Output: 'ẛ̣'

# NFD
s2 = '\u1E9B\u0323'
print(normalize('NFD', s2))  # Output: 'ẛ̣'

# NFKC
s3 = '\u00C5'
print(normalize('NFKC', s3))  # Output: 'Å'

# NFKD
s4 = '\u00C5'
print(normalize('NFKD', s4))  # Output: 'A\u030A'






import unicodedata

def normalize(s, form):
  return unicodedata.normalize(form, s)

# Example input string
s = "İstanbul"

# Apply NFKC normalization
nfkc = normalize(s, 'NFKC')
print(f'NFKC Normalized: {nfkc}')

# Apply NFKD normalization
nfkd = normalize(s, 'NFKD')
print(f'NFKD Normalized: {nfkd}')

# Apply NFC normalization
nfc = normalize(s, 'NFC')
print(f'NFC Normalized: {nfc}')

# Apply NFD normalization
nfd = normalize(s, 'NFD')
print(f'NFD Normalized: {nfd}')


# Outputs:
# NFKC Normalized: Istanbul
# NFKD Normalized: Istanb\u0307ul
# NFC Normalized: İstanbul
# NFD Normalized: Istanb\u0307ul