# A spam comment is defined as a text containing  following rewords.
# "make a lot of money","buy row","subscribe this","click this",write a program to delete these spam.

text = input('Enter the text ')
#  spam = False
 
if("make a lot fo monry"in text):
     spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False
    
if(spam):
    print("This is spam text ")
else:
    print("This is mot spam.")