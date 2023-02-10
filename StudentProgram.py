from datetime import date

import StudentClass as SC

DOB = input("Enter your DOB in the format YYYY-MM-DD ")

student = SC.Student(1, "Sam", DOB, "Sr")
student.current_age()
student.registration_dates()



