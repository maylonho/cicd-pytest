import pytest
from app.calculadora import *

def test_soma():
    assert soma(2,3) == 5