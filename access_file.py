# use open function to read open the file
# f = open('sample.txt', 'r')
f = open('sample.txt')
data = f.read()
print(data)
f.close()