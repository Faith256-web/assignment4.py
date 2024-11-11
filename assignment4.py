# create a cohort 4 class width:
# name, description, start date, end date
# add a constructor for the cohort class
# create a function/ add a method to the class that prints the cohort name and the total number of students
# create a new instance / objects of cohort class

class cohort:
 def __init__(self, name, description, start_date, end_date, num_students): 
   self.name = name
   self.description  = description
   self.start_date = start_date
   self.end_date = end_date
   self.student_total_num = num_students
 def print_cohort_info(self):
     print(f"cohort name:{self.name}")
     print(f"total number of students:{self.student_total_num}")

cohort4 =cohort (name = "data science",
                 description="course on data science and machine learning.",
                 start_date= "21-08-2024",end_date= "12-12-2026",
                 num_students= 58 )
cohort4.print_cohort_info()