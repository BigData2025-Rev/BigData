import pytest
from calculatorImp.funexcept import CustomException
from calculatorImp.calculatorMod import CalculatorImp

calculator = CalculatorImp()

def test_addition_success():
    result = calculator.addition(5,5)
    assert result == 10 # we expect 5+5 to equal 10

def subtraction_addition_success():
    result = calculator.addition(5,5)
    assert result == 10 # we expect 5+5 to equal 10

def test_round_success():
    result = calculator.rounding(1.1)
    assert result == 1

def test_addition_strings_entered():
    with pytest.raises(CustomException):
        result = calculator.addition("one", "two")

def test_subtraction_strings_entered():
    with pytest.raises(CustomException):
        result = calculator.subtraction("one", "two")

def test_round_string_entered():
    with pytest.raises(CustomException):
        result = calculator.rounding("five point seven")

def test_addition_exception_message_correct():
    try:
        result = calculator.addition(1, "1")
        assert False
    except CustomException as e:
        assert e.message == "One or more entries were not numeric"

def test_subtraction_exception_message_correct():
    try:
        result = calculator.subtraction(1, "1")
        assert False
    except CustomException as e:
        assert e.message == "One or more entries were not numeric"

def test_round_exception_message_coorect():
    try:
        result = calculator.rounding("1.1")
        assert False
    except CustomException as e:
        assert e.message == "Could not round the value"



                                
                                
