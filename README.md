# Quick-Calc

## Project Description
**Quick-Calc** is a simple calculator application that performs basic arithmetic operations. It also includes a **Clear** function to reset calculations. This project demonstrates proper software testing practices, including unit and integration testing, and version control using Git and GitHub.

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/swe-testing-assignment.git
cd swe-testing-assignment
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the application
```bash
python cli.py
```
### 4. Run tests
To run all the unit and integration tests, use:
```bash
pytest
```

---

## Testing Framework Research
I evaluated Pytest and Unittest for Python testing:

**Pytest:**
  
• Pros: Simple syntax, powerful fixtures, supports parameterized tests and automatic discovery of test files.

• Cons: Some features require learning its fixtures and plugins.

• Reason chosen: Pytest allows concise, readable tests and integrates easily with CLI + logic design.


**Unittest:**

• Pros: Built into Python, follows xUnit style, widely documented.

• Cons: More verbose, requires class-based test structure, less flexible for modern testing.


**Conclusion:**

Pytest was chosen for its simplicity, readability, and strong support for both unit and integration tests. 

