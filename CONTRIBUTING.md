# 🤝 Contributing to SyalaniWork

> SyalaniWork میں اپنا حصہ ڈالیں! ہم سب کے تعاون کی خوشخبری دیتے ہیں۔

---

## 🎯 Contributing Guidelines

### کیسے شامل ہو سکتے ہیں:

1. **Bugs Report کریں** 🐛
2. **Features suggest کریں** ✨
3. **Documentation improve کریں** 📝
4. **Code contribute کریں** 💻
5. **Projects add کریں** 🚀

---

## 📋 Process

### Step 1: Fork کریں
```bash
git clone https://github.com/YOUR-USERNAME/SyalaniWork.git
cd SyalaniWork
```

### Step 2: Branch بنائیں
```bash
git checkout -b feature/amazing-feature
# یا
git checkout -b bugfix/issue-name
```

### Step 3: Changes کریں
```bash
# اپنی تبدیلیاں کریں
# Tests چلائیں
pytest tests/
```

### Step 4: Commit کریں
```bash
git add .
git commit -m "Add: meaningful description" 
# یا
git commit -m "Fix: bug description"
```

### Step 5: Push کریں
```bash
git push origin feature/amazing-feature
```

### Step 6: Pull Request کھولیں
- GitHub پر جائیں
- "New Pull Request" button دبائیں
- اپنا branch select کریں
- Description اردو یا انگریزی میں لکھیں
- Submit کریں

---

## 📝 Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

### Types:
- `feat:` - نیا feature
- `fix:` - bug fix
- `docs:` - documentation
- `test:` - tests
- `refactor:` - code refactoring

### مثالیں:
```
feat: Add lesson 11 on decorators
fix: Fix file reading bug
docs: Update README with examples
test: Add unit tests for calculator
```

---

## 🎨 Code Style

### Python Conventions:
```python
# ✅ Good
def calculate_average(numbers):
    """نمبرز کی اوسط نکالیں"""
    return sum(numbers) / len(numbers)

# ❌ Bad
def calc_avg(nums):
    return sum(nums)/len(nums)
```

### نام رکھنے کے اصول:
- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`

---

## ✅ Testing

### نیا feature شامل کریں تو:

```bash
# Tests لکھیں
pytest tests/ -v

# Coverage check کریں
pytest --cov
```

### مثال:
```python
# tests/test_new_feature.py
def test_new_function():
    result = new_function(10)
    assert result == expected_output
```

---

## 📚 Documentation

ہر function میں docstring ہونی چاہیے:

```python
def process_data(data):
    """
    ڈیٹا کو process کریں۔
    
    Args:
        data (list): ڈیٹا کی لسٹ
        
    Returns:
        dict: نتیجہ
        
    Example:
        >>> result = process_data([1, 2, 3])
        >>> print(result)
    """
    pass
```

---

## 🎯 Contributing Ideas

### Lessons:
- [ ] Advanced OOP (Metaclasses)
- [ ] Design Patterns
- [ ] Database Integration
- [ ] Testing & Debugging
- [ ] Performance Optimization

### Projects:
- [ ] Weather Application
- [ ] Blog Platform
- [ ] Chat Application
- [ ] E-Commerce Site
- [ ] Social Media Clone

### Documentation:
- [ ] Video Tutorials
- [ ] Interview Questions
- [ ] Best Practices Guide
- [ ] Troubleshooting Guide

---

## 🏆 Recognition

بہترین contributions کے لیے:

- 🌟 Contributors list میں نام
- 📝 Release notes میں credit
- 🎁 Special badge
- 💌 Thank you message

---

## ⚠️ Code of Conduct

### ہم expect کرتے ہیں:
✅ Respectful communication  
✅ Constructive feedback  
✅ Inclusive behavior  
✅ Professional tone  

### ہم accept نہیں کرتے:
❌ Harassment  
❌ Discrimination  
❌ Spamming  
❌ Self-promotion  

---

## 🐛 Bug Report کیسے کریں

```
Title: [BUG] اختصار میں مسئلہ

Description:
1. کیا کریں گے؟
2. کیا ہوتا ہے?
3. کیا ہونا چاہیے?

Code:
```python
# Minimal example
```

Expected:
[نتیجہ]

Actual:
[غلط نتیجہ]
```

---

## ✨ Feature Request

```
Title: [FEATURE] feature کا نام

Description:
فیچر کے لیے use case

Benefit:
کیا فائدہ ہوگا

Example:
کیسے use ہوگا
```

---

## 🔗 Useful Links

- [GitHub Fork Guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [Pull Request Guide](https://docs.github.com/en/pull-requests)
- [Markdown Guide](https://www.markdownguide.org/)
- [Python PEP 8](https://pep8.org/)

---

## 💬 Questions?

- GitHub Discussions میں پوچھیں
- Issues میں detail سے لکھیں
- Email کریں: 263402958+aqsaamir636-cmyk@users.noreply.github.com

---

**شکریہ اپنا حصہ ڈالنے کے لیے! 🙏**

**Together we build better! 🚀**
