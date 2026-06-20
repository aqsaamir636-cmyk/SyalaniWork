"""
Lesson 6: File Handling (فائلوں کے ساتھ کام)
سبق 6: فائل ہینڈلنگ
"""

# ============================================
# 1. Writing to a File (فائل میں لکھنا)
# ============================================
print("--- فائل میں لکھنا ---")

# Simple write
with open("message.txt", "w", encoding="utf-8") as file:
    file.write("السلام علیکم!\n")
    file.write("یہ ایک فائل ہے۔\n")

print("✅ فائل محفوظ ہو گئی!")

# ============================================
# 2. Reading from a File (فائل سے پڑھنا)
# ============================================
print("\n--- فائل سے پڑھنا ---")

with open("message.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# ============================================
# 3. Reading Line by Line
# ============================================
print("--- لائن در لائن پڑھنا ---")

with open("message.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f">> {line.strip()}")

# ============================================
# 4. Working with CSV Files
# ============================================
print("\n--- CSV فائلیں ---")

import csv

data = [
    ["نام", "عمر", "شہر"],
    ["عائشہ", 20, "کراچی"],
    ["احمد", 22, "لاہور"],
    ["فاطمہ", 19, "اسلام آباد"]
]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("✅ CSV فائل محفوظ ہو گئی!")

# ============================================
# 5. Working with JSON Files
# ============================================
print("\n--- JSON فائلیں ---")

import json

students_data = {
    "students": [
        {"name": "عائشہ", "age": 20, "city": "کراچی"},
        {"name": "احمد", "age": 22, "city": "لاہور"},
        {"name": "فاطمہ", "age": 19, "city": "اسلام آباد"}
    ]
}

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students_data, file, ensure_ascii=False, indent=2)

print("✅ JSON فائل محفوظ ہو گئی!")
