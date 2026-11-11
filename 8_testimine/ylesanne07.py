"""Ülesanne 7. Temperatuuri teisendamine"""


from testitavad_funktsioonid import celsius_fahrenheit
assert celsius_fahrenheit(0) == 32
assert celsius_fahrenheit(100) == 212
assert round(celsius_fahrenheit(20), 1) == 68.0
