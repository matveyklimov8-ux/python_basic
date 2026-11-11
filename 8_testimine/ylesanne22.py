"""Ülesanne 22. Erindite testimine"""


from testitavad_funktsioonid import kalkulaator, soodushind
try: kalkulaator(5, 0, "/")
except ZeroDivisionError: pass
else: raise AssertionError("Oodati ZeroDivisionError")
try: soodushind(10, 150)
except ValueError: pass
else: raise AssertionError("Oodati ValueError")
