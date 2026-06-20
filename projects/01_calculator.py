"""
Project 1: Advanced Calculator (بہتر شدہ کیلکولیٹر)
پروجیکٹ 1: جدید کیلکولیٹر
"""

class Calculator:
    """بہتر شدہ کیلکولیٹ کریں"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            return "❌ صفر سے تقسیم نہیں ہو سکتی!"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        result = a ** b
        self.history.append(f"{a} ** {b} = {result}")
        return result
    
    def show_history(self):
        """حساب کی تاریخ دکھائیں"""
        if not self.history:
            return "کوئی حساب نہیں!"
        return "\n".join(self.history)
    
    def clear_history(self):
        """تاریخ صاف کریں"""
        self.history = []
        return "✅ تاریخ صاف ہو گئی!"

# استعمال
if __name__ == "__main__":
    calc = Calculator()
    
    print("=== جدید کیلکولیٹر ===")
    print(f"جمع: {calc.add(10, 5)}")
    print(f"تفریق: {calc.subtract(10, 3)}")
    print(f"ضرب: {calc.multiply(4, 5)}")
    print(f"تقسیم: {calc.divide(20, 4)}")
    print(f"طاقت: {calc.power(2, 3)}")
    
    print("\n📝 تاریخ:")
    print(calc.show_history())
