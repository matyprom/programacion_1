import pytest
from operaciones import sumar

def test_sumar_dos_positivos():
    assert sumar(2,3) == 5

def test_sumar_invalidos():
    with pytest.raises(ValueError):
        sumar(1,1)
