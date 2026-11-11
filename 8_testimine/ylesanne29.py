"""Ülesanne 29. Hulgatehete kontrollimine"""


a = {1,2,3}; b = {3,4}
assert a | b == {1,2,3,4}
assert a & b == {3}
assert a - b == {1,2}
