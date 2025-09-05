# 📦 Package Sorter

[![CI](https://github.com/your-username/package-sorter/actions/workflows/python-tests.yml/badge.svg)](https://github.com/your-username/package-sorter/actions)
![coverage](https://img.shields.io/badge/sort.py%20coverage-100%25-brightgreen)

A Python solution to classify packages into different stacks based on their **dimensions** and **mass**.

---

# 📐 Rules

- **Bulky**:

  - Volume `>= 1,000,000 cm³`
  - Or any dimension `>= 150 cm`
- **Heavy**:

  - Mass `>= 20 kg`

  ---

# 🚀 Objective

- **STANDARD** → packages that are neither heavy nor bulky.
- **SPECIAL** → packages that are heavy **or** bulky.
- **REJECTED** → packages that are **both** heavy and bulky.

---

# 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/package-sorter.git
cd package-sorter
```

Create a virtual environment (optional):

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

```python
from sort import sort

print(sort(100, 100, 100, 10))   # STANDARD
print(sort(200, 50, 50, 10))     # SPECIAL
print(sort(200, 200, 200, 25))   # REJECTED
```

---

# ✅ Running Tests

```bash
pytest
```

---

# 📊 Test Coverage (sort.py only)

Run coverage locally:

```bash
coverage run --source=sort -m pytest
coverage report -m
```

Example output:

```
Name      Stmts   Miss  Cover
-----------------------------
sort.py       9      0   100%
```

Generate HTML report:

```bash
coverage html
open htmlcov/index.html
```

---

# 🏆 Author

Developed by **Matheus Kolln** ✨
