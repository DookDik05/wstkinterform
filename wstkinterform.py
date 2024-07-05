import tkinter as tk
from tkinter import messagebox

def submit_form():
    title = title_var.get()
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    birthdate = birthdate_entry.get()
    gender = gender_var.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get("1.0", tk.END)
    district = district_entry.get()
    province = province_entry.get()
    postcode = postcode_entry.get()
    occupation = occupation_var.get()
    hobbies = [hobby for hobby, var in hobbies_vars.items() if var.get()]
    username = username_entry.get()
    password = password_entry.get()

    messagebox.showinfo("Form Submitted", "สมัครเสร็จสิ้น!!!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x650")

# variables
title_var = tk.StringVar(value="กรุณาเลือก")
gender_var = tk.StringVar(value="ชาย")
occupation_var = tk.StringVar(value="กรุณาเลือก")
hobbies_vars = {
    "อ่านหนังสือ": tk.BooleanVar(),
    "เล่นเกม": tk.BooleanVar(),
    "ดูหนัง": tk.BooleanVar(),
    "ฟังเพลง": tk.BooleanVar(),
    "ปลูกต้นไม้": tk.BooleanVar(),
    "ท่องเที่ยว": tk.BooleanVar(),
}

# Create and place widgets
tk.Label(root, text="ข้อมูลส่วนตัว",bg="sky blue", font=("Helvetica", 14)).grid(row=1, column=0)

tk.Label(root, text="สมัครสมาชิก",bg="lime", font=("Helvetica", 16)).grid(row=0, column=1,columnspan=2, pady=10)

tk.Label(root, text="คำนำหน้า:").grid(row=2, column=1, sticky=tk.W)
tk.OptionMenu(root, title_var, "กรุณาเลือก", "นาย", "นาง", "นางสาว").grid(row=2, column=2, sticky=tk.W)

tk.Label(root, text="ชื่อ:").grid(row=3, column=1, sticky=tk.W)
firstname_entry = tk.Entry(root)
firstname_entry.grid(row=3, column=2, sticky=tk.W)

tk.Label(root, text="นามสกุล:").grid(row=4, column=1, sticky=tk.W)
lastname_entry = tk.Entry(root)
lastname_entry.grid(row=4, column=2, sticky=tk.W)

tk.Label(root, text="วันเดือนปีเกิด:").grid(row=5, column=1, sticky=tk.W)
birthdate_entry = tk.Entry(root)
birthdate_entry.grid(row=5, column=2, sticky=tk.W)

tk.Label(root, text="เพศ:").grid(row=6, column=1, sticky=tk.W)
tk.Radiobutton(root, text="ชาย", variable=gender_var, value="ชาย").grid(row=6, column=2, sticky=tk.W)
tk.Radiobutton(root, text="หญิง", variable=gender_var, value="หญิง").grid(row=6, column=2, sticky=tk.E)

tk.Label(root, text="อีเมล์:").grid(row=7, column=1, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=7, column=2, sticky=tk.W)

tk.Label(root, text="เบอร์โทรศัพท์:").grid(row=8, column=1, sticky=tk.W)
phone_entry = tk.Entry(root)
phone_entry.grid(row=8, column=2, sticky=tk.W)

tk.Label(root, text="ที่อยู่ปัจจุบัน:").grid(row=9, column=1, sticky=tk.W)
address_entry = tk.Text(root, height=3, width=20)
address_entry.grid(row=9, column=2, sticky=tk.W)

tk.Label(root, text="อำเภอ:").grid(row=10, column=1, sticky=tk.W)
district_entry = tk.Entry(root)
district_entry.grid(row=10, column=2, sticky=tk.W)

tk.Label(root, text="จังหวัด:").grid(row=11, column=1, sticky=tk.W)
province_entry = tk.Entry(root)
province_entry.grid(row=11, column=2, sticky=tk.W)

tk.Label(root, text="รหัสไปรษณีย์:").grid(row=12, column=1, sticky=tk.W)
postcode_entry = tk.Entry(root)
postcode_entry.grid(row=12, column=2, sticky=tk.W)

tk.Label(root, text="อาชีพ:").grid(row=13, column=1, sticky=tk.W)
tk.OptionMenu(root, occupation_var, "กรุณาเลือก", "นักเรียน", "ครู/อาจารย์").grid(row=13, column=2, sticky=tk.W)

tk.Label(root, text="งานอดิเรก:").grid(row=13, column=1, sticky=tk.W)
row = 13
for hobby, var in hobbies_vars.items():
    row += 1
    tk.Checkbutton(root, text=hobby, variable=var).grid(row=row, column=2, sticky=tk.W)

tk.Label(root, text="ข้อมูลผู้ใช้",bg="pink", font=("Helvetica", 14)).grid(row=20, column=0)

tk.Label(root, text="Username:").grid(row=row+2, column=1, sticky=tk.W)
username_entry = tk.Entry(root)
username_entry.grid(row=row+2, column=2, sticky=tk.W)

tk.Label(root, text="Password:").grid(row=row+3, column=1, sticky=tk.W)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=row+3, column=2, sticky=tk.W)

tk.Button(root, text="สมัครสมาชิก", command=submit_form).grid(row=row+4, column=1, pady=10)
tk.Button(root, text="ยกเลิก", command=root.quit).grid(row=row+4, column=2, pady=10)

# Run
root.mainloop()
