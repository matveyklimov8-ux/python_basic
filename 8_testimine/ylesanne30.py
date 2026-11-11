"""Ülesanne 30. Andmestruktuuri muutmise avastamine"""


import copy
algne = [[1,2],[3,4]]
shallow = algne[:]
depth = copy.deepcopy(algne)
shallow[0][0] = 99
assert algne[0][0] == 99
assert depth[0][0] == 1
