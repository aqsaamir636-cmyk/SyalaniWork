"""
Lesson 3: Loops (دہراو / لوپس)
سبق 3: دہراؤ
"""

# ============================================
# 1. For Loop - Range
# ============================================
print("--- For Loop with Range ---")
for i in range(5):
    print(f"نمبر: {i}")

print("\nRange (1 سے 10 تک):")
for i in range(1, 11):
    print(i, end=" ")

print("\n\nRange (0 سے 20 تک، 2 کی جمپ):")
for i in range(0, 21, 2):
    print(i, end=" ")

# ============================================
# 2. For Loop - List
# ============================================
print("\n\n--- For Loop with List ---")
fruits = ["سیب", "آم", "کیلا", "انگور"]

for fruit in fruits:
    print(f"میری پسندیدہ پھل: {fruit}")

# ============================================
# 3. For Loop - String
# ============================================
print("\n--- For Loop with String ---")
word = "Python"

for letter in word:
    print(letter, end=" ")

# ============================================
# 4. For Loop with Index (Enumerate)
# ============================================
print("\n\n--- For Loop with Index ---")
subjects = ["ریاضی", "سائنس", "اردو", "انگریزی"]

for index, subject in enumerate(subjects):
    print(f"{index + 1}. {subject}")

# ============================================
# 5. While Loop
# ============================================
print("\n--- While Loop ---")
count = 1
while count <= 5:
    print(f"دہراؤ: {count}")
    count += 1

# ============================================
# 6. While Loop - User Input
# ============================================
print("\n--- While Loop with Condition ---")
# password = ""
# while password != "1234":
#     password = input("پاس ورڈ درج کریں: ")
#     if password == "1234":
#         print("صحیح پاس ورڈ!")
#     else:
#         print("غلط پاس ورڈ، دوبارہ کوشش کریں")

# ============================================
# 7. Break Statement
# ============================================
print("\n--- Break Statement ---")
for i in range(10):
    if i == 5:
        print("رکیں! 5 ملا")
        break
    print(i, end=" ")

# ============================================
# 8. Continue Statement
# ============================================
print("\n\n--- Continue Statement ---")
for i in range(6):
    if i == 3:
        print("\n3 کو چھوڑیں", end=" ")
        continue
    print(i, end=" ")

# ============================================
# 9. Nested Loops
# ============================================
print("\n\n--- Nested Loops (ٹیبل) ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()

# ============================================
# 10. Loop with Else
# ============================================
print("\n--- Loop with Else ---")
for i in range(3):
    print(f"لوپ: {i}")
else:
    print("لوپ مکمل ہوا!")

# ============================================
# 11. Practical Examples
# ============================================
print("\n--- عملی مثال 1: نمبروں کا جمع ---")
total = 0
for num in range(1, 6):
    total += num
print(f"1 سے 5 تک کا جمع: {total}")

print("\n--- عملی مثال 2: اردو شمار ---")
for num in range(1, 6):
    if num == 1:
        print("ایک")
    elif num == 2:
        print("دو")
    elif num == 3:
        print("تین")
    elif num == 4:
        print("چار")
    elif num == 5:
        print("پانچ")
