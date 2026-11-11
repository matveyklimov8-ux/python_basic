"""Ülesanne 3. Paaris- ja paaritud arvud"""


from testitavad_funktsioonid import on_paaris
assert on_paaris(2) and not on_paaris(3) and on_paaris(0) and on_paaris(-4)
print("Paarisuse testid läbisid.")
