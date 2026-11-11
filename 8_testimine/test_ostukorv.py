import pytest
from ostukorv import arvuta_summa, leia_kalleim, toodete_arv, rakenda_soodustus, eemalda_toode
@pytest.fixture
def korv():
    return {"Leib": {"hind": 2.50, "kogus": 2}, "Piim": {"hind": 1.80, "kogus": 1}, "Juust": {"hind": 4.20, "kogus": 3}}
def test_summa(korv): assert arvuta_summa(korv) == 19.40
def test_tuhi_summa(): assert arvuta_summa({}) == 0
def test_kalleim(korv): assert leia_kalleim(korv) == "Juust"
def test_tuhi_kalleim(): assert leia_kalleim({}) is None
def test_kalleima_viik(korv):
    korv["Aed"] = {"hind": 4.2, "kogus": 1}
    assert leia_kalleim(korv) == "Aed"
def test_kogus(korv): assert toodete_arv(korv) == 6
def test_tuhi_kogus(): assert toodete_arv({}) == 0
@pytest.mark.parametrize("summa,protsent,ootus", [(100,0,100),(100,10,90),(100,100,0),(15,20,12),(0,50,0)])
def test_soodustus(summa, protsent, ootus): assert rakenda_soodustus(summa, protsent) == ootus
def test_vigane_soodustus_alla():
    with pytest.raises(ValueError): rakenda_soodustus(10, -1)
def test_vigane_soodustus_ule():
    with pytest.raises(ValueError): rakenda_soodustus(10, 101)
def test_negatiivne_hind():
    with pytest.raises(ValueError): arvuta_summa({"Viga": {"hind": -1, "kogus": 1}})
def test_negatiivne_kogus():
    with pytest.raises(ValueError): toodete_arv({"Viga": {"hind": 1, "kogus": -1}})
def test_murdarv_kogus():
    with pytest.raises(ValueError): arvuta_summa({"Viga": {"hind": 1, "kogus": 1.5}})
def test_mittearv_hind():
    with pytest.raises(ValueError): arvuta_summa({"Viga": {"hind": "kaks", "kogus": 1}})
def test_eemaldamine(korv): assert "Piim" not in eemalda_toode(korv, "Piim")
def test_algne_korv_saab_sailida(korv):
    koopia = {k:v.copy() for k,v in korv.items()}; eemalda_toode(korv, "Piim"); assert korv == koopia
def test_puuduv_eemaldamine(korv): assert eemalda_toode(korv, "Puudub") == korv
def test_rahasumma_umardatakse(): assert arvuta_summa({"a": {"hind": 0.1, "kogus": 3}}) == 0.3
def test_hinnaga_null(): assert arvuta_summa({"Tasuta": {"hind": 0, "kogus": 3}}) == 0
def test_kogus_null(): assert arvuta_summa({"Vaba": {"hind": 5, "kogus": 0}}) == 0


def test_negatiivne_summa_soodustuses():
    with pytest.raises(ValueError):
        rakenda_soodustus(-1, 10)


def test_bool_ei_sobi_soodustuse_protsendiks():
    with pytest.raises(ValueError):
        rakenda_soodustus(10, True)


def test_eemaldamine_ei_muuda_toote_andmeid():
    algne = {"Piim": {"hind": 1.8, "kogus": 2}}
    uus = eemalda_toode(algne, "Puudub")
    uus["Piim"]["kogus"] = 5
    assert algne["Piim"]["kogus"] == 2
