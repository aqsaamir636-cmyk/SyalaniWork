"""
Lesson 9: Modules & Packages (ماڈیولز اور پیکجز)
سبق 9: ماڈیولز اور پیکجز
"""

# ============================================
# 1. Built-in Modules
# ============================================
print("--- بنی ہوئی ماڈیولز ---")

import math
import random
import datetime

# Math module
print(f"π کی قدر: {math.pi}")
print(f"√16 = {math.sqrt(16)}")
print(f"sin(90°) = {math.sin(math.radians(90))}")

# Random module
print(f"\nتصادفی نمبر: {random.randint(1, 100)}")
print(f"تصادفی انتخاب: {random.choice(['عائشہ', 'احمد', 'فاطمہ'])}")

# Datetime module
now = datetime.datetime.now()
print(f"\nموجودہ وقت: {now}")
print(f"سال: {now.year}, ماہ: {now.month}, دن: {now.day}")

# ============================================
# 2. Using OS Module
# ============================================
print("\n--- OS ماڈیول ---")

import os

print(f"موجودہ ڈائریکٹری: {os.getcwd()}")
print(f"فائلیں: {os.listdir('.')}")

# ============================================
# 3. Using Collections Module
# ============================================
print("\n--- Collections ماڈیول ---")

from collections import Counter, defaultdict

# Counter
words = ["Python", "Python", "Java", "Python", "C++"]
count = Counter(words)
print(f"الفاظ کی تعداد: {count}")

# defaultdict
student_grades = defaultdict(list)
student_grades["عائشہ"].append(90)
student_grades["احمد"].append(85)
print(f"نمبرات: {dict(student_grades)}")

# ============================================
# 4. Using Itertools Module
# ============================================
print("\n--- Itertools ماڈیول ---")

from itertools import combinations, permutations

# Combinations
combos = list(combinations([1, 2, 3], 2))
print(f"امتزاجات: {combos}")

# ============================================
# 5. Creating Custom Module
# ============================================
print("\n--- اپنی ماڈیول بنائیں ---")

# یہ کوڈ save کریں: my_module.py
# def greet(name):
#     return f"السلام علیکم {name}!"
# 
# def add(a, b):
#     return a + b

# اب import کریں:
# from my_module import greet, add
# print(greet("عائشہ"))
# print(add(5, 3))
