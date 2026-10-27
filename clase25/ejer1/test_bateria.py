from bateria import clasificar_nivel_bateria
def test_caso_normal():

    assert clasificar_nivel_bateria(25)
def test_caso_limite():
    assert clasificar_nivel_bateria(101)
def test_inalido():
    assert clasificar_nivel_bateria(-5)