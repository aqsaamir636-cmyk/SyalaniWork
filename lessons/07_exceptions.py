"""
Lesson 7: Exception Handling (غلطیوں کو سنبھالنا)
سبق 7: ایکسیپشن ہینڈلنگ
"""

# ============================================
# 1. Try-Except Basic
# ============================================
print("--- غلطی سنبھالنا ---")

try:
    number = int(input("نمبر درج کریں: "))
    result = 10 / number
    print(f"نتیجہ: {result}")
except ZeroDivisionError:
    print("❌ صفر سے تقسیم نہیں ہو سکتی!")
except ValueError:
    print("❌ براہ کرم صحیح نمبر درج کریں!")

# ============================================
# 2. Multiple Exceptions
# ============================================
print("\n--- متعدد غلطیاں ---")

try:
    numbers = [1, 2, 3]
    print(numbers[5])  # IndexError
except IndexError:
    print("❌ یہ index موجود نہیں ہے!")
except KeyError:
    print("❌ یہ key موجود نہیں ہے!")

# ============================================
# 3. Generic Exception
# ============================================
print("\n--- عام Exception ---")

try:
    x = "متن" + 5  # TypeError
except Exception as e:
    print(f"❌ غلطی: {e}")
    print(f"📌 قسم: {type(e).__name__}")

# ============================================
# 4. Finally Block
# ============================================
print("\n--- Finally بلاک ---")

try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("❌ فائل نہیں ملی!")
finally:
    print("✅ Finally بلاک ہمیشہ چلتا ہے!")

# ============================================
# 5. Else Block
# ============================================
print("\n--- Else بلاک ---")

try:
    number = 10
    result = 100 / number
except ZeroDivisionError:
    print("❌ خرابی ہوئی!")
else:
    print(f"✅ نتیجہ: {result}")

# ============================================
# 6. Custom Exceptions
# ============================================
print("\n--- اپنی Exception ---")

class NegativeNumberError(Exception):
    """منفی نمبر کے لیے Exception"""
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("نمبر منفی نہیں ہو سکتا!")
    return num * 2

try:
    result = check_positive(-5)
except NegativeNumberError as e:
    print(f"❌ {e}")

# ============================================
# 7. Raising Exceptions
# ============================================
print("\n--- Exception پھینکنا ---")

def divide(a, b):
    if b == 0:
        raise ValueError("تقسیم کنے والا صفر نہیں ہو سکتا!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"❌ {e}")

# ============================================
# 8. Type Errors
# ============================================
print("\n--- قسم کی غلطیاں ---")

try:
    text = "Python"
    print(text[10])  # IndexError
except (IndexError, KeyError) as e:
    print(f"❌ غلطی: {type(e).__name__}")

# ============================================
# 9. Practical Example - Safe Calculation
# ============================================
print("\n--- عملی مثال: محفوظ حساب ---")

def safe_divide(a, b):
    """محفوظ طریقے سے تقسیم کریں"""
    try:
        a = float(a)
        b = float(b)
        
        if b == 0:
            raise ZeroDivisionError("صفر سے تقسیم ممکن نہیں!")
        
        return a / b
    except ValueError:
        return "❌ براہ کرم صحیح نمبر درج کریں!"
    except ZeroDivisionError as e:
        return f"❌ {e}"
    finally:
        print("📝 حساب مکمل ہو گیا!")

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("abc", 5))

# ============================================
# 10. File Handling with Exceptions
# ============================================
print("\n--- فائل کے ساتھ Exception ---")

def read_file(filename):
    """محفوظ طریقے سے فائل پڑھیں"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"❌ فائل '{filename}' نہیں ملی!"
    except IOError:
        return "❌ فائل پڑھنے میں خرابی!"

result = read_file("nonexistent.txt")
print(result)
