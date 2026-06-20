"""
Lesson 2: Conditional Statements
سبق 2: شرطی بیان
"""

# ============================================
# 1. If Statement
# ============================================
age = 20

if age >= 18:
    print("آپ بالغ ہیں")
else:
    print("آپ نابالغ ہیں")

# ============================================
# 2. If-Else-If (Multiple Conditions)
# ============================================
marks = 75

if marks >= 80:
    print("گریڈ: A")
elif marks >= 70:
    print("گریڈ: B")
elif marks >= 60:
    print("گریڈ: C")
else:
    print("گریڈ: F")

# ============================================
# 3. Nested If
# ============================================
username = "aqsa"
password = "123456"
is_verified = True

if username == "aqsa":
    if password == "123456":
        if is_verified:
            print("خوش آمدید!")
        else:
            print("براہ کرم ای میل تصدیق کریں")
    else:
        print("غلط پاس ورڈ")
else:
    print("صارف نہیں ملا")

# ============================================
# 4. Comparison Operators
# ============================================
x = 10
y = 20

print(f"x > y: {x > y}")      # False
print(f"x < y: {x < y}")      # True
print(f"x == y: {x == y}")    # False
print(f"x != y: {x != y}")    # True
print(f"x >= 10: {x >= 10}")  # True
print(f"x <= 10: {x <= 10}")  # True

# ============================================
# 5. Logical Operators
# ============================================
is_working = True
has_experience = True

if is_working and has_experience:
    print("آپ کو نوکری مل سکتی ہے")

is_student = True
is_free = True

if is_student or is_free:
    print("آپ حاضر ہو سکتے ہیں")

is_summer = False

if not is_summer:
    print("سردیوں کا موسم ہے")

# ============================================
# 6. Membership Operators
# ============================================
fruits = ["سیب", "آم", "کیلا"]

if "سیب" in fruits:
    print("سیب درست ہے")

if "انگور" not in fruits:
    print("انگور نہیں ہے")

# ============================================
# 7. Practical Example
# ============================================
print("\n--- عملی مثال ---")
number = 15

if number > 0:
    if number % 2 == 0:
        print(f"{number} ایک مثبت اور جفت نمبر ہے")
    else:
        print(f"{number} ایک مثبت اور طاق نمبر ہے")
elif number < 0:
    print(f"{number} ایک منفی نمبر ہے")
else:
    print("یہ صفر ہے")
