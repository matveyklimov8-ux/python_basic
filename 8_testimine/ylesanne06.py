"""Ülesanne 6. Testide parandamine"""


from testitavad_funktsioonid import on_paaris
# Testide ootused peaksid kontrollima ka 0 ja negatiivset arvu.
assert on_paaris(0) is True
assert on_paaris(-3) is False
assert on_paaris(-4) is True
