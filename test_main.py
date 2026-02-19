# test_main.py
from main import suma, es_par

def test_suma_enteros():
    assert suma(2, 3) == 5

def test_suma_decimales():
    assert suma(1.5, 2.5) == 4.0

def test_es_par_true():
    assert es_par(10) is True

def test_es_par_false():
    assert es_par(7) is False