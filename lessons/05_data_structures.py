"""
Lesson 5: Data Structures
سبق 5: ڈیٹا کی ساختیں
"""

# ============================================
# 1. Lists (لسٹ)
# ============================================
print("--- Lists (لسٹ) ---")
fruits = ["سیب", "آم", "کیلا", "انگور"]

print(f"تمام پھل: {fruits}")
print(f"پہلا پھل: {fruits[0]}")
print(f"آخری پھل: {fruits[-1]}")
print(f"لسٹ کی لمبائی: {len(fruits)}")

# Add item
fruits.append("آڑو")
print(f"آڑو شامل کرنے کے بعد: {fruits}")

# Remove item
fruits.remove("کیلا")
print(f"کیلا نکالنے کے بعد: {fruits}")

# ============================================
# 2. Tuples (ٹپل)
# ============================================
print("\n--- Tuples (ٹپل) ---")
colors = ("سرخ", "سبز", "نیلا")

print(f"تمام رنگ: {colors}")
print(f"دوسرا رنگ: {colors[1]}")
print(f"ٹپل کی لمبائی: {len(colors)}")

# Tuples are immutable (نہیں بدل سکتے)
# colors[0] = "پیلا"  # Error!

# ============================================
# 3. Dictionaries (لغت)
# ============================================
print("\n--- Dictionaries (لغت) ---")
student = {
    "نام": "عائشہ",
    "عمر": 20,
    "شہر": "کراچی",
    "گریڈ": "A"
}

print(f"سب معلومات: {student}")
print(f"نام: {student['نام']}")
print(f"عمر: {student['عمر']}")

# Add new key
student["فون"] = "03001234567"
print(f"فون شامل کرنے کے بعد: {student}")

# ============================================
# 4. Sets (سیٹ)
# ============================================
print("\n--- Sets (سیٹ) ---")
numbers = {1, 2, 3, 4, 5}

print(f"نمبرز: {numbers}")
print(f"سیٹ کی لمبائی: {len(numbers)}")

# Add item
numbers.add(6)
print(f"6 شامل کرنے کے بعد: {numbers}")

# Remove item
numbers.remove(3)
print(f"3 نکالنے کے بعد: {numbers}")

# ============================================
# 5. List Operations
# ============================================
print("\n--- List Operations ---")
scores = [90, 85, 92, 88, 95]

print(f"نمبریں: {scores}")
print(f"کل: {sum(scores)}")
print(f"اوسط: {sum(scores) / len(scores)}")
print(f"زیادہ سے زیادہ: {max(scores)}")
print(f"کم سے کم: {min(scores)}")
print(f"ترتیب شدہ: {sorted(scores)}")
print(f"الٹی ترتیب: {sorted(scores, reverse=True)}")

# ============================================
# 6. Dictionary Operations
# ============================================
print("\n--- Dictionary Operations ---")
book = {
    "عنوان": "Python سیکھیں",
    "مصنف": "احمد",
    "سال": 2024,
    "صفحات": 300
}

print(f"تمام چابیاں: {book.keys()}")
print(f"تمام قیمتیں: {book.values()}")
print(f"تمام چیزیں: {book.items()}")

# ============================================
# 7. Nested Data Structures
# ============================================
print("\n--- Nested Data Structures ---")
school = {
    "نام": "اسلام آباد سکول",
    "شاگرد": [
        {"نام": "عائشہ", "کلاس": 10},
        {"نام": "احمد", "کلاس": 9},
        {"نام": "فاطمہ", "کلاس": 10}
    ]
}

print(f"سکول کا نام: {school['نام']}")
print(f"پہلے شاگرد کا نام: {school['شاگرد'][0]['نام']}")

# ============================================
# 8. List Slicing
# ============================================
print("\n--- List Slicing ---")
letters = ["A", "B", "C", "D", "E", "F"]

print(f"تمام: {letters}")
print(f"پہلے تین: {letters[0:3]}")
print(f"آخری دو: {letters[-2:]}")
print(f"ہر دوسرا: {letters[::2]}")

# ============================================
# 9. Practical Example
# ============================================
print("\n--- عملی مثال: کلاس کے نتائج ---")
class_results = {
    "عائشہ": [85, 90, 88],
    "احمد": [92, 88, 95],
    "فاطمہ": [78, 82, 80]
}

for student, marks in class_results.items():
    average = sum(marks) / len(marks)
    print(f"{student}: اوسط = {average:.2f}")
