from asistente.utils import limpiar_texto


def test_colapsa_saltos_y_espacios():
    crudo = "Cláusula 8.2\n\n\nEl   concesionario  debe\tinformar"
    assert limpiar_texto(crudo) == "Cláusula 8.2\nEl concesionario debe informar"


def test_texto_vacio_devuelve_vacio():
    assert limpiar_texto("") == ""


def test_solo_espacios_devuelve_vacio():
    assert limpiar_texto("   \n\n   \t  ") == ""