x = int(input())
marksheet = dict()
for i in range(x):
	name = str(input())
	mark = int(input())
	marksheet[name]=mark

for name,mark in sorted(marksheet.items()):
	print(name , ":" , mark)