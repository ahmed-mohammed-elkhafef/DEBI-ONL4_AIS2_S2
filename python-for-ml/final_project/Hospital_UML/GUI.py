import tkinter as tk
root = tk.Tk()
root.geometry('800x500+500+200')
root.title('Hospital Managment System')
root.config(background='red')
root.iconbitmap('D:/01_ENV_AI/DEBI-ONL4/DEBI-ONL4_AIS2_S2/python-for-ml/final_project/Hospital_UML/HMS.ico')

fr1 = tk.Frame(width = '300', height = '500', bg='grey')
fr1.place(x = 1, y = 1)

W = 250        # عرض الزرار
H = 40         # طول الزرار
X_COORD = 20   # مكانه العرضي
START_Y = 20   # مكان أول زرار
SPACE = 50     # المسافة اللي بنزودها عشان ينزل تحت اللي قبله

# 1. Add Department
add_dept = tk.Button(fr1, text='1. Add Department', fg='black', bg='white', anchor='w', padx=10)
add_dept.place(x=X_COORD, y=START_Y, width=W, height=H)

# 2. Remove Department
rem_dept = tk.Button(fr1, text='2. Remove Department', fg='black', bg='white', anchor='w', padx=10)
rem_dept.place(x=X_COORD, y=START_Y + SPACE, width=W, height=H)

# 3. Add Patient
add_pat = tk.Button(fr1, text='3. Add Patient', fg='black', bg='white', anchor='w', padx=10)
add_pat.place(x=X_COORD, y=START_Y + (SPACE * 2), width=W, height=H)

# 4. Remove Patient
rem_pat = tk.Button(fr1, text='4. Remove Patient', fg='black', bg='white', anchor='w', padx=10)
rem_pat.place(x=X_COORD, y=START_Y + (SPACE * 3), width=W, height=H)

# 5. Add Staff
add_staff = tk.Button(fr1, text='5. Add Staff', fg='black', bg='white', anchor='w', padx=10)
add_staff.place(x=X_COORD, y=START_Y + (SPACE * 4), width=W, height=H)

# 6. Remove Staff
rem_staff = tk.Button(fr1, text='6. Remove Staff', fg='black', bg='white', anchor='w', padx=10)
rem_staff.place(x=X_COORD, y=START_Y + (SPACE * 5), width=W, height=H)

# 7. View Basic Info (Patient/Staff)
view_info = tk.Button(fr1, text='7. View Basic Info', fg='black', bg='white', anchor='w', padx=10)
view_info.place(x=X_COORD, y=START_Y + (SPACE * 6), width=W, height=H)

# 8. View Patient Record (Medical)
view_record = tk.Button(fr1, text='8. View Patient Record', fg='black', bg='white', anchor='w', padx=10)
view_record.place(x=X_COORD, y=START_Y + (SPACE * 7), width=W, height=H)

# 9. Exit
exit_btn = tk.Button(fr1, text='9. Exit', fg='white', bg='#c0392b', font=('Arial', 10, 'bold'))
exit_btn.place(x=X_COORD, y=START_Y + (SPACE * 8), width=W, height=H)

root.mainloop()