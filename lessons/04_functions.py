"""
Lesson 4: Functions
سبق 4: فنکشنز (کام)
"""

# ============================================
# 1. Simple Function
# ============================================
def greet():
    """یہ ایک سادہ سلام ہے"""
    print("السلام علیکم!")

greet()

# ============================================
# 2. Function with Parameters
# ============================================
def greet_person(name):
    """شخص کو سلام کریں"""
    print(f"السلام علیکم {name}!")

greet_person("عائشہ")
greet_person("احمد")

# ============================================
# 3. Function with Multiple Parameters
# ============================================
def add(x, y):
    """دو نمبروں کو جوڑیں"""
    result = x + y
    return result

print(f"10 + 5 = {add(10, 5)}")
print(f"20 + 30 = {add(20, 30)}")

# ============================================
# 4. Function with Default Parameters
# ============================================
def introduce(name, age=18, city="اسلام آباد"):
    """تعارف کروائیں"""
    print(f"نام: {name}")
    print(f"عمر: {age}")
    print(f"شہر: {city}")
    print()

introduce("عائشہ")
introduce("احمد", 25)
introduce("فاطمہ", 30, "کراچی")

# ============================================
# 5. Function with Return Multiple Values
# ============================================
def get_user_info():
    """یوزر کی معلومات"""
    name = "عائشہ"
    age = 25
    return name, age

user_name, user_age = get_user_info()
print(f"نام: {user_name}, عمر: {user_age}\n")

# ============================================
# 6. Function with List Parameter
# ============================================
def sum_list(numbers):
    """لسٹ کے تمام نمبروں کا جمع"""
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_list([1, 2, 3, 4, 5])
print(f"جمع: {result}\n")

# ============================================
# 7. Function with Loop
# ============================================
def print_table(number, lines=5):
    """نمبر کا جدول بنائیں"""
    print(f"{number} کا جدول:")
    for i in range(1, lines + 1):
        print(f"{number} × {i} = {number * i}")
    print()

print_table(5)
print_table(3, 7)

# ============================================
# 8. Function with Conditions
# ============================================
def check_number(num):
    """نمبر کی جانچ کریں"""
    if num > 0:
        return "مثبت"
    elif num < 0:
        return "منفی"
    else:
        return "صفر"

print(f"15 {check_number(15)} ہے")
print(f"-5 {check_number(-5)} ہے")
print(f"0 {check_number(0)} ہے\n")

# ============================================
# 9. Function with *args
# ============================================
def sum_all(*numbers):
    """کتنے بھی نمبروں کا جمع"""
    return sum(numbers)

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40) = {sum_all(10, 20, 30, 40)}\n")

# ============================================
# 10. Function with **kwargs
# ============================================
def print_student(**info):
    """سکول کے بچے کی معلومات"""
    for key, value in info.items():
        print(f"{key}: {value}")
    print()

print_student(name="عائشہ", age=15, school="سیکنڈری")
print_student(name="احمد", grade="10th", marks=85)

# ============================================
# 11. Recursive Function
# ============================================
def factorial(n):
    """فیکٹوریل حساب کریں"""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"5! = {factorial(5)}\n")

# ============================================
# 12. Practical Examples
# ============================================
def convert_to_urdu_numbers(num):
    """ہندسوں کو اردو میں بدلیں"""
    urdu_digits = {
        0: "۰", 1: "۱", 2: "۲", 3: "۳", 4: "۴",
        5: "۵", 6: "۶", 7: "۷", 8: "۸", 9: "۹"
    }
    return "".join(urdu_digits[int(digit)] for digit in str(num))

print(f"123 اردو میں: {convert_to_urdu_numbers(123)}")
print(f"5678 اردو میں: {convert_to_urdu_numbers(5678)}")
