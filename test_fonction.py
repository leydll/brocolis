from app import calculer_moyenne

def test_calculer_moyenne_standard():
    assert calculer_moyenne([10, 20, 30]) == 20

def test_calculer_moyenne_vide():
    assert calculer_moyenne([]) == 0

def test_calculer_moyenne_un_element():
    assert calculer_moyenne([5]) == 5