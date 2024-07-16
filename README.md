# AP-CSP-2
The Unit 3 Test Application Question for AP CSP

The provided code is the solution to the following question below:

After doing course selection, the [insert school] admin needs to figure out how many teachers they need next year!

They have all of the course sections assigned to blocks (Note that a block can have several different courses running!) and need to find out the minimum number of teachers they need.

For example,
minTeachers(ICS3UN01 = “A”, ICS3UN02 = “B”, ICS3UN03 = “C”) = 1    
Reason: because 1 teacher can teach each section!
minTeachers(ICS3UN01 = “A”, ICS3UN02 = “A”, ICS3UN03 = “A”) = 3        
Reason: because all of the sections are in the same block so 3 teachers are needed!
minTeachers(ICS3UN01 = “A”, ICS3UN02 = “A”, ICS3UN03 = “A”, MCR3UE01 = “B”) = 3        
Reason: because all of the ICS sections are in the same block so 3 teachers are needed, and one of them can still teach MCR in block B!


Create the function minTeachers that takes in an arbitrary number of course-block pairs and returns the minimum number of teachers needed.

Note: For this example, there is no restriction on teachers teaching too many courses and no restriction on teacher qualifications.



Marking Scheme:
Function created with correct name and parameters [1A]
Function returns correct integer number of teachers needed [2 A]
Function is tested on range of test cases and outcomes are printed [1A]
(To see how to format test cases, go to Homework 3.3.3)
Code organization rubric: [1A]
