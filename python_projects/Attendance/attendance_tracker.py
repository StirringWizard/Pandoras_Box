import tkinter as tk
from tkinter import filedialog
import pandas as pd

class AttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance System")
        
        # Variables
        self.file_path = tk.StringVar()
        self.attendance_data = None
        
        # Menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Search
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(pady=10)
        
        self.search_label = tk.Label(self.search_frame, text="Search:")
        self.search_label.grid(row=0, column=0)
        
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.grid(row=0, column=1)
        
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search)
        self.search_button.grid(row=0, column=2)
        
        # Mark Attendance
        self.mark_frame = tk.Frame(self.root)
        self.mark_frame.pack(pady=10)
        
        self.absent_var = tk.BooleanVar()
        self.absent_checkbox = tk.Checkbutton(self.mark_frame, text="Absent", variable=self.absent_var)
        self.absent_checkbox.grid(row=0, column=0)
        
        self.planned_absent_var = tk.BooleanVar()
        self.planned_absent_checkbox = tk.Checkbutton(self.mark_frame, text="Planned Absent", variable=self.planned_absent_var)
        self.planned_absent_checkbox.grid(row=0, column=1)
        
        self.mark_button = tk.Button(self.mark_frame, text="Mark", command=self.mark_attendance)
        self.mark_button.grid(row=0, column=2)
        
        # Textbox to pick CSV
        self.file_entry = tk.Entry(self.root, textvariable=self.file_path, width=50)
        self.file_entry.pack(pady=10)
        
        self.file_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.file_button.pack()
    
    def browse_file(self):
        filename = filedialog.askopenfilename(initialdir="./", title="Select file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        self.file_path.set(filename)
        self.load_data()
    
    def load_data(self):
        try:
            self.attendance_data = pd.read_csv(self.file_path.get())
        except Exception as e:
            print("Error:", e)
            self.attendance_data = None
    
    def search(self):
        if self.attendance_data is not None:
            query = self.search_entry.get()
            result = self.attendance_data[self.attendance_data['Name'].str.contains(query, case=False)]
            print(result)
        else:
            print("No data loaded.")
    
    def mark_attendance(self):
        if self.attendance_data is not None:
            query = self.search_entry.get()
            index = self.attendance_data[self.attendance_data['Name'].str.contains(query, case=False)].index
            if len(index) > 0:
                if self.absent_var.get():
                    self.attendance_data.at[index[0], 'Attendance'] = 'Absent'
                elif self.planned_absent_var.get():
                    self.attendance_data.at[index[0], 'Attendance'] = 'Planned Absent'
                else:
                    self.attendance_data.at[index[0], 'Attendance'] = 'Present'
                print("Attendance marked for", query)
                print(self.attendance_data)
            else:
                print("Name not found.")
        else:
            print("No data loaded.")

root = tk.Tk()
app = AttendanceSystem(root)
root.mainloop()
