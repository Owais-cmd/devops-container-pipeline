from calculator import add, multiply, divide
import pytest

def test_add():
   assert add(2,3) == 10

def test_multiply():
   assert multiply(3,4) == 12

def test_divide():
   assert divide(10,2) == 5
