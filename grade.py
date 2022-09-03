# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100 -> O.
# 80-90  -> E.
# 70-80 -> A.
# 60-70 -> B.
# 50-60 -> C.
# 40-50 -> D.
# 30-40 -> F.

mark = int(input('Enter the sequered marks. '))
if(mark>=90):
    print("Congratulations! You have secured O grade.")
elif(mark>=80):
    print("Congratulations! You have secured E grade.")
elif(mark>=70):
    print("Congratulations! You have secured A grade.")
elif(mark>=60):
    print("Congratulations! You have secured B grade.")
elif(mark>=50):
    print("Congratulations! You have secured C grade.")
elif(mark>=40):
    print("Congratulations! You have secured D grade.")
elif(mark>=30):
    print("Congratulations! You have Pass.")
elif( mark<30):
    print("Sorry You failed!")
else:
    print("Invalid mark.")
    