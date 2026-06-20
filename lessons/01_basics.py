"""
Lesson 1: Python Basics
سبق 1: Python کی بنیادیں
"""

# ============================================
# 1. Print Statement اور Output
# ============================================
print("السلام علیکم! خوش آمدید")
print("Hello, World!")
print("Python میں خوش آمدید")

# ============================================
# 2. Variables (متغیرات)
# ============================================
name = "عائشہ"
age = 25
height = 5.6
is_student = True

print(f"نام: {name}")
print(f"عمر: {age}")
print(f"قد: {height}")

# ============================================
# 3. Data Types (ڈیٹا کی اقسام)
# ============================================
# Integer
count = 42

# Float
price = 99.99

# String
message = "Python سیکھنا مزہ دار ہے!"

# Boolean
is_learning = True

print(type(count))      # <class 'int'>
print(type(price))      # <class 'float'>
print(type(message))    # <class 'str'>
print(type(is_learning)) # <class 'bool'>

# ============================================
# 4. Arithmetic Operations (ریاضیاتی کام)
# ============================================
x = 10
y = 3

print(f"جمع: {x} + {y} = {x + y}")
print(f"تفریق: {x} - {y} = {x - y}")
print(f"ضرب: {x} * {y} = {x * y}")
print(f"تقسیم: {x} / {y} = {x / y}")
print(f"بقیہ: {x} % {y} = {x % y}")
print(f"طاقت: {x} ** {y} = {x ** y}")

# ============================================
# 5. String Operations (متن کے کام)
# ============================================
first_name = "عائشہ"
last_name = "امیر"
full_name = first_name + " " + last_name

print(f"مکمل نام: {full_name}")
print(f"لمبائی: {len(full_name)}")
print(f"بڑے حروف: {full_name.upper()}")
print(f"چھوٹے حروف: {full_name.lower()}")

# ============================================
# 6. Input from User (صارف سے ان پٹ)
# ============================================
# user_input = input("اپنا نام بتائیں: ")
# print(f"خوش آمدید {user_input}!")
