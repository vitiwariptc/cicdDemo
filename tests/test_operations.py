from src.mathOperations import add, sub

def test_add():
	assert add(2, 3) == 5

def test_diff():
	assert sub(4, 5) == -1