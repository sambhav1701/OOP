from datetime import date

import StudentClass as SC

#DOB = input("Enter your DOB in the format YYYY-MM-DD ")

student = SC.Student(1, "Sam", date(1998,1,17), "Sr")
student.current_age()
student.registration_dates()



