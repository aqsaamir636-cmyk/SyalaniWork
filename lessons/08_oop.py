"""
Lesson 8: Object-Oriented Programming (OOP)
سبق 8: آبجیکٹ اورینٹیڈ پروگرامنگ
"""

# ============================================
# 1. Basic Class
# ============================================
print("--- بنیادی کلاس ---")

class Student:
    """شاگرد کی کلاس"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"السلام علیکم، میں {self.name} ہوں!"

# Object بنائیں
student1 = Student("عائشہ", 20)
print(student1.greet())
print(f"عمر: {student1.age}")

# ============================================
# 2. Methods (طریقے)
# ============================================
print("\n--- Methods ---")

class Calculator:
    """کیلکولیٹر"""
    
    def __init__(self, name="میرا کیلکولیٹر"):
        self.name = name
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "صفر سے تقسیم نہیں ہو سکتی!"
        return a / b

calc = Calculator()
print(f"جمع: {calc.add(10, 5)}")
print(f"تفریق: {calc.subtract(10, 5)}")
print(f"ضرب: {calc.multiply(10, 5)}")
print(f"تقسیم: {calc.divide(10, 5)}")

# ============================================
# 3. Attributes (خصوصیات)
# ============================================
print("\n--- Attributes ---")

class Car:
    """گاڑی کی کلاس"""
    
    def __init__(self, brand, model, year):
        self.brand = brand      # برانڈ
        self.model = model      # ماڈل
        self.year = year        # سال
        self.speed = 0          # رفتار
    
    def accelerate(self):
        self.speed += 10
        return f"رفتار: {self.speed} کلومیٹر"
    
    def brake(self):
        if self.speed > 0:
            self.speed -= 10
        return f"رفتار: {self.speed} کلومیٹر"
    
    def info(self):
        return f"{self.year} - {self.brand} {self.model}"

car = Car("Toyota", "Corolla", 2024)
print(car.info())
print(car.accelerate())
print(car.accelerate())
print(car.brake())

# ============================================
# 4. Inheritance (وراثت)
# ============================================
print("\n--- Inheritance (وراثت) ---")

class Animal:
    """جانور کی بنیادی کلاس"""
    
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "کوئی آواز"

class Dog(Animal):
    """کتا - Animal سے وراثت"""
    
    def sound(self):
        return f"{self.name} بھاؤں بھاؤں کرتا ہے!"

class Cat(Animal):
    """بلی - Animal سے وراثت"""
    
    def sound(self):
        return f"{self.name} میاؤں میاؤں کرتی ہے!"

dog = Dog("ماکس")
cat = Cat("میٹی")

print(dog.sound())
print(cat.sound())

# ============================================
# 5. Polymorphism (بہت شکلیں)
# ============================================
print("\n--- Polymorphism ---")

animals = [dog, cat]
for animal in animals:
    print(animal.sound())

# ============================================
# 6. Static & Class Methods
# ============================================
print("\n--- Static & Class Methods ---")

class MathOperations:
    """ریاضیاتی کام"""
    
    count = 0  # کلاس متغیر
    
    @staticmethod
    def square(n):
        """مربع نکالیں - static method"""
        return n * n
    
    @classmethod
    def show_count(cls):
        """کل تعداد دکھائیں"""
        return f"کل آپریشنز: {cls.count}"

print(f"16 کا مربع: {MathOperations.square(4)}")

# ============================================
# 7. Properties (خصوصیات)
# ============================================
print("\n--- Properties ---")

class Person:
    """شخص"""
    
    def __init__(self, name, age):
        self.name = name
        self._age = age  # private
    
    @property
    def age(self):
        """عمر حاصل کریں"""
        return self._age
    
    @age.setter
    def age(self, value):
        """عمر سیٹ کریں"""
        if value < 0:
            print("❌ عمر منفی نہیں ہو سکتی!")
        else:
            self._age = value

person = Person("احمد", 25)
print(f"عمر: {person.age}")
person.age = 26
print(f"نئی عمر: {person.age}")

# ============================================
# 8. Practical Example - Bank Account
# ============================================
print("\n--- عملی مثال: بینک اکاؤنٹ ---")

class BankAccount:
    """بینک اکاؤنٹ"""
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance
    
    def deposit(self, amount):
        """رقم جمع کریں"""
        if amount > 0:
            self._balance += amount
            return f"✅ {amount} روپے جمع ہوئے! بیلنس: {self._balance}"
        return "❌ رقم منفی نہیں ہو سکتی!"
    
    def withdraw(self, amount):
        """رقم نکالیں"""
        if amount <= self._balance:
            self._balance -= amount
            return f"✅ {amount} روپے نکلے! بیلنس: {self._balance}"
        return "❌ ناکافی بیلنس!"
    
    def get_balance(self):
        """بیلنس دیکھیں"""
        return f"بیلنس: {self._balance} روپے"

account = BankAccount("عائشہ", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
