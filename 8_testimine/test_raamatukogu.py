import pytest
from raamatukogu import Raamatukogu
@pytest.fixture
def lib(): return Raamatukogu({"Python": 3, "Java": 2, "Linux": 1})
def test_lubatud_laenutus(lib): assert lib.laenuta("Python")
def test_vigane_pealkiri(lib): assert not lib.laenuta("Unknown")
def test_laenutus_vahendab(lib): lib.laenuta("Python"); assert lib.saadavus("Python") == 2
def test_laenutus_nullini(lib):
    assert lib.laenuta("Linux"); assert not lib.laenuta("Linux"); assert lib.saadavus("Linux") == 0
def test_tagasta_laenutatu(lib): lib.laenuta("Java"); assert lib.tagasta("Java")
def test_tagastamine_ilma_laenutuseta(lib): assert not lib.tagasta("Java")
def test_tagastamine_taastab_saadavuse(lib): lib.laenuta("Java"); lib.tagasta("Java"); assert lib.saadavus("Java") == 2
def test_koguarv_pusib(lib):
    algne = lib.koguarv(); lib.laenuta("Python"); lib.tagasta("Python"); assert lib.koguarv() == algne
def test_tundmatu_saadavus(lib): assert lib.saadavus("X") == 0
def test_negatiivne_algkogus():
    with pytest.raises(ValueError): Raamatukogu({"Bad": -1})
def test_saadavus_erineb_pealkirjati(lib): assert lib.saadavus("Python") == 3 and lib.saadavus("Java") == 2
def test_laenuta_ja_tagasta_kaks(lib):
    lib.laenuta("Python"); lib.laenuta("Python"); assert lib.tagasta("Python"); assert lib.saadavus("Python") == 2
def test_tagasta_kaks_korda(lib):
    lib.laenuta("Java"); assert lib.tagasta("Java"); assert not lib.tagasta("Java")
def test_mitme_raamatu_koguarv(lib): assert lib.koguarv() == 6
def test_laenutatud_koguarv_pusib(lib):
    enne = lib.koguarv(); lib.laenuta("Python"); assert lib.koguarv() == enne
