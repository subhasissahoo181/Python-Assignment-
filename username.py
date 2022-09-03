#Write a program to find wheather a given userName contains less than 10 charecters or not.

username= input('Enter your name: ')
user_len = len(username)
if(user_len > 10):
    print('The userNeme contain greaterthan 10 character.')
else:
    print('The userNeme contain less than 10 character.')