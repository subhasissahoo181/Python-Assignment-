# Write a program to fill in a letter template given bellow with name and date.
# letter = ''' Dear <|NAME}>,
#                  You are Selected!
#                  <|DATE|>'''

# from token import NAME


# NAME = input("Enter Your Name.")
# DATE = input("Enter Today Date.")
# letter = ''' Dear ''' + NAME + '''\n You are Selected!
#         Date: '''+DATE

# print(letter)

# ------------------------------------------------


letter = ''' Dear <|NAME|>,
You are Selected!

Date:<|DATE|>'''
NAME = input("Enter Your Name. \n")
DATE = input("Enter Today Date.\n")
letter=letter.replace("<|NAME|>",NAME)
letter=letter.replace("<|DATE|>",DATE)
print(letter)