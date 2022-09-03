# Repeat program 4 for a list of such words to be censored.

words = ['hello','he',"donkey"] 

with open("ch-9/multiple_text.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"#####")

with open("ch-9/multiple_text.txt","w") as f:
    f.write(content)