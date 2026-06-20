"""
Unit Tests for Calculator
کیلکولیٹر کے لیے ٹیسٹس
"""

import pytest
import sys
sys.path.append('..')

from projects.calculator import Calculator

class TestCalculator:
    """کیلکولیٹر ٹیسٹ کریں"""
    
    def setup_method(self):
        """ہر ٹیسٹ سے پہلے چلے"""
        self.calc = Calculator()
    
    def test_add(self):
        """جمع کا ٹیسٹ"""
        assert self.calc.add(10, 5) == 15
    
    def test_subtract(self):
        """تفریق کا ٹیسٹ"""
        assert self.calc.subtract(10, 3) == 7
    
    def test_multiply(self):
        """ضرب کا ٹیسٹ"""
        assert self.calc.multiply(4, 5) == 20
    
    def test_divide(self):
        """تقسیم کا ٹیسٹ"""
        assert self.calc.divide(20, 4) == 5
    
    def test_divide_by_zero(self):
        """صفر سے تقسیم"""
        result = self.calc.divide(10, 0)
        assert "❌" in result

if __name__ == "__main__":
    pytest.main(["-v", __file__])
