# 🔐 Password Strength Analyzer & Dictionary Attack Simulator

A Python-based cybersecurity mini-project developed for the **Cyber Security Lab (7CS4-22)** at Swami Keshvanand Institute of Technology, Jaipur.

## 📌 Project Information

| Detail | Description |
|---|---|
| Student Name | Ayesha Agarwal |
| Roll Number | 23ESKCY011 |
| Project Code | CSL-G13 |
| Experiment | Experiment 3 – Dictionary & Brute Force Attack |
| Technology | Python |
| Interface | Streamlit |
| Session | 2026–27 |

## 📖 Project Overview

The Password Strength Analyzer & Dictionary Attack Simulator is an educational cybersecurity application designed to evaluate password strength and demonstrate password-guessing techniques using locally generated test hashes.

The application analyzes passwords based on entropy and common patterns. It also demonstrates dictionary and bounded brute-force attacks against test passwords hashed using MD5, SHA-1 and bcrypt.

## ✨ Features

### 1. Password Strength Analyzer
- Calculates password entropy.
- Detects common password patterns.
- Generates a password strength score.
- Classifies passwords as Weak, Medium or Strong.

### 2. Hash Generator
- MD5 hash generation.
- SHA-1 hash generation.
- bcrypt hash generation.
- bcrypt password verification.

### 3. Dictionary Attack Simulator
- Uses a local password dictionary.
- Tests candidate passwords against generated hashes.
- Supports MD5, SHA-1 and bcrypt.
- Displays attempts and execution time.

### 4. Brute Force Demonstration
- Generates password combinations using a selected character set.
- Supports configurable maximum password length.
- Uses a bounded number of attempts.
- Displays attack results and execution time.

## 🛠️ Technologies Used

- Python
- Streamlit
- hashlib
- bcrypt
- Pandas
- Matplotlib

## 📂 Project Structure

```text
Password_Strength_Analyzer/
│
├── app.py
├── README.md
├── requirements.txt
│
├── modules/
│   ├── __init__.py
│   ├── entropy_calculator.py
│   ├── pattern_detector.py
│   ├── password_analyzer.py
│   ├── hash_generator.py
│   ├── dictionary_attack.py
│   └── brute_force.py
│
├── dataset/
│   └── passwords.txt
│
└── results/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Password_Strength_Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open locally at:

`http://localhost:8501`

## 🔬 Experimental Scope

The project demonstrates:

- Password entropy and pattern analysis.
- MD5, SHA-1 and bcrypt hashing.
- Dictionary-based password guessing.
- Bounded brute-force password guessing.
- Comparison of password hashing behaviour.

## 🔒 Ethical Considerations

This project is developed strictly for educational purposes.

- Only dummy passwords and locally generated test hashes are used.
- Attack simulations are performed offline.
- No real accounts, external systems or unauthorized devices are targeted.
- MD5 and SHA-1 are demonstrated for educational comparison and are not recommended for password storage.

## 🎯 Objective

To understand password security, password hashing algorithms, entropy, common password patterns and the working principles of dictionary and brute-force attacks.

---

**Developed by:** Ayesha Agarwal  
**Institution:** SKIT Jaipur  
**Academic Session:** 2026–27