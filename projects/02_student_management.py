"""
Project 2: Student Management System (شاگردوں کا نظام)
پروجیکٹ 2: شاگردوں کا انتظامی نظام
"""

import json
import os

class StudentManagementSystem:
    """شاگردوں کو منظم کریں"""
    
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()
    
    def load_students(self):
        """شاگردوں کو لوڈ کریں"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    
    def save_students(self):
        """شاگردوں کو محفوظ کریں"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.students, f, ensure_ascii=False, indent=2)
    
    def add_student(self, name, roll_no, grade):
        """نیا شاگرد شامل کریں"""
        student = {
            "name": name,
            "roll_no": roll_no,
            "grade": grade
        }
        self.students.append(student)
        self.save_students()
        return f"✅ {name} شامل ہو گیا!"
    
    def view_all_students(self):
        """تمام شاگردوں کو دیکھیں"""
        if not self.students:
            return "کوئی شاگرد نہیں!"
        
        result = "\n📚 تمام شاگرد:\n"
        for student in self.students:
            result += f"{student['name']} - رول نمبر: {student['roll_no']} - گریڈ: {student['grade']}\n"
        return result
    
    def delete_student(self, roll_no):
        """شاگرد کو حذف کریں"""
        for i, student in enumerate(self.students):
            if student["roll_no"] == roll_no:
                name = student["name"]
                self.students.pop(i)
                self.save_students()
                return f"✅ {name} حذف ہو گیا!"
        return "❌ شاگرد نہیں ملا!"

# استعمال
if __name__ == "__main__":
    sms = StudentManagementSystem()
    
    print("=== شاگردوں کا نظام ===")
    print(sms.add_student("عائشہ", 101, "A"))
    print(sms.add_student("احمد", 102, "B"))
    print(sms.add_student("فاطمہ", 103, "A+"))
    
    print(sms.view_all_students())
