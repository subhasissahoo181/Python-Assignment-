# Write a program to find out the line number where python is present from ques 6.

content = True
i=1
with open("ch-9/log.txt") as f:

    while content:
        content = f.readline()
        # 
        if 'python' in content.lower():
            print(content)
            print("Yes python is present.")
            print(i)
            i+=1
        else:
            print("No python is not present.") 