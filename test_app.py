from app import factorial

def test_factorial():
    # Test case to verify the correctness of the application [cite: 14]
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    # assert factorial(-5) == "Factorial is not defined for negative numbers"