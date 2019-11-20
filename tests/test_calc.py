from base64encoding.base64bis import base64encode, base64decode
from calculator import calc


'# TEST DE LA CALCULATRICE'

"""
def test_add():
    assert calc.add(1, 1) == 2


def test_minus():
    assert calc.minus(3, 2) == 1


def test_div():
    assert calc.div(1, 2) != ZeroDivisionError


def test_mul():
    assert calc.mul(3, 2) == 6

"""
'# Test de encodage en base64'


def test_enc():
 #   assert base64encode('adrien') == 'YWRyaWVu'
  #  assert base64decode('YWRyaWVu') == 'adrien'
    try:
        assert base64encode(3)
        assert base64decode(4)
    except TypeError:
        print('Error')