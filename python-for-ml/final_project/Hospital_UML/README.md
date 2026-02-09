# 🏥 Hospital Management System (UML Implementation)

A **Python-based Object-Oriented Programming (OOP) project** that simulates a hospital management system. This project emphasizes **UML class relationships** such as **Inheritance**, **Composition**, and **Association**, demonstrating clean software design.

---

## 📋 Features

The system is managed by a central `SystemManager` class, providing a unified interface to operate a hospital:

- **Department Management:** Add or remove hospital departments.  
- **Patient Management:** Register new patients or discharge them from specific departments.  
- **Staff Management:** Recruit new staff members or remove them from departments.  
- **Structured OOP Design:** Demonstrates inheritance, aggregation, and composition.

---

## 🏗️ Architecture & UML Design

The project follows a hierarchical and modular design:

1. **Person (Base Class):** Holds common attributes like `name` and `age`.  
2. **Patient & Staff (Subclasses):** Inherit from `Person`.  
   - `Patient` includes `medical_record`.  
   - `Staff` includes `position` or role.  
3. **Department:** Composes lists of `Patients` and `Staff`.  
4. **Hospital:** Aggregates multiple `Department` objects and serves as the container for all hospital operations.  
5. **SystemManager:** Controller class managing the `Hospital` instance and coordinating all operations.

---

## 🚀 How to Run

1. Ensure **Python 3.x** is installed.  
2. Clone or download the repository.  
3. Navigate to the project folder:

```bash
cd python-for-ml/final_project
```

4. Run the main script as a module:

```bash
python -m Hospital_UML.main
```

> ⚠️ **Important:** Do **not** run internal modules (`Patient.py`, `Staff.py`, etc.) directly. Always run `main.py`.

---

## 🛠️ Implementation Details

- **Language:** Python  
- **Paradigm:** Object-Oriented Programming (OOP)  
- **Key Concepts:**
  - `super()` calls for inheritance.  
  - List comprehensions for efficient data manipulation.  
  - Encapsulation of hospital logic within `SystemManager` and `Hospital`.  

---

## 📂 Project Structure

```
Hospital_UML/
├── __init__.py            # Package initializer
├── main.py                # Entry point
├── core/
│   ├── __init__.py
│   └── SystemManger.py    # Main controller
└── model/
    ├── __init__.py
    ├── Person.py          # Base class
    ├── Patient.py         # Patient class
    ├── Staff.py           # Staff class
    ├── Department.py      # Department class
    └── Hospital.py        # Hospital class
```

---

## ⚡ Class Relationships

- `Person` → Base class  
- `Patient` & `Staff` → Inherit from `Person`  
- `Department` → Composes `Patients` & `Staff`  
- `Hospital` → Aggregates `Departments`  
- `SystemManager` → Manages `Hospital` instance  
