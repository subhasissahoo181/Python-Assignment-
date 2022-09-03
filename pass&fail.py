# Write a program to  find out whether a student is pass or fail if it requires total 40% and at least 33%  in each subject to pass assume 3 subjects and take marks as an input form the user.


sub1 = int(input('Enter the mark of subject 1: '))
sub2 = int(input('Enter the mark of subject 2: '))
sub3 = int(input('Enter the mark of subject 3: '))
total= int(((sub1+sub2+sub3)/300)*100)
if(sub1<33 or sub2<33 or sub3<33):
     print("You are fail in subject")
elif(total> 40):
    print('You are pass.')
else:
    print('You are fail.')