class Student:
	def __init__(bright):
		bright.student_details = {}
 
	@property
	def input_student_details(bright):	
		roll_number = input("Enter Roll Number : ")
		name = input("Enter Student Name : ")
		Attendancepercent = int(input("Enter Attendance percentage : "))
		bright.student_details[roll_number] = {'name': name, 'Attendance percentage': Attendancepercent}
		print("Attendance percentage Added successfully")
 
	def update_student_Attendancepercent(bright):	 
		roll_number = input("Enter Roll Number of the Student to Update Attendance percentage : ")
		if roll_number in bright.student_details:
			new_Attendancepercent = int(input("Enter New Attendance percentage : "))
			bright.student_details[roll_number]['Attendance percentage'] = new_Attendancepercent
			print("Attendance percentage updated successfully")
		else:
			print("Student not found")
 
	def print_student_details(bright):	
		roll_number = input("Enter Roll Number of the student to view details : ")
		if roll_number in bright.student_details:
			student = bright.student_details[roll_number]
			print("Roll Number :", roll_number)
			print("Student Name :", student['name'])
			print("Attendance percentage :", student['Attendance percentage'])
		else:
			print("Student not found")
 
obj = Student()
 
while True:
    print("\n ********* Student Management System *********  ")
    print("\n1. Input Student Details")
    print("2. Update Student Attendance percentage")
    print("3. Print Student Details")
    print("4. Exit")
 
    choice = input("\nEnter your Choice (1 to 4): ")
 
    if choice == '1':
        obj.input_student_details
    elif choice == '2':
        obj.update_student_Attendancepercent()
    elif choice == '3':
        obj.print_student_details()
    elif choice == '4':
        print("Exiting the program")
        break
    else:
        print("Invalid Choice. Please Try Again !!!")