class Raamatukogu:
    """Raamatukogu saadaval olevate eksemplaride haldamiseks."""
    def __init__(self, kogused):
        if any(not isinstance(v, int) or v < 0 for v in kogused.values()):
            raise ValueError("Kogused peavad olema mittenegatiivsed täisarvud.")
        self._algkogus = dict(kogused)
        self._saadaval = dict(kogused)
        self._laenutatud = {nimi: 0 for nimi in kogused}
    def laenuta(self, pealkiri):
        if pealkiri not in self._saadaval or self._saadaval[pealkiri] <= 0: return False
        self._saadaval[pealkiri] -= 1
        self._laenutatud[pealkiri] += 1
        return True
    def tagasta(self, pealkiri):
        if pealkiri not in self._laenutatud or self._laenutatud[pealkiri] <= 0: return False
        self._laenutatud[pealkiri] -= 1
        self._saadaval[pealkiri] += 1
        return True
    def saadavus(self, pealkiri): return self._saadaval.get(pealkiri, 0)
    def koguarv(self, pealkiri=None):
        if pealkiri is not None: return self._saadaval.get(pealkiri, 0) + self._laenutatud.get(pealkiri, 0)
        return sum(self._saadaval.values()) + sum(self._laenutatud.values())
