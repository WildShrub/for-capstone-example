
import sys 
from pathlib import Path
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add

def test_add():
    assert add(5,6) == 11

def test_add2():
    assert add(30,15) == 45
def test_add3():
    assert add(5,6) != 10


def test_subtract():
    assert sub(5,6) == -1

def test_subtract2():
    assert sub(30,15) == 15
def test_subtract3():
    assert sub(5,6) != 10
