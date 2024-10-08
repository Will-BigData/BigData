import pytest
from Calculator.implementation import CustomException, CalculatorImp

calculator = CalculatorImp()

def test_addition_success():
    result = calculator.addition(5, 5)
    assert result == 10 # we expect 5 + 5 to equal 10


def test_subtraction_success():
    result = calculator.subtraction(5, 5)
    assert result == 0 # we expect 5 -5 to equal 0


def test_round_success():
    result = calculator.rounding(1.1)
    assert result == 1 # we expect 1.1 rounded to be 1


def test_addition_strings_entered():
    with pytest.raises(CustomException): # this line lets pytest know to fail the test if CustomException is not raised
        result = calculator.addition("one", "two")
        # no assert is needed because of the with pytest line


def test_subtraction_strings_entered():
    with pytest.raises(CustomException):# this line lets pytest know to fail the test if CustomException is not raised
        result = calculator.subtraction("two", "one")
        # no assert is needed because of the with pytest line

def test_round_string_entered():
    with pytest.raises(CustomException):# this line lets pytest know to fail the test if CustomException is not raised
        result = calculator.rounding("five point seven")
        # no assert is needed because of the with pytest line
 

def test_addition_exception_message_correct():
    # we are placing this test in a try/except block because we need to acccess the message of the exception
    try:
        result = calculator.addition(1, "1")
        assert False
    except CustomException as e:
        assert e.message == "One or more entries were not numeric"


def test_subtraction_exception_message_correct():
    # we are placing this test in a try/except block because we need to acccess the message of the exception
    try:
        result = calculator.subtraction(1, "1")
        assert False
    except CustomException as e:
        assert e.message == "One or more entries were not numeric"


def test_round_exception_message_correct():
    # we are placing this test in a try/except block because we need to acccess the message of the exception
    try:
        result = calculator.rounding("1.1")
        assert False
    except CustomException as e:
        assert e.message == "Could not round the value" 
