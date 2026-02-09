from model.Department import Department
from model.Hospital import Hospital
from model.Patient import Patient
from model.Person import Person
from model.Staff import Staff

class SystemManager:
    """The central manager for all hospital operations (Single Hospital Mode)."""
    def __init__(self, hospital_name):
        # Initializes the system with one specific hospital
        self.hospital = Hospital(hospital_name, "Main Campus")

    # --- 1. Department Management ---
    def add_department(self, dept_name):
        new_dept = Department(dept_name)
        self.hospital.add_department(new_dept)

    def remove_department(self, dept_name):
        original_count = len(self.hospital.departments)
        self.hospital.departments = [d for d in self.hospital.departments if d.name != dept_name]
        if len(self.hospital.departments) < original_count:
            print(f"Success: Department '{dept_name}' has been removed.")
        else:
            print(f"Error: Department '{dept_name}' not found.")

    def _get_dept(self, dept_name):
        """Internal helper to find a department object."""
        for d in self.hospital.departments:
            if d.name == dept_name:
                return d
        return None

    # --- 2. Patient Management ---
    def add_patient(self, dept_name, name, age, record):
        dept = self._get_dept(dept_name)
        if dept:
            new_p = Patient(name, age, record)
            dept.add_patient(new_p)
        else:
            print(f"Error: Department '{dept_name}' not found.")

    def remove_patient(self, dept_name, patient_name):
        dept = self._get_dept(dept_name)
        if dept:
            dept.patients = [p for p in dept.patients if p.name != patient_name]
            print(f"Success: Patient '{patient_name}' removed from {dept_name}.")
        else:
            print(f"Error: Department '{dept_name}' not found.")

    # --- 3. Staff Management ---
    def add_staff(self, dept_name, name, age, position):
        dept = self._get_dept(dept_name)
        if dept:
            new_s = Staff(name, age, position)
            dept.add_staff(new_s)
        else:
            print(f"Error: Department '{dept_name}' not found.")

    def remove_staff(self, dept_name, staff_name):
        dept = self._get_dept(dept_name)
        if dept:
            dept.staff = [s for s in dept.staff if s.name != staff_name]
            print(f"Success: Staff member '{staff_name}' removed from {dept_name}.")
        else:
            print(f"Error: Department '{dept_name}' not found.")