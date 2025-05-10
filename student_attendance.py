class Attendence_System:
    
    def __init__(self, attendance_list, late_students):
        self.attendance_list = set()
        self.late_students = set()
        
    def mark_present(self, student_name):
        self.attendance_list.add(student_name)
        
    def mark_absent(self, student_name):
        self.attendance_list.discard(student_name)
        
    def count_present(slef):
        return len(self.attendance_list)
    
    def mark_late(self, student_name):
        self.late_students.add(student_name)
        
    def check_late_in_attendance(self):
        return self.attendance_list.intersection(self.late_students)
    
attendance = Attendence_System()
attendance.mark_present("indrayani")
attendance.mark_present("Dhanashri")
attendance.mark_present("Naitik")
attendance.mark_late("mohini")
attendance.mark_absent("hetashri")

print(f"Number of students present: {attendance.count_present()}")

late_in_attendance = attendance.check_late_in_attendance()
if late_in_attendance:
    print(f"Late students present :{','.join(late_in_attendance)}")
else:
    print("No late students are present.")
    