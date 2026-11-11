"""Ülesanne 9. Palindroomi kontrollimine"""


from testitavad_funktsioonid import palindroom
assert palindroom("Kass") is False
assert palindroom("Radar") is True
assert palindroom("A man, a plan, a canal: Panama") is True
