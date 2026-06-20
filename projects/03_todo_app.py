"""
Project 3: To-Do List App (کام کی فہرست)
پروجیکٹ 3: کام کی فہرست ایپ
"""

import json
import os
from datetime import datetime

class TodoApp:
    """کام کی فہرست"""
    
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """کام لوڈ کریں"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """کام محفوظ کریں"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)
    
    def add_todo(self, task):
        """نیا کام شامل کریں"""
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.save_todos()
        return f"✅ '{task}' شامل ہو گیا!"
    
    def complete_todo(self, todo_id):
        """کام مکمل کریں"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                self.save_todos()
                return f"✅ '{todo['task']}' مکمل ہو گیا!"
        return "❌ کام نہیں ملا!"
    
    def view_all_todos(self):
        """تمام کام دیکھیں"""
        if not self.todos:
            return "کوئی کام نہیں!"
        
        result = "\n📋 کام کی فہرست:\n"
        for todo in self.todos:
            status = "✅ مکمل" if todo["completed"] else "⏳ زیر التوا"
            result += f"{todo['id']}. {todo['task']} - {status}\n"
        return result

# استعمال
if __name__ == "__main__":
    app = TodoApp()
    
    print("=== کام کی فہرست ===")
    print(app.add_todo("Python سیکھیں"))
    print(app.add_todo("پروجیکٹ بنائیں"))
    print(app.add_todo("دوستوں سے شیئر کریں"))
    
    print(app.view_all_todos())
    
    print(app.complete_todo(1))
    print(app.view_all_todos())
