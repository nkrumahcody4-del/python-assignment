# Create a function for school admission system. 
# A student can apply for admission by providing their name, age, email, grade
# The function should check if the student is eligible for admission based 
# on grade
# If the student is eligible, 
# the function should return a message saying "Congratulations {name}, 
# you have been admitted to our school"
# If the student is not eligible, the function should return a message saying
#  "Sorry {name}, you are not eligible for admission"
# If the student is eligible, the function should also return the student's 
# profile which includes their name, age, email, and grade.
# If the student is not eligible, the function should not return the profile.
# The function should also store the student's profile in a local storage
# (a dictionary) if they are eligible for admission.


def student_profile(name, age, email,grade):
    profile = {
        'name': name,
        'age': age,
        'email': email,
        'grade': grade
    }
    return profile
student_profile = input("Enter your name, age, email and grade separated by commas: ")
print(student_profile)
name, age, email, grade = student_profile.split(',')
print(student_profile(name, age, email, grade))
student_grade = input("Kindly Enter Your Grade")
grade = 55
if grade >= 50:
    print (grade("You are eligible, Congratulations you have been admitted to our school {name}"))
elif grade >= 40:
 print (grade("Sorry {name}, you are not eligible for admission"))


