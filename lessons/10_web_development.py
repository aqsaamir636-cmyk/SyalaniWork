"""
Lesson 10: Web Development with Flask
سبق 10: Flask کے ساتھ ویب ڈیولپمنٹ
"""

# ============================================
# Flask Setup اور Basic App
# ============================================

# pip install flask کریں پہلے!

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ============================================
# 1. Basic Route
# ============================================

@app.route('/')
def home():
    """گھر کا صفحہ"""
    return '''<!DOCTYPE html>
    <html dir="rtl">
    <head>
        <title>خوش آمدید</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>السلام علیکم!</h1>
        <p>Flask میں خوش آمدید!</p>
    </body>
    </html>'''

# ============================================
# 2. JSON Route
# ============================================

@app.route('/api/students')
def get_students():
    """شاگردوں کی معلومات"""
    students = [
        {"name": "عائشہ", "age": 20, "city": "کراچی"},
        {"name": "احمد", "age": 22, "city": "لاہور"},
        {"name": "فاطمہ", "age": 19, "city": "اسلام آباد"}
    ]
    return jsonify(students)

# ============================================
# 3. POST Route
# ============================================

@app.route('/add-student', methods=['POST'])
def add_student():
    """نیا شاگرد شامل کریں"""
    data = request.get_json()
    return jsonify({"status": "success", "message": f"{data.get('name')} شامل ہو گیا!"})

# ============================================
# 4. Dynamic Route
# ============================================

@app.route('/student/<name>')
def student_profile(name):
    """شاگرد کا پروفائل"""
    return f'''
    <h1>پروفائل: {name}</h1>
    <p>نام: {name}</p>
    '''

# ============================================
# 5. Query Parameters
# ============================================

@app.route('/search')
def search():
    """تلاش کریں"""
    query = request.args.get('q', 'کوئی نہیں')
    return f"<h1>تلاش: {query}</h1>"

# ============================================
# Run the app
# ============================================

if __name__ == '__main__':
    print("🚀 Flask app چل رہی ہے...")
    print("📍 URL: http://localhost:5000")
    app.run(debug=True)

# استعمال:
# python lessons/10_web_development.py
