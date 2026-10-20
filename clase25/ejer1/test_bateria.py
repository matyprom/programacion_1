from bateria import clasificar_nivel_bateria
def caso_normal():

    assert clasificar_nivel_bateria(25)
def caso_limite():
    assert clasificar_nivel_bateria(101)
def inalido():
    assert clasificar_nivel_bateria(-5)