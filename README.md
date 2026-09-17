# 🛡️ ShieldPass : Password Strength Assessment & Generation Engine

**ShieldPass** is a Python-based password security tool that evaluates password strength using multiple security criteria and can also generate strong random passwords.

The project analyzes a password based on:

- 🔢 Password length
- 🔠 Uppercase and lowercase characters
- 🔢 Numbers
- 🔐 Special characters
- ⚠️ Common password patterns
- 📊 Estimated entropy
- ⏱️ Estimated crack-time category

It also includes a secure password generator using Python's `random.SystemRandom`.

---

## 🚀 Features

### 1. Password Strength Assessment

ShieldPass calculates a password score from **0 to 4**.

| Score | Strength | Indicator |
|------:|----------|-----------|
| 0 | Very Weak | 🔴 Red |
| 1 | Weak | 🟠 Orange |
| 2 | Medium | 🟡 Yellow |
| 3 | Strong | 🟢 Green |
| 4 | Very Strong | 🔵 Cyan |

The score considers password length, character diversity, and common patterns.

### 2. Character Complexity Analysis

The password is checked for four character categories:

- Lowercase letters: `a-z`
- Uppercase letters: `A-Z`
- Numbers: `0-9`
- Special characters: `! @ # $ % ...`

Example:

```text
Password: Hello@123

Lowercase  ✓
Uppercase  ✓
Number     ✓
Special    ✓

Complexity: 4 / 4
```

### 3. Common Pattern Detection

ShieldPass detects commonly used patterns such as:

```text
123
abc
qwerty
password
```

If a common pattern is detected, the password receives a score penalty and a security recommendation is displayed.

### 4. Entropy Calculation

ShieldPass estimates password entropy using:

```text
Entropy = Password Length × log₂(Character Set Size)
```

A larger entropy value generally indicates a larger theoretical password search space.

### 5. Password Generator

ShieldPass can generate random passwords containing:

- Lowercase letters
- Uppercase letters
- Numbers
- Special characters

Default password length:

```python
generate_password(16)
```

The generator uses:

```python
random.SystemRandom()
```

---

## 🛠️ Technologies Used

- **Python 3**
- `math`
- `re`
- `random`
- `string`

No external Python packages are required.

---

## 📂 Project Structure

```text
ShieldPass/
│
├── shieldpass.py
└── README.md
```

> Rename `shieldpass.py` if your actual Python filename is different.

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/ShieldPass.git
```

### Step 2: Navigate to the Project

```bash
cd ShieldPass
```

### Step 3: Run the Program

```bash
python shieldpass.py
```

Or:

```bash
python3 shieldpass.py
```

---

## 💻 How It Works

```text
              ┌─────────────────────┐
              │   Enter Password     │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Check Length      │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Character Complexity│
              │ Lower / Upper / Num │
              │ Special Characters  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Common Pattern Check│
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Entropy Calculation │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Calculate Score     │
              │      0 → 4          │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Strength + Feedback │
              └─────────────────────┘
```

---

## 📊 Scoring Logic

### Password Length

| Condition | Score |
|-----------|------:|
| Less than 8 characters | No length point |
| 8+ characters | +1.0 |
| 12+ characters | +0.5 additional |

### Character Complexity

| Condition | Score |
|-----------|------:|
| Uppercase + lowercase | +1.0 |
| Contains number | +1.0 |
| Contains special character | +1.0 |

### Common Pattern Penalty

If the password contains patterns such as:

```text
123
abc
qwerty
password
```

the score is reduced by:

```text
-1.5
```

The final score is restricted to:

```text
0 ≤ Score ≤ 4
```

---

## 🔐 Security Considerations

ShieldPass is an **educational password-strength assessment tool**.

The entropy and crack-time calculations are heuristic estimates and should **not** be treated as guarantees of how long a real attacker would need to crack a password.

Actual password security depends on factors such as:

- Password hashing algorithm
- Hashing parameters
- Hardware available to an attacker
- Rate limiting
- Multi-factor authentication
- Password reuse
- Whether the password has appeared in a breached-password database

For production authentication systems, passwords should be securely hashed using dedicated password-hashing algorithms such as **Argon2id, scrypt, or bcrypt**, rather than storing plaintext passwords.

---

## 🎯 Project Objectives

The main objectives of ShieldPass are:

1. Understand password security fundamentals.
2. Implement password-strength evaluation in Python.
3. Analyze character complexity.
4. Implement entropy-based estimation.
5. Detect common password patterns.
6. Generate strong random passwords.
7. Provide actionable feedback to users.
8. Practice Python regular expressions and functions.

---

## 🔮 Future Improvements

- [ ] GUI interface using Tkinter
- [ ] Web interface using Flask or FastAPI
- [ ] Password breach checking using a privacy-preserving API
- [ ] More comprehensive common-password detection
- [ ] Password strength meter
- [ ] Copy-to-clipboard functionality
- [ ] Configurable password-generation rules
- [ ] Unit testing
- [ ] REST API support
- [ ] Docker support

---

## 👨‍💻 Author

**Tarun Kumar**

B.Tech Computer Science & Engineering  
Cyber Security Specialization

---

## 📜 License

This project is intended for **educational and cybersecurity learning purposes**.

You may modify and improve the project for personal, academic, and learning purposes.

---

## ⭐ Support

If you find this project useful for learning Python and cybersecurity concepts, consider giving the repository a ⭐ on GitHub.

**ShieldPass — Build stronger passwords. Learn stronger security. 🔐**
