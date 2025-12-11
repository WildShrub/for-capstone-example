
import sys 
from pathlib import Path
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add
from app import subtract
from app import multiply
from app import divide
from app import log
from app import square
from app import sin
from app import cos
from app import square_root
from app import percentage


def test_add():
    assert add(5,6) == 11

def test_add2():
    assert add(30,15) == 45
def test_add3():
    assert add(5,6) != 10


def test_subtract():
    assert subtract(10,4) == 6

def test_subtract2():
    assert subtract(20,5) == 15

def test_subtract3():
    assert subtract(10,4) != 5

def test multiply():
    assert multiply(3,7) == 21
def test_multiply2():
    assert multiply(4,5) == 20
def test_multiply3():
    assert multiply(3,7) != 20
def test_multiply4(3,0)
    assert multiply(3,0) == 0
def test_divide():
    assert divide(20,4) == 5
def test_divide2():
    assert divide(15,3) == 5
def test_divide3():
    assert divide(20,4) != 4
def test_divide4():
    assert divide(5,0) == "Error: Division by zero"
def test_log():
    assert log(100,10) == 2
def test_log2():
    assert log(1000,2) == 9.965784284662087
def test_log3():
    assert log(100,2) != 3 
def test_log4():
    assert log(-10,10) == "Error: Invalid input for logarithm"
def test_log5():
    assert log(10,1) == "Error: Invalid input for logarithm"
def test_log6():
    assert log(10,-5) == "Error: Invalid input for logarithm"
def test_log7():
    assert log(0,10) == "Error: Invalid input for logarithm"
def test_log8():
    assert log(10,0) == "Error: Invalid input for logarithm"

def test_square():
    assert square(5) == 25
def test_square2():
    assert square(10) == 100
def test_square3():
    assert square(5) != 20
def test_square3():
    assert square(0) == 0
def test_square4():
    assert square(-4) == 16
def test_square5():
    assert square(1) == 1
def test_square6():
    assert square(-1) == 1

def test_sin():
    assert sin(0) == 0
def test_sin2():
    assert sin(MATH.pi/2) == 1
def test_sin3():
    assert sin(MATH.pi) == 0
def test_sin4():
    assert sin(MATH.pi*3/2) == -1
def test_sin5():
    assert sin(MATH.pi*2) == 0

def test_sin6():
    #quadrant I
    assert sin(1) > 0
def test_sin7(): 
    #quadrant II
    assert sin(2) > 0
def test_sin8():
    #quadrant III
    assert sin(4) < 0
def test_sin9():
    #quadrant IV
    assert sin(5) < 0



def test_cos():
    assert cos(0) == 1
def test_cos2():
    assert cos(MATH.pi/2) == 0
def test_cos3():
    assert cos(MATH.pi) == -1
def test_cos4():
    assert cos(MATH.pi*3/2) == 0
def test_cos5():
    assert cos(MATH.pi*2) == 1

def test_cos6():
    #quadrant I
    assert cos(1) > 0
def test_cos7(): 
    #quadrant II
    assert cos(2) < 0
def test_cos8():
    #quadrant III
    assert cos(4) < 0
def test_cos9():
    #quadrant IV
    assert cos(5) > 0

def test_square_root():
    assert square_root(25) == 5
def test_square_root2():
    assert square_root(0) == 0
def test_square_root3():
    assert square_root(16) == 4
def test_square_root4():
    assert square_root(-9) == "Error: Negative input for square root"
def test_square_root5():
    assert square_root(2) == MATH.sqrt(2)


def test_percentage():
    assert percentage(50,200) == 25.0
def test_percentage2():
    assert percentage(30,150) == 20.0
def test_percentage3():
    assert percentage(50,200) != 30.0
def test_percentage4():
    assert percentage(10,0) == "Error: Division by zero"
def test_percentage5():
    assert percentage(0,100) == 0.0
def test_percentage6():
    assert percentage(75,300) == 25.0
def test_percentage7():
    assert percentage(-50,200) == "Error: Negative input for percentage"
def test_percentage8():
    assert percentage(50,-200) == "Error: Negative input for percentage"
def test_percentage9():
    assert percentage(-50,-200) == "Error: Negative input for percentage"
def test_percentage10():
    assert percentage(1,1) == 100.0 

